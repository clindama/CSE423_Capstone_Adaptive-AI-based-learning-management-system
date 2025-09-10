-- Factual Knowledge
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Concept Recap', 'Reinforces core facts, definitions, and terminology.', 'factual', 'fact');

-- Procedural Knowledge
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Focused on an individual step or procedure', 'Guides students through how to solve problems by looking at it in parts.', 'procedural', 'procedure');

-- Strategic Knowledge
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Focused on linking multiple procedures as a whole', 'Teaches strategic thinking for choosing efficient problem-solving approaches.', 'strategic', 'strategy');

-- Rational Knowledge   
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Concept Rationale', 'Explains the reasoning and logic behind the concept.', 'rational', 'rationale');

-- General Knowledge
INSERT INTO InstructionMethod (name, description, method_type, method_keyword)
VALUES 
('Advanced Dive', 'Provides a comprehensive and structured overview of the concept.', 'general', 'overview');