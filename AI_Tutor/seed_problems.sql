-- ===========================================================
-- 1.1 Expressions
-- ===========================================================

-- Expressions - Objective 1
-- Factual Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'What is an algebraic expression?',
    'An algebraic expression is a mathematical phrase that can contain numbers, variables, and operation symbols.',
    'factual',
    'definition, expressions'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Which of the following is NOT an algebraic expression: A) 2x + 3, B) 7, C) = 4x - 1, D) x^2 - 5?',
    'C) = 4x - 1',
    'factual',
    'recognition, expressions'
);

-- Procedural Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Combine the like terms: 3x + 5 + 2x.',
    '5x + 5',
    'procedural',
    'simplify, combine like terms'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Rewrite the expression 4(x + 2) using the distributive property.',
    '4x + 8',
    'procedural',
    'distributive, expanding'
);

-- Strategic Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Simplify the expression 6(x - 2) + 3x.',
    '9x - 12',
    'strategic',
    'strategy, order of operations'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Simplify 3(x + 3) + 4x - 1?',
    '7x + 8',
    'strategic',
    'simplify, strategy'
);

-- Rational Problems
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Why can we combine the terms 2x and 5x, but not 2x and 3y?',
    'Because 2x and 5x are like terms (same variable), while 2x and 3y are not.',
    'rational',
    'reasoning, like terms'
),
(
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Expressions'),
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    'Explain why simplifying expressions is important before solving equations.',
    'It makes equations easier to solve and reduces the chance of mistakes.',
    'rational',
    'reasoning, simplify'
);

-- Expressions - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'What is an algebraic expression?',
  'A mathematical phrase that includes numbers, variables, and operations but no equals sign.',
  'factual',
  'definition, expressions'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'In the expression 5x + 7, what does the variable represent in a real-world context?',
  'It represents an unknown quantity that can change based on the situation.',
  'factual',
  'variable, real-world, definition'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Translate the sentence into an expression:' || CHAR(10) ||
  '"Seven more than twice a number."',
  '2x + 7',
  'procedural',
  'translation, word problems, syntax'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Write an algebraic expression for the phrase:' || CHAR(10) ||
  '"The product of a number and 4 decreased by 9."',
  '4x - 9',
  'procedural',
  'translation, expression building, operations'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'A taxi company charges $3 for pickup and $2 per mile. Write an expression for the cost of a ride that is m miles long.' || CHAR(10) ||
  'Explain your reasoning.',
  '3 + 2m || Fixed cost is $3, variable cost is $2 per mile.',
  'strategic',
  'real-world modeling, word problems, expression building'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Write an expression to represent the cost of x movie tickets if each ticket costs $12, and you also buy a snack combo for $5.' || CHAR(10) ||
  'Show the full expression and explain what each part represents.',
  '12x + 5 || 12x for tickets, 5 for the combo.',
  'strategic',
  'real-world scenario, expression structure, modeling'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'Why is it helpful to convert word problems into algebraic expressions?',
  'It allows us to use mathematical reasoning to solve real-world problems and make generalizations.',
  'rational',
  'reasoning, problem translation, abstraction'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Expressions'),
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  'How does identifying keywords (like "sum" or "product") help in writing algebraic expressions?',
  'They signal the mathematical operation needed, guiding how to build the expression correctly.',
  'rational',
  'keywords, abstraction, reasoning'
);

-- ===========================================================
-- 1.2 Combining Like Terms
-- ===========================================================
-- Combining Like Terms - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
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
    'factual',
    'like terms, variables'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
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
    'factual',
    'definition, like terms'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Identify and group the like terms in the expression:' || CHAR(10) ||
    '7x + 3y - 2x + 5y',
    '7x and -2x || 3y and 5y',
    'procedural',
    'grouping, like terms'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Group the like terms from the expression below:' || CHAR(10) ||
    '8a + 2b + 3a - b + 4',
    '8a and 3a || 2b and -b',
    'procedural',
    'grouping, simplification'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'You are given the expression: 4x + 2y - 3x + y - 6.' || CHAR(10) ||
    'Simplify it.',
    'x + 3y - 6',
    'strategic',
    'simplification, process'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'You need to simplify this expression for a final answer:' || CHAR(10) ||
    '6m - 4 + 2m - 3m + 10.',
    '4m + 6',
    'strategic',
    'simplify, combining like terms'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Why can''t you combine 4x and 5y when simplifying an expression?',
    'They are not like terms because they have different variables.',
    'rational',
    'reasoning, variable rules'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    'Why is it important to identify like terms before combining them?',
    'Because combining unlike terms leads to incorrect simplification and violates algebraic rules.',
    'rational',
    'reasoning, simplification rules'
);

