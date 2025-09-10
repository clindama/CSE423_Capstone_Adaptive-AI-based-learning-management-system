
-- This is an example outline of what I plan to change with problems to allow for 
-- the LMS variable inclusion. It is still a work in progress 

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Simplify the expression 4(x + 3) - 2x.',
    '2x + 12',
    'procedural'
);

-- 1. Difficulty Band
INSERT INTO ProblemDifficultyLink (problem_id, difficulty_id)
VALUES (10, (SELECT id FROM DifficultyBand WHERE name = 'Core'));

-- 2. Numeric Complexity
INSERT INTO ProblemNumericComplexityLink (problem_id, numeric_complexity_id)
VALUES (10, (SELECT id FROM NumericComplexity WHERE name = 'integers_only'));

-- 3. Representation Mode
INSERT INTO ProblemRepresentationLink (problem_id, representation_mode_id)
VALUES (10, (SELECT id FROM RepresentationMode WHERE name = 'visual'));

-- 4. Instructional Strategy
INSERT INTO ProblemStrategyLink (problem_id, strategy_id)
VALUES (10, (SELECT id FROM InstructionalStrategy WHERE name = 'scaffolding'));

-- 5. Engagement Method
INSERT INTO ProblemEngagementLink (problem_id, engagement_id)
VALUES (10, (SELECT id FROM EngagementMethod WHERE name = 'real_world'));

-- 6. Teaching Style
INSERT INTO ProblemTeachingLink (problem_id, teaching_style_id)
VALUES (10, (SELECT id FROM TeachingStyle WHERE name = 'facilitator'));


-- ===========================================================
-- 1.1 Expressions
-- ===========================================================

-- Expressions - Objective 1
-- Factual Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'What is an algebraic expression?',
    'An algebraic expression is a mathematical phrase that can contain numbers, variables, and operation symbols.',
    'factual'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Which of the following is NOT an algebraic expression: A) 2x + 3, B) 7, C) = 4x - 1, D) x^2 - 5?',
    'C) = 4x - 1',
    'factual',
);

-- Procedural Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Combine the like terms: 3x + 5 + 2x.',
    '5x + 5',
    'procedural'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Rewrite the expression 4(x + 2) using the distributive property.',
    '4x + 8',
    'procedural'
);

-- Strategic Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Simplify the expression 6(x - 2) + 3x.',
    '9x - 12',
    'strategic'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Simplify 3(x + 3) + 4x - 1?',
    '7x + 8',
    'strategic'
);

-- Rational Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Why can we combine the terms 2x and 5x, but not 2x and 3y?',
    'Because 2x and 5x are like terms (same variable), while 2x and 3y are not.',
    'rational'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Explain why simplifying expressions is important before solving equations.',
    'It makes equations easier to solve and reduces the chance of mistakes.',
    'rational'
);

-- Expressions - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'What is an algebraic expression?',
  'A mathematical phrase that includes numbers, variables, and operations but no equals sign.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'In the expression 5x + 7, what does the variable represent in a real-world context?',
  'It represents an unknown quantity that can change based on the situation.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Translate the sentence into an expression:' || CHAR(10) ||
  '"Seven more than twice a number."',
  '2x + 7',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Write an algebraic expression for the phrase:' || CHAR(10) ||
  '"The product of a number and 4 decreased by 9."',
  '4x - 9',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'A taxi company charges $3 for pickup and $2 per mile. Write an expression for the cost of a ride that is m miles long.' || CHAR(10) ||
  'Explain your reasoning.',
  '3 + 2m || Fixed cost is $3, variable cost is $2 per mile.',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Write an expression to represent the cost of x movie tickets if each ticket costs $12, and you also buy a snack combo for $5.' || CHAR(10) ||
  'Show the full expression and explain what each part represents.',
  '12x + 5 || 12x for tickets, 5 for the combo.',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Why is it helpful to convert word problems into algebraic expressions?',
  'It allows us to use mathematical reasoning to solve real-world problems and make generalizations.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'How does identifying keywords (like "sum" or "product") help in writing algebraic expressions?',
  'They signal the mathematical operation needed, guiding how to build the expression correctly.',
  'rational'
);

