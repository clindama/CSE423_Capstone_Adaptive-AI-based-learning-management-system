-- General Explanations
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Explain Concept', 'Structured explanation in neutral vocabulary.', 'general', 'explanation'),
('Simplified Terms', 'Breaks concept into simpler language for beginners.', 'general', 'simplified'),
('Advanced Dive', 'Explains using higher-level vocabulary.', 'general', 'advanced');

-- Interactive
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Ask & Guide', 'Teach step by step while waiting for student input to proceed.', 'interactive', 'guide'),
('Interactive Quiz', 'Engages with questions that require active participation.', 'interactive', 'quiz');

-- Reinforcement
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Use Analogies', 'Teaches with metaphors and real-world comparisons.', 'reinforcement', 'analogy'),
('Step-by-Step Examples', 'Solves problems while explaining each step.', 'reinforcement', 'example'),
('Flashcard Review', 'Quick-hit facts to reinforce what was learned.', 'reinforcement', 'review');