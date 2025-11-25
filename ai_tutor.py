"""
AI Tutor Module
Handles all AI-powered tutoring functionality including:
- Student profiling
- Problem generation
- Performance analysis
- Adaptive learning
"""

import sqlite3
import random
import string
from config import DB_PATH, AI_AVAILABLE, client, LEARNING_CATEGORIES
from google.genai import types


# ==================== USER PROFILE MANAGEMENT ====================

def load_user_profile(user_id):
    """Load user profile or create default profile if none exists"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    # Create default profile if none exists
    if row is None:
        cur.execute("""
            INSERT INTO UserLMSProfile (
                user_id, preferred_learner_style, target_difficulty,
                preferred_length, preferred_numeric_complexity,
                focus_category, performance_score, ai_goal, notes
            ) VALUES (?, 'visual', 2, 'medium', 'integers_only',
                    'procedural', 0, 'teach_new', 'No notes')
        """, (user_id,))
        conn.commit()
        cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
        row = cur.fetchone()

    columns = [c[0] for c in cur.description]
    profile = dict(zip(columns, row))

    conn.close()
    return profile


def get_full_performance(user_id):
    """Get performance statistics by category"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT p.category, SUM(pp.is_correct), COUNT(*)
        FROM PracticeProblem pp
        JOIN GenProblem p ON p.id = pp.genProblem_id
        JOIN PracticeProblemSet ps ON ps.id = pp.set_id
        WHERE ps.user_id=?
        GROUP BY p.category
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()

    all_cats = LEARNING_CATEGORIES
    performance_summary = {cat: 0 for cat in all_cats}

    total_correct = 0
    total_attempts = 0
    for cat, correct, total in rows:
        accuracy = round((correct / total) * 100, 1) if total > 0 else 0
        performance_summary[cat] = accuracy
        total_correct += correct
        total_attempts += total

    overall_score = round((total_correct / total_attempts) * 100, 1) if total_attempts > 0 else 0
    return performance_summary, overall_score


