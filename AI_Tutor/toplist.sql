-- Topic 1: Foundations for Algebra
INSERT INTO Topic (name, description, topic_order)
VALUES ('Foundations for Algebra', 'Learn the fundamentals of algebra.', 1);

-- Goal 1.1: Expressions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Expressions',
    'Learn what are Expressions', 
    1
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Expressions - Objective 1',
    'Understand what expressions are and how to manipulate them.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Expressions - Objective 2',
    'Translate word problems into algebraic expressions.',
    2
);

-- Goal 1.2: Combine Like Terms
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'), 
    'Combine Like Terms',
    'Learn to simplify expressions by combining like terms.',
    2
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Combine Like Terms - Objective 1',
    'Identify and group like terms in algebraic expressions.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Combine Like Terms' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Combine Like Terms - Objective 2',
    'Understand how to simplify expressions.',
    2
);

-- Goal 1.3: Properties of Real Numbers
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Properties of Real Numbers',
    'Understand the properties of real numbers.',
    3
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Properties of Real Numbers - Objective 1',
    'Recognize associative, commutative, and distributive properties.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Properties of Real Numbers' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Properties of Real Numbers - Objective 2',
    'Apply properties to simplify algebraic expressions.',
    2
);

-- Goal 1.4: Exponents and Order of Operations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Exponents and Order of Operations',
    'Apply exponent rules and follow the correct order of operations.',
    4
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Exponents - Objective 1',
    'Use PEMDAS to evaluate expressions correctly.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Exponents and Order of Operations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Exponents - Objective 2',
    'Apply multiplication and power rules with exponents.',
    2
);

-- Goal 1.5: Absolute Value
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Absolute Value',
    'Understand and evaluate absolute value expressions.',
    5
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Absolute Value' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Absolute Value - Objective 1',
    'Define absolute value and relate it to distance from zero.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Absolute Value' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Absolute Value - Objective 2',
    'Solve simple absolute value expressions and equations.',
    2
);

-- Goal 1.6: Simplify Expressions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Simplify Expressions',
    'Simplify numeric and algebraic expressions using properties and operations.',
    6
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Simplify Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Simplify - Objective 1',
    'Combine like terms and apply properties to simplify expressions.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Simplify Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Simplify - Objective 2',
    'Identify unnecessary steps and streamline solutions.',
    2
);

-- Goal 1.7: Evaluate Expressions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Evaluate Expressions',
    'Substitute values into algebraic expressions and simplify.',
    7
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Evaluate Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Evaluate - Objective 1',
    'Substitute numerical values into algebraic expressions.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Evaluate Expressions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Evaluate - Objective 2',
    'Use order of operations to evaluate accurately.',
    2
    );

-- Goal 1.8: Write Expressions from Verbal
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Write Expressions from Verbal',
    'Translate real-world and mathematical verbal phrases into expressions.',
    8
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Verbal - Objective 1',
    'Identify key terms and translate them into algebraic symbols.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write Expressions from Verbal' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Verbal - Objective 2',
    'Construct expressions from multi-step verbal scenarios.',
    2
);

-- Goal 1.9: Intro to Equations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Intro to Equations',
    'Understand what equations are and how to work with them.',
    9
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Intro to Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Equations - Objective 1',
    'Define an equation and identify parts like variables and constants.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Intro to Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Equations - Objective 2',
    'Differentiate between expressions and equations.',
    2
);

-- Goal 1.10: Patterns, Equations, and Graphs
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Foundations for Algebra'),
    'Patterns, Equations, and Graphs',
    'Explore relationships between patterns, equations, and graphs.',
    10
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Patterns, Equations, and Graphs' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Patterns - Objective 1',
    'Recognize patterns in data and relate them to equations.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Patterns, Equations, and Graphs' AND topic_id = (SELECT id FROM Topic WHERE name = 'Foundations for Algebra')),
    'Patterns - Objective 2',
    'Interpret graphs that represent real-world equations.',
    2
);

-- Topic 2: Equations
INSERT INTO Topic (name, description, topic_order)
VALUES ('Equations', 'Learn about equations and their properties.', 1);

-- Goal 2.1: Solving One-Step Equations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solving One-Step Equations',
    'Learn to solve one-step equations using inverse operations.',
    1
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solving One-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solving One-Step Equations - Objective 1',
    'Identify one-step equations and their components.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solving One-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solving One-Step Equations - Objective 2',
    'Recognize common mistakes in solving one-step equations.',
    2
);

-- Goal 2.2: Solving Two-Step Equations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solving Two-Step Equations',
    'Learn to solve two-step equations using inverse operations.',
    2
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solving Two-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solving Two-Step Equations - Objective 1',
    'Identify two-step equations and their components.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solving Two-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solving Two-Step Equations - Objective 2',
    'Apply inverse operations to solve two-step equations.',
    2
);