-- ===========================================================
-- 1.2 Combining Like Terms
-- ===========================================================
-- Combining Like Terms - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Which of the following are like terms?' || CHAR(10) ||
    'A) 3x and 5y' || CHAR(10) ||
    'B) 2x and 7x' || CHAR(10) ||
    'C) 4 and 4x' || CHAR(10) ||
    'D) x^2 and x',
    'B',
    'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'What makes two terms "like terms"?' || CHAR(10) ||
    'A) Same coefficients' || CHAR(10) ||
    'B) Same variable raised to the same power' || CHAR(10) ||
    'C) Any numeric terms' || CHAR(10) ||
    'D) Identical signs',
    'B',
    'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Identify and group the like terms in the expression:' || CHAR(10) ||
    '7x + 3y - 2x + 5y',
    '7x and -2x || 3y and 5y',
    'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Group the like terms from the expression below:' || CHAR(10) ||
    '8a + 2b + 3a - b + 4',
    '8a and 3a || 2b and -b',
    'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'You are given the expression: 4x + 2y - 3x + y - 6.' || CHAR(10) ||
    'Simplify it.',
    'x + 3y - 6',
    'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'You need to simplify this expression for a final answer:' || CHAR(10) ||
    '6m - 4 + 2m - 3m + 10.',
    '4m + 6',
    'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Why can''t you combine 4x and 5y when simplifying an expression?',
    'They are not like terms because they have different variables.',
    'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Why is it important to identify like terms before combining them?',
    'Because combining unlike terms leads to incorrect simplification and violates algebraic rules.',
    'rational'
);

-- Combining Like Terms - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'What does it mean to simplify an algebraic expression?',
  'To combine like terms and rewrite the expression in its simplest form.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Which terms can be combined in the expression 3x + 5 + 7x - 2?',
  '3x and 7x; 5 and -2 are constants but can be combined as well.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Identify like terms in the expression: 4a + 3b - 2a + 7b.',
  '4a and -2a; 3b and 7b. 2)',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Identify like terms in the expression 6x - 4 + 2x + 9?',
  '6x and 2x; -4 and 9.'
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Given the expression 5m + 3n - 2m + 7, simplify it.',
  '3m + 3n + 7.',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Simplify an expression with multiple variables and constants, like 2x + 3y - x + 5 - 2y + 7?',
  'x + y + 12.',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Why do we combine like terms when simplifying expressions?',
  'To reduce the expression to its simplest form, making it easier to understand and solve.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'How does combining like terms help in solving equations?',
  'It simplifies the equation, reducing the number of terms, and makes it easier to isolate variables.',
  'rational'
);

-- ===========================================================
-- 1.3 Properties of Real Numbers
-- ===========================================================
-- Properties of Real Numbers - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Which property is illustrated by the equation below?' || CHAR(10) ||
    '(2 + 3) + 4 = 2 + (3 + 4)',
    'Associative Property of Addition',
    'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Which property allows you to write:' || CHAR(10) ||
    '6 * 3 = 3 * 6',
    'Commutative Property of Multiplication',
    'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Apply the distributive property to rewrite:' || CHAR(10) ||
    '5(2 + x)',
    '10 + 5x',
    'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Use the associative property to rewrite this expression without changing its value:' || CHAR(10) ||
    '(7 * 2) * 5',
    '7 * (2 * 5)',
    'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'You are given an expression: 3(x + 4) + 2x.' || CHAR(10) ||
    'Simplify it using the distributive and addition properties.',
    '5x + 12',
    'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
    'You want to simplify: (x + 2) + (3x + 5).',
    '4x + 7',
    'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Why is it valid to switch the order in 7 + 2 = 2 + 7?',
    'Because the commutative property of addition states that changing the order does not change the sum.',
    'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Why does the distributive property matter when simplifying expressions like 4(x + 2)?',
    'It allows multiplication to apply across addition, breaking expressions into manageable parts.',
    'rational'
);

