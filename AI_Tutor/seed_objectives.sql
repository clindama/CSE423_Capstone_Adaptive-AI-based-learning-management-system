
-- =========================================================================
-- Goal 1.1: Expressions
-- =========================================================================

-- *** Expressions - Objective 1 ***
-- General: Explanation
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'explanation'),
    'An expression in math is a combination of numbers, variables, and operations (like + or ×). Unlike equations, expressions don’t include an equals sign.'
);

-- General: Simplified
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'simplified'),
    'Think of expressions like math puzzles without an equals sign. They use numbers, letters (like x or y), and math symbols.'
);

-- General: Advanced
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'advanced'),
    'A mathematical expression is a finite combination of variables, constants, and operators that evaluates to a value under specific conditions. It lacks an equality relationship.'
);

-- Interactive: Guide
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'guide'),
    'Let’s build an expression together. Start with a number. Now add a variable to it. What do you get? Let’s continue...'
);

-- Interactive: Quiz
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'quiz'),
    'Which of the following is a valid expression?\nA) 5 + x\nB) x = 3\nC) 4x = 7\n(Answer: A)\nLet’s try another...'
);

-- Reinforcement: Analogy
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'analogy'),
    'An expression is like a recipe — it tells you what ingredients (numbers and variables) you need, but doesn’t say how much food you end up with.'
);

-- Reinforcement: Example
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Example: 3x + 2 is an expression. If x = 4, then 3x + 2 = 3(4) + 2 = 14.'
);

-- Reinforcement: Review
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'review'),
    'Expressions use numbers and variables\n No equals sign\n 5 + x is an expression\n x = 3 is an equation\nMore flashcards...'
);

-- *** Expressions - Objective 2 ***
-- General: Explanation
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'explanation'),
    'To translate a word problem into an expression, look for phrases that mean operations. For example, "five more than a number" becomes x + 5.'
);

-- General: Simplified
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'simplified'),
    'Change the words into math. If a sentence says "7 less than a number," just write the number minus 7: x - 7.'
);

-- General: Advanced
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'advanced'),
    'Translating verbal statements to algebra requires recognizing operation cues. "Triple a number decreased by 2" becomes 3x - 2, where x is the unknown.'
);

-- Interactive: Guide
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'guide'),
    'Let’s turn a sentence into an expression. The problem says "twice a number plus 3". First, identify the number. Let’s call it x...'
);

-- Interactive: Quiz
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'quiz'),
    'What is the expression for "6 more than a number"?\nA) x + 6\nB) 6x\nC) x - 6\n(Answer: A)\nHere’s another one...'
);

-- Reinforcement: Analogy
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'analogy'),
    'Think of word problems like a secret message. You’re decoding math terms hidden in words. "Half of a number" is like splitting a pizza — x/2.'
);

-- Reinforcement: Example
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Example: "The sum of a number and 8" becomes x + 8.\nAnother: "Four times a number minus 5" becomes 4x - 5.'
);

-- Reinforcement: Review
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'review'),
    'Word to Expression\n"Twice a number" → 2x\n"Three less than a number" → x - 3\n"Half a number" → x ÷ 2\nKeep practicing...'
);