-- Goal 2.3: Solving Multi-Step Equations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solving Multi-Step Equations',
    'Learn to solve multi-step equations using inverse operations.',
    3
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solving Multi-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Multi-Step - Objective 1',
    'Identify multi-step equations and their components.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solving Multi-Step Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Multi-Step - Objective 2',
    'Apply inverse operations to solve multi-step equations.',
    2
);

-- Goal 2.4: Solving Equations with Variables on Both Sides
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solving Equations with Variables on Both Sides',
    'Learn to solve equations with variables on both sides using inverse operations.',
    4
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solving Equations with Variables on Both Sides' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Variables on Both Sides - Objective 1',
    'Identify equations with variables on both sides.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solving Equations with Variables on Both Sides' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Variables on Both Sides - Objective 2',
    'Apply inverse operations to solve equations with variables on both sides.',
    2
);

-- Goal 2.5: Literal Equations and Formulas
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Literal Equations and Formulas',
    'Learn to manipulate literal equations and formulas.',
    5
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Literal Equations and Formulas' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Literal Equations - Objective 1',
    'Identify literal equations and their components.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Literal Equations and Formulas' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Literal Equations - Objective 2',
    'Apply inverse operations to solve literal equations.',
    2
);

-- Goal 2.6: Solve Word Problems with 1 Unknown
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solve Word Problems with 1 Unknown',
    'Learn to translate word problems into equations and solve for one unknown.',
    6
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 1 Unknown' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems - Objective 1',
    'Identify key information in word problems.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 1 Unknown' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems - Objective 2',
    'Translate word problems into equations.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 1 Unknown' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems - Objective 3',
    'Solve equations derived from word problems.',
    3
);

-- Goal 2.7: Solve Word Problems with 2 or more Unknowns
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solve Word Problems with 2 or more Unknowns',
    'Learn to translate word problems into equations and solve for two or more unknowns.',
    7
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 2 or more Unknowns' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems with 2 Unknowns - Objective 1',
    'Identify key information in word problems with multiple unknowns.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 2 or more Unknowns' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems with 2 Unknowns - Objective 2',
    'Translate word problems into systems of equations.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Word Problems with 2 or more Unknowns' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Word Problems with 2 Unknowns - Objective 3',
    'Solve systems of equations derived from word problems.',
    3
);

-- Goal 2.8: Absolute Value equations/Inequalities
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Absolute Value Equations and Inequalities',
    'Learn to solve absolute value equations and inequalities.',
    8
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Absolute Value Equations and Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Absolute Value - Objective 1',
    'Identify absolute value equations and inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Absolute Value Equations and Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Absolute Value - Objective 2',
    'Solve absolute value equations.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Absolute Value Equations and Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Absolute Value - Objective 3',
    'Graph absolute value inequalities.',
    3
);

-- Goal 2.9: Ratios and Proportions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Ratios and Proportions',
    'Learn to solve problems involving ratios and proportions.',
    9
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Ratios and Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Ratios - Objective 1',
    'Identify and create ratios from given information.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Ratios and Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Ratios - Objective 2',
    'Solve problems involving equivalent ratios.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Ratios and Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Proportions - Objective 2',
    'Solve problems involving proportions.',
    3
);

-- Goal 2.10: Solve Proportions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Solve Proportions',
    'Learn to solve proportions using cross-multiplication and other methods.',
    10
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Solve Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solve Proportions - Objective 1',
    'Identify and set up proportions from given information.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solve Proportions - Objective 2',
    'Use cross-multiplication to solve proportions.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Proportions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Solve Proportions - Objective 3',
    'Apply proportions to real-world problems.',
    3
);

-- Goal 2.11: Percent
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Percent',
    'Learn to calculate and apply percentages in various contexts.',
    11
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Percent' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent - Objective 1',
    'Understand the concept of percent.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Percent' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent - Objective 2',
    'Calculate percentages of given quantities.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Percent' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent - Objective 3',
    'Apply percent concepts to real-world problems.',
    3
);

-- Goal 2.12: Percent Change
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Equations'),
    'Percent Change',
    'Learn to calculate and apply percent change in various contexts.',
    12
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Percent Change' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent Change - Objective 1',
    'Understand the concept of percent change.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Percent Change' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent Change - Objective 2',
    'Calculate percent change for given values.',
    2
),
(
    (SELECT id FROM Goal WHERE title = 'Percent Change' AND topic_id = (SELECT id FROM Topic WHERE name = 'Equations')),
    'Percent Change - Objective 3',
    'Apply percent change concepts to real-world problems.',
    3
);