def load_context(user_id):
    """Generate comprehensive context for AI including student profile and history"""
    profile = load_user_profile(user_id)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Fetch last 20 attempts for context
    cur.execute("""
    SELECT pp.id, p.category, p.prompt, pp.student_answer, pp.is_correct
    FROM PracticeProblem pp
    JOIN GenProblem p ON p.id = pp.genProblem_id
    JOIN PracticeProblemSet ps ON ps.id = pp.set_id
    WHERE ps.user_id=?
    ORDER BY pp.id ASC
    LIMIT 20
    """, (user_id,))

    attempts = cur.fetchall()

    attempts_summary = "\n".join(
        [f"ID: {pid}, Category: {c}, Problem: {q}, Student Answer: {a}, Correct: {bool(s)}"
        for pid, c, q, a, s in attempts]
    )
    conn.close()

    perf_summary, overall_score = get_full_performance(user_id)
    perf_text = "\n".join([f"{cat}: {score}%" for cat, score in perf_summary.items()])
    cat_summary = f"\nOverall Performance Score: {overall_score}%\nCategory Performance:\n{perf_text}"

    return f"""
        <identity>
        You are a math tutor who creates personalized learning experiences for your students. You adapt your teaching methods based on each student's unique profile and learning history.

        You know your students by using their Student Profile that you maintain and update over time. Refer to <profile_structure> for details on each field.
        Here is the current profile for the student you are tutoring:
        Preferred Style: {profile['preferred_learner_style']}
        Difficulty: {profile['target_difficulty']}
        Numeric Pref: {profile['preferred_numeric_complexity']}
        Focus Category: {profile['focus_category']}
        Notes: {profile['notes']}

        Knowledge Types are the key categories of problems or content you create. These are the most important variables in tailoring learning experiences:
        - Factual: General info/facts about the topic/goal.
        - Procedural: Specific steps to solve a problem (like a room in a house).
        - Strategic: Multi-step problems; culmination of procedural steps (The entire house).
        - Rational: Explanations behind concepts; the "why".

        ALWAYS Be unique and creative in your generation, avoiding repetition, while not overcomplicating. This applies to both problems and answers.

        You will analyze the student's most recent problems (Up to 20 problem attempts) to inform your decisions about their profile and future problem generation.
        Here are their recent attempts (oldest first):
        {attempts_summary}
        Here is a summary of their performance across all attempts:
        {cat_summary}
        </identity>

        
        <profile_structure>
        - Preferred Style: ('visual', 'Learns best with diagrams, charts, and images'), ('auditory', 'Learns best with listening and discussion'), ('reading_writing', 'Learns best with text and notes'),
        ('kinesthetic', 'Learns best with hands-on activities'), ('logical', 'Learns best with reasoning and systems'), ('social', 'Learns best in group settings'),
        ('solitary', 'Learns best independently'), ('nature', 'Learns best through real-world and environmental examples')
        **Be aware that preferred style may not always be represented in problem generation, but should influence your approach when possible.**
        **Nature in this interpretation means real-world examples, not just outdoors or plants**
        - Difficulty: (1, 'Intro', 'Entry-level, simple problems'), (2, 'Core', 'Typical grade-level problems'), (3, 'Challenge', 'Challenging but solvable'),
        (4, 'Advanced', 'Above grade-level complexity'), (5, 'Expert', 'Very difficult, enrichment');
        - Numeric Pref: ('integers_only', 'Whole numbers only'), ('simple_fractions', 'Simple fractions included'), ('decimals', 'Decimals included'),
        ('negatives', 'Negative numbers included'), ('mixed', 'Combination of multiple number types'), ('radicals', 'Square roots or higher roots included');
        - Focus Category: (factual, procedural, strategic, rational); Should be the category the student has most difficulty with or categories the student has little exposure to yet.
            * Focus Category should not be the only category used, but should be an emphasized area where the student needs more practice.
        - Notes: Key insights about the student's interests, challenges, and preferences. 
        ** Use notes to store information you as the tutor have observed about the student that you will want to remember for future problem generation. **
        ** The notes section is your memory of the student, so include anything you think is relevant to help you tutor them better. **
        ** Notes are not only used to keep track of student informaion, but also allow you to make notes to yourself. If you notice question generation is failing to meet constraints, or
        if you believe the questions or answers could be improved, include that in notes for your future reference. **
        ** Still mainatin conciseness and relevance. Avoid overly long notes. **
        - AI Goal: ('teach_new', 'Focus on teaching new concepts'), ('challenge', 'Focus on challenging the student'), ('review', 'Focus on reviewing known concepts').
        The student should be in a 'teach_new' mode if they are first learning a topic, haven't performed much across all categories, or have a low performance score.
        They should be in 'challenge' mode if they are doing well (80+ score) and their specific knowledge category they struggle with needs extra focus (70- in that category).
        They should be in 'review' mode if they are consistently performing well (80+ score) or need reinforcement of concepts.
        The student should only rarely be in 'challenge' mode for extended periods; rotate between 'teach_new' and 'review' more often. 
        - Performance Score: A numeric value (0-100) representing overall performance. A student is passing if score >= 70. Though 80+ is ideal.
        </profile_structure>
    """


# ==================== AI PROFILE ALGORITHM ====================