-- Properties of Real Numbers - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'What is the associative property in algebra?',
  'The associative property states that (a + b) + c = a + (b + c).',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Name two properties of real numbers used to simplify expressions.',
  'Commutative property and associative property.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Simplify 3(x + 4) using the distributive property.',
  '3x + 12.',
  'procedural'
);

-- ================= Good for testing multiple answer formats =================
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Use the associative property to simplify the expression (2+ 7x) + 3x.',
  '(7x + 3x) = 2 + 10x = 10x + 2',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'When simplifying expressions, how do you decide when to apply the distributive property versus combining like terms?',
  'Apply the distributive property first to remove parentheses, then combine like terms to simplify further.',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Simplify the expression 2(x + 3) + 4x.',
  '6x + 6.',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Why is the distributive property important when simplifying algebraic expressions?',
  'It allows you to remove parentheses by distributing multiplication over addition or subtraction, simplifying calculations.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Explain why combining like terms alone is not always sufficient to simplify expressions.',
  'Because expressions may have parentheses or multiplication needing the distributive property before combining like terms.',
  'rational'
);

-- ===========================================================
-- 1.4 Exponents and Order of Operations
-- ===========================================================
-- Exponents and Order of Operations - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'What does the P stand for in PEMDAS?',
    'Parentheses',
    'factual'
);


INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'Which operation should be performed first in the expression 3 + 4 * 2?' || CHAR(10) || 'A) Addition' || CHAR(10) || 'B) Multiplication' || CHAR(10) || 'C) Subtraction' || CHAR(10) || 'D) Division',
    'B multiplication',
    'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'Perform the first operation for: 2 + 3 * (4 - 1).',
    'Perform (4 - 1) first, which equals 2 + 3 * 3.',
    'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'What is the value of 2^3?',
    '8',
    'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'Simplify the expression 3 + 4 * 2^2?',
    '3 + 4 * 4 = 3 + 16 = 19',
    'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'What is the value of 3 + 2 * (3^2 - 1)?',
    '3 + 2 * 8 = 3 + 16 = 19',
    'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'Why is it important to follow the order of operations in mathematics?',
    'To ensure consistent and correct results when evaluating expressions.',
    'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
    (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 1'),
    'Explain why parentheses are used in the order of operations.',
    'Parentheses indicate which operations should be performed first, ensuring clarity in complex expressions.',
    'rational'
);

-- Exponents and Order of Operations - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'Are the following expressions equivalent?' || CHAR(10) ||
  '-4^2 and (-4)^2)?',
  'False, -4^2 = -16 while (-4)^2 = 16',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'The following is an example of which property?' || CHAR(10) ||
  '(a^x)^y = a^(x*y)' || CHAR(10) ||
  'A) Power of a Power Rule' || CHAR(10) ||
  'B) Power of a Product Rule' || CHAR(10) ||
  'C) Power of a Fraction Rule' || CHAR(10) ||
  'D) Multiplication of Powers Rule',
  'A Power of a Power Rule',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'What is the first step in simplifying the expression (2^3 * 2^4)?',
  'Apply the Multiplication of Powers Rule: a^m * a^n = a^(m+n) == 2^(3+4)',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'Simplify the expression (3^2)^3.',
  '3^(2*3) = 3^6 = 729',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'What is the final result of the expression (2^3 * 2^2) * 3^2?',
  '2^(3+2) * 3^2 = 2^5 * 9 = 32 * 9 = 288',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'Use Power Rules to simplify the expression (2^3 * 3)^2',
  '(2^3)^2 * 3^2 = 2^(3*2) * 3^2 = 2^6 * 9 = 64 * 9 = 576',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'Why is it important to understand the properties of exponents?',
  'Understanding properties of exponents helps simplify complex expressions and solve equations efficiently.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations'),
  (SELECT id FROM LearningObjective WHERE title = 'Exponents and Order of Operations - Objective 2'),
  'How does the order of operations affect the evaluation of expressions with exponents?',
  'It ensures that exponents are calculated before multiplication or addition, leading to correct results.',
  'rational'
);

