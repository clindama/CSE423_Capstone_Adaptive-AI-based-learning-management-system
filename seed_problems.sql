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