def Profile_Alg(user_id):
    """AI-driven algorithm to update student profile based on performance"""
    if not AI_AVAILABLE:
        return

    profile = load_user_profile(user_id)
    context = load_context(profile["user_id"])
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))

    prompt = f"""
        {context}

        <task>
        Analyze student learning patterns and continuously refine an internal learning profile to optimize future problem generation.
        You do not invent information; you infer patterns only from data provided.
        Analyze the student's last 20 problem attempts and produce a concise, updated student profile.
        The goal is to maintain accurate reflection of the student's learning progress, preferred style,
        and focus areas while adjusting only when justified by clear evidence.
        </task>

       <constraints>
        - ALWAYS use evidence-based reasoning only.
        - ALWAYS keep tone neutral, factual, and analytic (no motivation, emotion, or praise).
        - ALWAYS update 'focus_category' based on weakest category performance.
            * Categories with no attempts should be prioritized
        - ALWAYS Compute Performance Score as the accuracy percentage across the last 20 attempts (or all attempts if fewer than 20).
        - ALWAYS output <Format> exactly as specified. Use <profile_strucure> for context on fields.
        - ALWAYS review your output for consistency and accuracy.
        - NEVER fabricate interests or traits.
        - NEVER modify fields not listed in <format>.
        - Notes should summarize observed learning behavior and suggest strategies.
            * Include relevant observations on category performance.
            * Ensure the category balance rules are followed. If not, mention that adjustments are needed.
            (Ex. Out of 20 problems, generally aim for 5 factual, 5 procedural, 5 strategic, 5 rational. If focus_category performance < 70%, aim for ~7 in that category and ~4 in others.
            ONLY exception to this rule set is if overall attempts of any category is 10 + the next highest category. In this case, prioritize the underrepresented category.
            (Ex. If factual=15, procedural=4, strategic=3, rational=2, choose procedural/strategic/rational until factual evens out (<=5 attempts difference next highest))
            * If interest are implemented within problems to frequently, suggest reducing their use in notes.
        - If adjusting difficulty, do so by +/- 1 at most.
        </constraints>

        <Format>
        Preferred Learner Style: ...
        Target Difficulty: ...
        Preferred Length: ...
        Preferred Numeric Complexity: ...
        Focus Category: ...
        Performance Score: ...
        AI Goal: ...
        Notes: ...
        </Format>

        [variation:{noise}]
    """

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=300
            )
        )
        text = resp.candidates[0].content.parts[0].text.strip()

        # Parse AI output
        updates = {}
        for line in text.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                updates[key.strip().lower().replace(" ", "_")] = value.strip()

        # Allowed columns in UserLMSProfile
        allowed_cols = ["preferred_learner_style", "target_difficulty", "preferred_length",
                        "preferred_numeric_complexity", "focus_category",
                        "performance_score", "ai_goal", "notes"]

        numeric_fields = ["target_difficulty", "performance_score"]

        updates_filtered = {}
        for k, v in updates.items():
            if k in allowed_cols:
                if k in numeric_fields:
                    try:
                        # Keep digits and decimal point
                        num_str = ''.join(c for c in v if c.isdigit() or c == '.')
                        num_val = float(num_str)

                        # Clamp values
                        if k == "performance_score":
                            num_val = max(0, min(100, num_val))   # Performance 0–100%
                        elif k == "target_difficulty":
                            num_val = max(1, min(5, num_val))     # Difficulty 1–5

                        updates_filtered[k] = num_val
                    except:
                        updates_filtered[k] = None  # fallback if parsing fails
                else:
                    updates_filtered[k] = v

        if updates_filtered:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            set_clause = ", ".join([f"{k}=?" for k in updates_filtered.keys()])
            values = list(updates_filtered.values()) + [user_id]

            cur.execute(f"""
                UPDATE UserLMSProfile
                SET {set_clause}
                WHERE user_id=?
            """, values)

            conn.commit()
            conn.close()

    except Exception as e:
        print("Error updating profile:", e)


# ==================== AI PROBLEM GENERATION ====================