-- ===========================================================
-- 1.5 Absolute Value
-- ===========================================================
-- Absolute Value - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'What is the definition of absolute value?',
  'The absolute value of a number is its distance from zero on the number line, regardless of direction.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'What symbol is used to denote absolute value?',
  '||',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'What is the absolute value of -8?',
  '8',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'What is the absolute value of 23?',
  '23',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'If the absolute value of x is 7, what are the possible values of x?',
  'x can be 7 or -7.',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'What is the value of the expression |-5| + |3|?',
  '8',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'Why is the absolute value of a number always non-negative?',
  'Because absolute value represents distance from zero, which cannot be negative.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'How does understanding absolute value help in solving equations?',
  'It allows us to find all possible solutions that are equidistant from zero.',
  'rational'
);

-- Absolute Value - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  'Is the distance from -5 to 0 the same as the distance from 5 to 0?',
  'Yes, both distances are 5.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Which of the following is an absolute value expression?' || CHAR(10) ||
  'A) x + 3' || CHAR(10) || 'B) |x - 5|' || CHAR(10) || 'C) (x - 2)' || CHAR(10) || 'D) (x + 4)',
  'B |x - 5|',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Simplify the expression |3 * -7|.',
  '21',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Simplify the expression |4 - 9|.',
  '5',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Simplify the expression |4 - 3| + |8 + 2|.',
  '1 + 10 = 11',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Simplify the expression |4 * -3| - |8 + 2|.',
  '12 - 10 = 2',
  'procedural'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Why are the following expressions equivalent? |a - b| and |b - a|.',
  'Because both expressions represent the distance between a and b on the number line.',
  'rationale'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Absolute Value'),
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  'Why do we treat the absolute value sign || the same as parentheses when simplifying expressions?',
  'Because absolute value signs indicate that we should evaluate the expression inside them first, similar to parentheses.',
  'rational'
);

-- ===========================================================
-- 1.6 Simplify Expressions
-- ===========================================================
-- Simplify Expressions - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'What does an expression not have that separates it from an equation?',
  'An equal sign.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Which of the following is an expression?' || CHAR(10) ||
  'A) x + 5 = 10' || CHAR(10) ||
  'B) 3x - 2' || CHAR(10) ||
  'C) y / z = 4' || CHAR(10) ||
  'D) a^2 + b^2 = c^2',
  'B 3x - 2',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Find the like terms in the expression 3x + 5x - 2y + 2 - 3y.',
  '3x and 5x are like terms; -2y and -3y are like terms.',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Use the distributive property to simplify the expression 3(x + 2).',
  '3x + 6',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Simplify the expression 2(x + 3) + 4x.',
  '2x + 6 + 4x = 6x + 6',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Simplify the expression 5(2x + 3y) - 2(3x - 4).',
  '10x + 15y - 6x + 8 = 4x + 15y + 8',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Why is it important to simplify expressions?',
  'Simplifying expressions makes them easier to work with and understand, especially in solving equations.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Explain the importance of following the order of operations when simplifying expressions.',
  'Following the order of operations ensures that expressions are simplified correctly and consistently.',
  'rational'
);

