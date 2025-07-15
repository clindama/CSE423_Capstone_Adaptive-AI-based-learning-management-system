-- Topic 1: Foundations for Algebra
INSERT INTO Topic (id, name, description, topic_order)
VALUES (1, 'Foundations for Algebra', 'Learn the fundamentals of algebra.', 1);

-- Goal 1.1: Expressions
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (1, 1, 'Expressions', 'Learn what are Expressions', 1);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(1, 'Expressions - Objective 1', 'Understand what expressions are and how to manipulate them.', 1),
(1, 'Expressions - Objective 2', 'Translate word problems into algebraic expressions.', 2);

-- Goal 1.2: Combine Like Terms
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (2, 1, 'Combine Like Terms', 'Learn to simplify expressions by combining like terms.', 2);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(2, 'Combine Like Terms - Objective 1', 'Identify and group like terms in algebraic expressions.', 1),
(2, 'Combine Like Terms - Objective 2', 'Understand how to simplify expressions.', 2);

-- Goal 1.3: Properties of Real Numbers
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (3, 1, 'Properties of Real Numbers', 'Understand the properties of real numbers.', 3);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(3, 'Properties - Objective 1', 'Recognize associative, commutative, and distributive properties.', 1),
(3, 'Properties - Objective 2', 'Apply properties to simplify algebraic expressions.', 2);

-- Goal 1.4: Exponents and Order of Operations
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (4, 1, 'Exponents and Order of Operations', 'Apply exponent rules and follow the correct order of operations.', 4);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(4, 'Exponents - Objective 1', 'Use PEMDAS to evaluate expressions correctly.', 1),
(4, 'Exponents - Objective 2', 'Apply multiplication and power rules with exponents.', 2);

-- Goal 1.5: Absolute Value
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (5, 1, 'Absolute Value', 'Understand and evaluate absolute value expressions.', 5);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(5, 'Absolute Value - Objective 1', 'Define absolute value and relate it to distance from zero.', 1),
(5, 'Absolute Value - Objective 2', 'Solve simple absolute value expressions and equations.', 2);

-- Goal 1.6: Simplify Expressions
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (6, 1, 'Simplify Expressions', 'Simplify numeric and algebraic expressions using properties and operations.', 6);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(6, 'Simplify - Objective 1', 'Combine like terms and apply properties to simplify expressions.', 1),
(6, 'Simplify - Objective 2', 'Identify unnecessary steps and streamline solutions.', 2);

-- Goal 1.7: Evaluate Expressions
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (7, 1, 'Evaluate Expressions', 'Substitute values into algebraic expressions and simplify.', 7);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(7, 'Evaluate - Objective 1', 'Substitute numerical values into algebraic expressions.', 1),
(7, 'Evaluate - Objective 2', 'Use order of operations to evaluate accurately.', 2);

-- Goal 1.8: Write Expressions from Verbal
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (8, 1, 'Write Expressions from Verbal', 'Translate real-world and mathematical verbal phrases into expressions.', 8);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(8, 'Verbal - Objective 1', 'Identify key terms and translate them into algebraic symbols.', 1),
(8, 'Verbal - Objective 2', 'Construct expressions from multi-step verbal scenarios.', 2);

-- Goal 1.9: Intro to Equations
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (9, 1, 'Intro to Equations', 'Understand what equations are and how to work with them.', 9);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(9, 'Equations - Objective 1', 'Define an equation and identify parts like variables and constants.', 1),
(9, 'Equations - Objective 2', 'Differentiate between expressions and equations.', 2);

-- Goal 1.10: Patterns, Equations, and Graphs
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (10, 1, 'Patterns, Equations, and Graphs', 'Explore relationships between patterns, equations, and graphs.', 10);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(10, 'Patterns - Objective 1', 'Recognize patterns in data and relate them to equations.', 1),
(10, 'Patterns - Objective 2', 'Interpret graphs that represent real-world equations.', 2);

-- Topic 2: Equations
INSERT INTO Topic (id, name, description, topic_order)
VALUES (1, 'Equations', 'Learn about equations and their properties.', 1);

-- Goal 2.1: Solving One-Step Equations
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (1, 2, 'Solving One-Step Equations', 'Learn to solve one-step equations using inverse operations.', 1);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(1, 'One-Step - Objective 1', 'Identify one-step equations and their components.', 1),
(1, 'One-Step - Objective 2', 'Apply inverse operations to solve one-step equations.', 2);

-- Goal 2.2: Solving Two-Step Equations
INSERT INTO Goal (id, topic_id, title, description, goal_order)
VALUES (2, 2, 'Solving Two-Step Equations', 'Learn to solve two-step equations using inverse operations.', 2);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(2, 'Two-Step - Objective 1', 'Identify two-step equations and their components.', 1),
(2, 'Two-Step - Objective 2', 'Apply inverse operations to solve two-step equations.', 2);