def generate_problem(obj_title, obj_desc, profile):
    """Generate a problem using AI based on student profile and learning objective"""
    if not AI_AVAILABLE:
        return None, None, None

    context = load_context(profile["user_id"])
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))

    categories = LEARNING_CATEGORIES
    bias = random.choice(categories)

    prompt = f"""
        {context}

        <task>
        Generate one (1) math problem tailored to the student's profile and learning history.
        You will create a problem for the following Learning Objective:
        Title: {obj_title}
        Description: {obj_desc}
        The problem must be clear, concise, and appropriately challenging.
        </task>

        <constraints>
        - ALWAYS be concise (max 4 sentences for question).
        - ALWAYS include a correct answer.
        - ALWAYS base the output on the following categories: factual, procedural, strategic, rational.
        - ALWAYS output <format> exactly as specified.
        - ALWAYS ensure long-term category balance across multiple generations. This rule supersedes all other constraints:
            * If the student recently had too many of one category, choose a different one. Ideally, rotate categories evenly (25% each if possible).
            * Review the student's recent problems to determine category distribution.
            (Ex. If they have only been asked 3 of the 4 categories recently, choose the missing one)
            (Ex. If one category is overrepresented, avoid it this time)
            * If the student has not completed 20 problems yet, aim for equal distribution across all categories. (25% each before focus_category adjustments)
            * Favor the student's focus_category if their performance in that category is below 70%. (Split should be 33/67 between focus and others until performance improves).
            * NEVER repeat the same category more than twice in a row UNLESS their performance is below 50% in that category. NEVER repeat more than 3 times in a row.
            * ONLY exception to this rule set is if overall attempts of any category is 10 + the next highest category. In this case, prioritize the underrepresented category.
            (Ex. If factual=15, procedural=4, strategic=3, rational=2, choose procedural/strategic/rational until factual evens out (<=5 attempts difference next highest))
        - Use student interests (from Notes) ONLY when:
            * The student's performance in that category is below 70%.
            * AND the topic benefits from real-world analogies.
            * Student interests should ONLY be used to reinforce engagement or to aid understanding. Interests should NOT be incorporated into every problem.
        - Avoid fabricated interests or irrelevant context.
        - ALWAYS adapt your tone and problem design based on the student's AI goal:
            - If AI Goal = 'teach_new':
                * Favor easier difficulty within the student's target range.
                * Use approachable phrasing.
            - If AI Goal = 'challenge':
                * Slightly increase difficulty beyond their target_difficulty.
                * Only maintain this if the student's overall performance is above 85% AND their focus category performance is above 75%.
            - If AI Goal = 'review':
                * Keep difficulty equal to target_difficulty.
                * Use gentle recap tone or "apply what you know" phrasing.
        - Regardless of goal, maintain category diversity over time.
        - Use word problems appropriately to enhance engagement without overcomplicating. Use ONLY IF needed to create the problem type, introduce variety, align with student interests, or match difficulty.
            * Difficulty levels 4-5 should favor word problems more often. 2-3 should use them sparingly. Level 1 should avoid them unless necessary (likely for factual and rational).
        - ALWAYS review your output for consistency and accuracy. Make sure the problem aligns with all constraints and the student's profile. As the tutor, you should feel that this problem is well-suited to help the student learn effectively.
            * Ensure the category balance rules are followed. (Ex. Out of 20 problems, generally aim for 5 factual, 5 procedural, 5 strategic, 5 rational. If focus_category performance < 70%, aim for ~7 in that category and ~4 in others)
        </constraints>


        <answer_format>
        - Factual / Rational -> short, direct textual responses (less than or equal to 2 sentences) (One word answers are preferred if applicable).
        - Procedural / Strategic -> final numeric or algebraic answer only, no full walkthrough.
        - Do NOT leave the answer blank.
        </answer_format>

        <format>
        Category: [factual / procedural / strategic / rational]
        Problem: ...
        Answer: ...
        </format>

        [variation:{noise}]
    """

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.8,
                max_output_tokens=200
            )
        )
        text = resp.candidates[0].content.parts[0].text.strip()

        category = None
        problem = ""
        answer = ""

        # Parse category
        if "Category:" in text:
            after = text.split("Category:")[1].strip()
            category_line = after.splitlines()[0].strip()
            category = category_line.lower()

        # Parse problem & answer
        if "Problem:" in text:
            prob_part = text.split("Problem:")[1]
            if "Answer:" in prob_part:
                prob_text, ans_text = prob_part.split("Answer:")
                problem = prob_text.strip()
                answer = ans_text.strip()
            else:
                problem = prob_part.strip()

        return problem, answer, category

    except Exception as e:
        print("Error generating problem:", e)
        return None, None, None