-- Topic 3: Inequalities
INSERT INTO Topic (name, description, topic_order)
VALUES ('Inequalities', 'Explore the world of inequalities, their properties, and how to solve them.', 3);

-- Goal 3.1: Properties of Sets
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Properties of Sets',
    'Learn the properties of sets and how to work with them.',
    1
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Properties of Sets' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Properties of Sets - Objective 1',
    'Understand the basic properties of sets.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Properties of Sets' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Properties of Sets - Objective 2',
    'How to apply set properties in problem-solving.',
    2
);

-- Goal 3.2: Write and Graph Inequalities
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Write and Graph Inequalities',
    'Learn to write and graph inequalities on a number line.',
    2
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write and Graph Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Write and Graph Inequalities - Objective 1',
    'Understanding inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Write and Graph Inequalities - Objective 2',
    'Graph inequalities on a number line.',
    2
);

-- Goal 3.3: Solve Inequalities using Addition and Subtraction
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Solve Inequalities using Addition and Subtraction',
    'Learn to solve inequalities using addition and subtraction.',
    3
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Solve Inequalities using Addition and Subtraction' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Inequalities - Objective 1',
    'Use addition to solve inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Inequalities using Addition and Subtraction' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Inequalities - Objective 2',
    'Use subtraction to solve inequalities.',
    2
);

-- Goal 3.4: Solve Inequalities using Multiplication and Division
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Solve Inequalities using Multiplication and Division',
    'Learn to solve inequalities using multiplication and division.',
    4
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Solve Inequalities using Multiplication and Division' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Inequalities - Objective 1',
    'Use multiplication to solve inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Inequalities using Multiplication and Division' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Inequalities - Objective 2',
    'Use division to solve inequalities.',
    2
);

-- Goal 3.5: Solve Multi-Step Inequalities
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Solve Multi-Step Inequalities',
    'Learn to solve multi-step inequalities.',
    5
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Solve Multi-Step Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Multi-Step Inequalities - Objective 1',
    'Understand the process of solving multi-step inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Solve Multi-Step Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Solve Multi-Step Inequalities - Objective 2',
    'Apply appropriate strategies to solve multi-step inequalities.',
    2
);

-- Goal 3.6: Union and Intersection of Sets
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Union and Intersection of Sets',
    'Learn to find the union and intersection of sets.',
    6
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Union and Intersection of Sets' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Union of Sets - Objective 1',
    'Understand the concept of union of sets.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Union and Intersection of Sets' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Intersection of Sets - Objective 1',
    'Understand the concept of intersection of sets.',
    2
);

-- Goal 3.7: Compound Inequalities
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Inequalities'),
    'Compound Inequalities',
    'Learn to solve compound inequalities.',
    7
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Compound Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Compound Inequalities - Objective 1',
    'Understand the concept of compound inequalities.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Compound Inequalities' AND topic_id = (SELECT id FROM Topic WHERE name = 'Inequalities')),
    'Compound Inequalities - Objective 2',
    'Solve compound inequalities using various methods.',
    2
);

-- Topic 4: Functions and Linear Equations
INSERT INTO Topic (name, description, topic_order)
VALUES ('Functions and Linear Equations', 'Explore the concepts of functions and linear equations.', 4);

-- Goal 4.1: Coordinate Plane
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Coordinate Plane',
    'Learn about the coordinate plane and how to plot points.',
    1
);
INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Coordinate Plane' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Coordinate Plane - Objective 1',
    'Understand the concept of the coordinate plane.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Coordinate Plane' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Coordinate Plane - Objective 2',
    'Plot points on the coordinate plane.',
    2
);

-- Goal 4.2: Identify relations and functions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Identify Relations and Functions',
    'Learn to identify and represent relations and functions.',
    2
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Identify Relations and Functions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Identify Relations - Objective 1',
    'Understand the concept of relations.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Identify Relations and Functions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Identify Functions - Objective 1',
    'Understand the concept of functions.',
    2
);

-- Goal 4.3: Function Notation
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Function Notation',
    'Learn about function notation and how to use it.',
    3
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Function Notation' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Function Notation - Objective 1',
    'Understand the concept of function notation.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Function Notation' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Function Notation - Objective 2',
    'Use function notation to represent functions.',
    2
);

-- Goal 4.4: Write and Graph function rules
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write and Graph Function Rules',
    'Learn to write and graph function rules.',
    4
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write and Graph Function Rules' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Function Rules - Objective 1',
    'Understand how to write function rules.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Function Rules' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Function Rules - Objective 1',
    'Learn to graph function rules.',
    2
);