-- Simplify Expressions - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 2'),
  'Where in PEMDAS does absolute value fall?',
  'Absolute value is evaluated along with parentheses, so it is part of the P in PEMDAS.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 2'),
  'What property allows us to perform the following: a^x * a^y = a^(x + y)?',
  'Multiplication of Powers Rule',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Use power rules to simplify the expression (2^3 * 2^2).',
  '8 * 4 = 32',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 2'),
  'Simplify the expression |3 - 4| -  |4 - 3| ',
  '1 - 1 = 0',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Simplify the expression |3 - (2^3 + 2^2)|.',
  '|3 - (8 + 4)| = |3 - 12| = |-9| = 9',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 1'),
  'Simplify the expression (7 - 2)(2x + 3^2)',
  '5(2x + 9) = 10x + 45',
  'strategic'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 2'),
  'Why do we use properties of exponents when simplifying expressions?',
  'Properties of exponents allow us to rewrite and combine expressions more easily, making simplification straightforward.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Simplifying Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Simplifying Expressions - Objective 2'),
  'Explain how order of operations and properties simplify complex expressions.',
  'Order of operations and properties allow us to break down complex expressions into simpler parts, making them easier to evaluate.',
  'rational'
);

-- ===========================================================
-- 1.7 Evaluating Expressions
-- ===========================================================
-- Evaluating Expressions - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'What does it mean to evaluate an expression?',
  'To evaluate an expression means to substitute values for variables and simplify the result.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'What is a variable in an algebraic expression?',
  'A variable is a symbol, usually a letter, that represents an unknown or changeable value.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'Evaluate the expression 3x + 2 when x = 4.',
  '14',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'Evaluate the expression 2a - 5 when a = 6.',
  '7',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'Evaluate the expression 4x - 2y + z when x = 3, y = 2, and z = 5.',
  '11',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'A student substitutes x = 5 and y = -1 into the expression 2x^2 + 3y. What is the result?',
  '47',
  'strategic'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'Why is it important to substitute values correctly when evaluating expressions?',
  'Incorrect substitution leads to wrong answers; accurate substitution ensures valid results in problem solving.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  'How can substituting variables help in real-world problem solving?',
  'It allows us to calculate specific outcomes by applying real values to general formulas or models.',
  'rational'
);

-- Evaluating Expressions - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'What is the order of operations used in evaluating expressions?',
  'Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right).',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'What does PEMDAS stand for?',
  'Parentheses, Exponents, Multiplication, Division, Addition, Subtraction.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'Evaluate: 3 + 4 * 2',
  '11',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'Evaluate: (5 + 2) * 3',
  '21',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'Evaluate: 6 + (3^2 * 2) - 4',
  '20',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'Evaluate the expression: (8 + 2) / (2 * 2) + 5',
  '7.5',
  'strategic'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'Why is it important to follow the order of operations when evaluating expressions?',
  'It ensures consistency and accuracy in solving expressions, preventing different people from getting different answers.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Evaluate Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  'A student evaluates 3 + 5 * 2 as (3 + 5) * 2. What mistake did they make?',
  'They added before multiplying, ignoring the correct order of operations.',
  'rational'
);

-- ===========================================================
-- 1.8 Write Expressions from verbal
-- ===========================================================
-- Write Expressions from verbal - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'What algebraic operation is indicated by the phrase "sum of"?',
  'Addition (+)',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'What does the phrase "product of" mean in algebraic expressions?',
  'Multiplication (*)',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Translate the phrase "5 more than a number x" into an algebraic expression.',
  'x + 5',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Translate the phrase "twice a number y" into an algebraic expression.',
  '2 * y',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Write an expression for: "The difference between 3 times a number and 7."',
  '3 * x - 7',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Translate: "The quotient of a number and 4, increased by 2."',
  'x / 4 + 2',
  'strategic'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Why is it important to understand key phrases like "sum," "difference," or "product" when writing expressions?',
  'Because each phrase signals a specific mathematical operation, which ensures correct translation of verbal language into algebra.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  'Explain why "less than" reverses the order of subtraction in expressions.',
  'Because in phrases like "5 less than x", the amount is being taken from x, not the other way around. So it translates to x - 5.',
  'rational'
);

