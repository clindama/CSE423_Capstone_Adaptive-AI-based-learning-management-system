import tkinter as tk
from tkinter import messagebox
import sqlite3
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

class PracticeAI:
    def run(self):
        self.window.mainloop()
        
    def __init__(self, db_path="learning_platform.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Load all problems ordered by ID
        self.cursor.execute("SELECT id, prompt, correct_answer FROM Problem ORDER BY id ASC")
        self.problems = self.cursor.fetchall()
        self.current_index = 0
        self.tracked_scores = []  # Stores (problem_id, prompt, user_answer, score)

        self.window = tk.Tk()
        self.window.title("AI Practice Tutor")
        self.window.geometry("750x600")

        self.prompt_label = tk.Label(self.window, text="", font=("Helvetica", 14), wraplength=700, justify="left")
        self.prompt_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.window, font=("Helvetica", 12), width=60)
        self.answer_entry.pack(pady=10)

        self.submit_btn = tk.Button(self.window, text="Submit Answer", command=self.check_with_ai)
        self.submit_btn.pack(pady=5)

        self.hint_btn = tk.Button(self.window, text="Walkthrough", command=self.ask_for_hint)
        self.hint_btn.pack(pady=5)

        self.hint_display = tk.Text(self.window, font=("Helvetica", 12), height=20, width=85, wrap="word")
        self.hint_display.pack(pady=10)
        self.hint_display.config(state="disabled")

        self.load_problem()
        self.window.mainloop()

    def load_problem(self):
        if self.current_index >= len(self.problems):
            self.show_summary()
            return

        problem = self.problems[self.current_index]
        self.problem_id = problem[0]
        self.current_prompt = problem[1]
        self.correct_answer = problem[2]
        self.prompt_label.config(text=f"Problem {self.problem_id}: {self.current_prompt}")
        self.answer_entry.delete(0, tk.END)
        self.clear_hint_display()

    def clear_hint_display(self):
        self.hint_display.config(state="normal")
        self.hint_display.delete("1.0", tk.END)
        self.hint_display.config(state="disabled")

    def check_with_ai(self):
        user_answer = self.answer_entry.get().strip()

        prompt = f"""
You are a supportive math tutor grading a student's response.

Problem: {self.current_prompt}
Student Answer: {user_answer}
Correct Answer: {self.correct_answer}

Grade the student's answer from 0 to 100.
- Give partial credit for close or mostly correct answers.
- Minor formatting or notation differences should not heavily reduce the score.
- Only return a number, no explanation.
- Use your own knowledge and solve the problem when determining the score, don't just compare to the correct answer.
- For multiple choice problems, only give 0 or 100
- If nothing is next to Student Answer: give a 0
"""
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_completion_tokens=10,
                top_p=1,
                stream=False
            )
            ai_response = completion.choices[0].message.content.strip()
            score = int("".join(filter(str.isdigit, ai_response.splitlines()[0])))

            self.tracked_scores.append((self.problem_id, self.current_prompt, user_answer, score))

            if score >= 80:
                messagebox.showinfo("Passed", f"AI rated your answer {score}/100. Moving to the next problem.")
                #Add tracking here
            else:
                messagebox.showwarning("Not Quite", f"AI rated your answer {score}/100. You can review it later.")
                #Add tracking here

            self.current_index += 1
            self.load_problem()

        except Exception as e:
            messagebox.showerror("Error", f"AI check failed: {str(e)}")

    def ask_for_hint(self):
        prompt = f"""
You are a math tutor. Give a walk through for this problem with all varibles and numbers change so you dont give the original answer, DONT USE EMOJIS ONLY TEXT NO SPECIAL CODES, give a maximum of 500 words and make it so an young student could understand:
{self.current_prompt}
"""
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_completion_tokens=600,
                top_p=1,
                stream=False
            )
            hint = completion.choices[0].message.content.strip()
            self.hint_display.config(state="normal")
            self.hint_display.delete("1.0", tk.END)
            self.hint_display.insert(tk.END, hint)
            self.hint_display.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve hint: {str(e)}")

    def show_summary(self):
        avg_score = sum(score for (_, _, _, score) in self.tracked_scores) / len(self.tracked_scores)
        messagebox.showinfo("Session Complete", f"You completed all problems.\nAverage Score: {avg_score:.2f}%")

        lowest = sorted(self.tracked_scores, key=lambda x: x[3])[:5]
        advice_prompt = """
You are an AI tutor. A student just completed a practice session. Here are the 5 problems they scored lowest on:

"""
        for pid, question, answer, score in lowest:
            advice_prompt += f"Problem {pid}: {question}\nStudent Answer: {answer}\nScore: {score}/100\n\n"

        advice_prompt += "\nWhat should this student focus on studying next? Give specific advice based on these questions."

        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": advice_prompt}],
                temperature=0.6,
                max_completion_tokens=300,
                top_p=1,
                stream=False
            )
            feedback = completion.choices[0].message.content.strip()
            messagebox.showinfo("Study Advice", feedback)
        except Exception as e:
            messagebox.showerror("Error", f"Could not get study advice: {str(e)}")

# Run the GUI

if __name__ == "__main__":
    PracticeAI().run()