-- Goal 4.5: Direct Variation
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Direct Variation',
    'Learn about direct variation and how to identify it.',
    5
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Direct Variation' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Direct Variation - Objective 1',
    'Understand the concept of direct variation.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Direct Variation' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Direct Variation - Objective 2',
    'Identify direct variation in real-world scenarios.',
    2
);

-- Goal 4.6: Slope
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Slope',
    'Learn about slope and how to calculate it.',
    6
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Slope' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Slope - Objective 1',
    'Understand the concept of slope.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Slope' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Slope - Objective 2',
    'Calculate the slope of a line given two points.',
    2
);

-- Goal 4.7: Write and Graph Equations in Slope-Intercept Form
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write and Graph Equations in Slope-Intercept Form',
    'Learn to write and graph equations in slope-intercept form.',
    7
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Slope-Intercept Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Equations - Objective 1',
    'Understand how to write equations in slope-intercept form.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Slope-Intercept Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Equations - Objective 1',
    'Learn to graph equations in slope-intercept form.',
    2
);

-- Goal 4.8: Write and Graph Equations in Point-Slope Form
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write and Graph Equations in Point-Slope Form',
    'Learn to write and graph equations in point-slope form.',
    8
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Point-Slope Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Equations - Objective 1',
    'Understand how to write equations in point-slope form.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Point-Slope Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Equations - Objective 1',
    'Learn to graph equations in point-slope form.',
    2
);

-- Goal 4.9: Write and Graph Equations in Standard Form
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write and Graph Equations in Standard Form',
    'Learn to write and graph equations in standard form.',
    9
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Standard Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Equations - Objective 1',
    'Understand how to write equations in standard form.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Equations in Standard Form' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Equations - Objective 1',
    'Learn to graph equations in standard form.',
    2
);

-- Goal 4.10: Write Equations of Parallel lines
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write Equations of Parallel Lines',
    'Learn to write equations of parallel lines.',
    10
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES 
(
    (SELECT id FROM Goal WHERE title = 'Write Equations of Parallel Lines' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Equations - Objective 1',
    'Understand how to write equations of parallel lines.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write Equations of Parallel Lines' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Equations - Objective 1',
    'Learn to graph equations of parallel lines.',
    2
);

-- Goal 4.11: Write Equations of Perpendicular lines
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write Equations of Perpendicular Lines',
    'Learn to write equations of perpendicular lines.',
    11
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write Equations of Perpendicular Lines' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Equations - Objective 1',
    'Understand how to write equations of perpendicular lines.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write Equations of Perpendicular Lines' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Equations - Objective 1',
    'Learn to graph equations of perpendicular lines.',
    2
);

-- Goal 4.12: Write and Graph Absolute Value Functions
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write and Graph Absolute Value Functions',
    'Learn to write and graph absolute value functions.',
    12
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write and Graph Absolute Value Functions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Absolute Value Functions - Objective 1',
    'Understand how to write absolute value functions.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write and Graph Absolute Value Functions' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Absolute Value Functions - Objective 1',
    'Learn to graph absolute value functions.',
    2
);

-- Goal 4.13: Write Inverse Function equations
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Write Inverse Function Equations',
    'Learn to write inverse function equations.',
    13
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Write Inverse Function Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Write Inverse Functions - Objective 1',
    'Understand how to write inverse functions.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Write Inverse Function Equations' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Graph Inverse Functions - Objective 1',
    'Learn to graph inverse functions.',
    2
);

-- Goal 4.14: Arithmetic Sequences
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Arithmetic Sequences',
    'Learn about arithmetic sequences and how to find their terms.',
    14
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Arithmetic Sequences' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Arithmetic Sequences - Objective 1',
    'Understand the concept of arithmetic sequences.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Arithmetic Sequences' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Arithmetic Sequences - Objective 2',
    'Find the nth term of an arithmetic sequence.',
    2
);

-- Goal 4.15: Scatter Plots and Line of Best Fit
INSERT INTO Goal (topic_id, title, description, goal_order)
VALUES (
    (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations'),
    'Scatter Plots and Line of Best Fit',
    'Learn to create scatter plots and find the line of best fit.',
    15
);

INSERT INTO LearningObjective (goal_id, title, description, obj_order)
VALUES (
    (SELECT id FROM Goal WHERE title = 'Scatter Plots and Line of Best Fit' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Scatter Plots - Objective 1',
    'Understand how to create scatter plots.',
    1
),
(
    (SELECT id FROM Goal WHERE title = 'Scatter Plots and Line of Best Fit' AND topic_id = (SELECT id FROM Topic WHERE name = 'Functions and Linear Equations')),
    'Line of Best Fit - Objective 1',
    'Learn to find the line of best fit for a scatter plot.',
    2
);

-- Topic 5: Systems of Equations and Inequalities