-- Write Expressions from verbal - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'What is a multi-step expression?',
  'An expression that involves more than one mathematical operation or transformation.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'What does it mean to translate a verbal scenario into an expression?',
  'It means converting written language that describes a mathematical situation into an algebraic expression.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'Translate: "6 more than the product of 2 and a number n."',
  '2 * n + 6',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'Translate: "The sum of a number x and 3, then divide the result by 2."',
  '(x + 3) / 2',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'Write an expression for: "A number is doubled, then 3 is subtracted from the result. That total is then divided by 5."',
  '(2 * x - 3) / 5',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'Translate the following: "Add 4 to the square of a number y, then multiply the result by 3, and subtract 7."',
  '3 * (y ^ 2 + 4) - 7',
  'strategic'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'Why is it important to preserve the order of operations when translating a multi-step verbal expression?',
  'To ensure the expression matches the intended calculation described in the scenario. The wrong order can completely change the result.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal'),
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  'A student writes "3 + x * 2" for the phrase "triple the sum of a number and two." What is wrong with this expression?',
  'The student multiplied x by 2 instead of adding 2 to x first. The correct expression is 3 * (x + 2).',
  'rational'
);

-- ===========================================================
-- 1.9 Intro Equations
-- ===========================================================
-- Evaluate Equations - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Evaluating Equations'),
    (SELECT id FROM LearningObjective WHERE title = 'Evaluating Equations - Objective 1'),
    'What is an equation?',
    'An equation is a mathematical statement that asserts the equality of two expressions.',
    'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Evaluating Equations'),
    (SELECT id FROM LearningObjective WHERE title = 'Evaluating Equations - Objective 1'),
    'Which of the following is an equation?' || CHAR(10) ||
    'A) 3x + 2' || CHAR(10) ||
    'B) x - 5 = 10' || CHAR(10) ||
    'C) 4y + 3' || CHAR(10) ||
    'D) z / 2',
    'B x - 5 = 10',
    'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Evaluating Equations'),
    (SELECT id FROM LearningObjective WHERE title = 'Evaluating Equations - Objective 1'),
    'Evaluate the equation x + 3 = 11 for x.',
    'x = 8',
    'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  'Solve the equation: x / 2 = 12',
  'x = 6',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  'You are told that 3 more than a number is equal to 11. Write and solve the equation.',
  'x + 3 = 11; x = 8',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  'A number divided by 4 is equal to 6. Write and solve the equation.',
  'x / 4 = 6; x = 24',
  'strategic'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  'Why do we perform inverse operations when solving equations?',
  'To isolate the variable and keep the equation balanced while undoing the original operations.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  'Why is checking your solution important after solving an equation?',
  'To confirm that your solution makes the original equation true.',
  'rational'
);

-- Evaluate Equations - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'What is a multi-step equation?',
  'An equation that requires two or more inverse operations to isolate the variable.',
  'factual'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'What operation should you undo first when solving 2x + 5 = 15?',
  'Subtract 5 first, then divide by 2.',
  'factual'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'Solve: 4x - 2 = 10',
  'x = 3',
  'procedural'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'Solve: 3x = x + 10',
  'x = 5',
  'procedural'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'Solve: 3(x - 2) + 4 = 19',
  'x = 5',
  'strategic'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'Solve: 3x - 2 = x + 10',
  'x = 6',
  'procedural'
);

-- Rational
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'Why is it useful to simplify both sides of an equation before solving?',
  'It reduces complexity, prevents mistakes, and helps isolate the variable more easily.',
  'rational'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Intro to Equations'),
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  'A student solved 3x + 2 = 11 by dividing 11 by 3 first. What went wrong?',
  'They skipped the subtraction step. Inverse operations must be done in reverse order.',
  'rational'
);

- ===========================================================
-- 1.10 Patterns, Equations, and Graphs
-- ===========================================================

-- *** We are going to hold off on goals that involve visual representation (graghs) ***