-- Combining Like Terms - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'What does it mean to simplify an algebraic expression?',
  'To combine like terms and rewrite the expression in its simplest form.',
  'factual',
  'definition, simplification, expressions'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Which terms can be combined in the expression 3x + 5 + 7x - 2?',
  '3x and 7x; 5 and -2 are constants but can be combined as well.',
  'factual',
  'like terms, identification, simplification'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Identify like terms in the expression: 4a + 3b - 2a + 7b.',
  '4a and -2a; 3b and 7b. 2)',
  'simplification, combining like terms'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Identify like terms in the expression 6x - 4 + 2x + 9?',
  '6x and 2x; -4 and 9.',
  'simplification, combining like terms'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Given the expression 5m + 3n - 2m + 7, simplify it.',
  '3m + 3n + 7.',
  'strategic',
  'simplification, grouping'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Simplify an expression with multiple variables and constants, like 2x + 3y - x + 5 - 2y + 7?',
  'x + y + 12.',
  'strategic',
  'complex expressions, grouping, approach'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'Why do we combine like terms when simplifying expressions?',
  'To reduce the expression to its simplest form, making it easier to understand and solve.',
  'rational',
  'reasoning, simplification, clarity'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Combine Like Terms'),
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  'How does combining like terms help in solving equations?',
  'It simplifies the equation, reducing the number of terms, and makes it easier to isolate variables.',
  'rational',
  'reasoning, problem solving, simplification'
);

-- ===========================================================
-- 1.3 Properties of Real Numbers
-- ===========================================================
-- Properties of Real Numbers - Objective 1
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Which property is illustrated by the equation below?' || CHAR(10) ||
    '(2 + 3) + 4 = 2 + (3 + 4)',
    'Associative Property of Addition',
    'factual',
    'associative, definition'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Which property allows you to write:' || CHAR(10) ||
    '6 * 3 = 3 * 6',
    'Commutative Property of Multiplication',
    'factual',
    'commutative, multiplication'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Apply the distributive property to rewrite:' || CHAR(10) ||
    '5(2 + x)',
    '10 + 5x',
    'procedural',
    'distributive, expression'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Use the associative property to rewrite this expression without changing its value:' || CHAR(10) ||
    '(7 * 2) * 5',
    '7 * (2 * 5)',
    'procedural',
    'associative, parentheses'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'You are given an expression: 3(x + 4) + 2x.' || CHAR(10) ||
    'Simplify it using the distributive and addition properties.',
    '5x + 12',
    'strategic',
    'distributive, simplify, multi-step'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
    'You want to simplify: (x + 2) + (3x + 5).',
    '4x + 7',
    'strategic',
    'associative, commutative, expression strategy'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Why is it valid to switch the order in 7 + 2 = 2 + 7?',
    'Because the commutative property of addition states that changing the order does not change the sum.',
    'rational',
    'commutative, reasoning'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    'Why does the distributive property matter when simplifying expressions like 4(x + 2)?',
    'It allows multiplication to apply across addition, breaking expressions into manageable parts.',
    'rational',
    'distributive, simplification, justification'
);

-- Properties of Real Numbers - Objective 2
-- Factual
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'What is the associative property in algebra?',
  'The associative property states that (a + b) + c = a + (b + c).',
  'factual',
  'associative property, definition'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Name two properties of real numbers used to simplify expressions.',
  'Commutative property and associative property.',
  'factual',
  'properties, real numbers, definition'
);

-- Procedural
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Simplify 3(x + 4) using the distributive property.',
  '3x + 12.',
  'procedural',
  'distributive property, simplification, steps'
);

-- ================= Good for testing multiple answer formats =================
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Use the associative property to simplify the expression (2+ 7x) + 3x.',
  '(7x + 3x) = 2 + 10x = 10x + 2',
  'procedural',
  'associative property, simplification, grouping'
);

-- Strategic
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'When simplifying expressions, how do you decide when to apply the distributive property versus combining like terms?',
  'Apply the distributive property first to remove parentheses, then combine like terms to simplify further.',
  'strategic',
  'simplification strategy, distributive property, combining like terms'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Simplify the expression 2(x + 3) + 4x.',
  '6x + 6.',
  'strategic',
  'simplification strategy, distributive property, combining like terms'
);

-- Rationale
INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Why is the distributive property important when simplifying algebraic expressions?',
  'It allows you to remove parentheses by distributing multiplication over addition or subtraction, simplifying calculations.',
  'rational',
  'distributive property, importance, reasoning'
);

INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category, tags)
VALUES (
  (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
  (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers'),
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  'Explain why combining like terms alone is not always sufficient to simplify expressions.',
  'Because expressions may have parentheses or multiplication needing the distributive property before combining like terms.',
  'rational',
  'simplification, reasoning, distributive property'
);

