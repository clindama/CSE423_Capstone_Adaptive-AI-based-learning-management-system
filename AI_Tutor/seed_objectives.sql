
-- Content for Topics 1-3 (Only the first 2-3 Goals and their Objectives)
-- =========================================================================
-- Topic 1: Foundations for Algebra
-- =========================================================================

-- *** Goal 1.1 Expressions ***

-- Expressions - Objective 1: "Understand what expressions are and how to manipulate them."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Expressions are foundational in algebra and serve as the building blocks for more complex mathematical reasoning.' || CHAR(10) ||
    'They consist of numbers, variables, and operators arranged to represent relationships or quantities without using an equals sign.' || CHAR(10) ||
    'Expressions can range from a single term to combinations of many terms connected by addition or subtraction.' || CHAR(10) ||
    'Mastery of expressions enables students to simplify, transform, and interpret mathematical relationships.' || CHAR(10) ||
    'To manipulate expressions effectively, one must understand how terms interact, when terms are considered alike, and how properties of real numbers—such as the distributive property—can be applied to simplify expressions or reformat them for problem solving.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Expression**: A mathematical phrase composed of numbers, variables, and operators that does not include an equals sign.' || CHAR(10) ||
    '**Variable**: A symbol that represents an unknown or changeable quantity, usually written as a letter.' || CHAR(10) ||
    '**Constant**: A fixed numerical value that does not change.' || CHAR(10) ||
    '**Term**: A part of an expression; can be a number, a variable, or a combination of both.' || CHAR(10) ||
    '**Coefficient**: A number that multiplies a variable in a term.' || CHAR(10) ||
    '**Operator**: A symbol that denotes a mathematical operation, such as +, -, *, or /.' || CHAR(10) ||
    '**Like Terms**: Terms that have the same variable(s) raised to the same exponent(s), allowing them to be combined.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To manipulate expressions effectively, begin by identifying like terms—these are terms that share identical variables and exponents.' || CHAR(10) ||
    'Once identified, combine them by performing the operation indicated (usually addition or subtraction) on their coefficients.' || CHAR(10) ||
    'If the expression includes parentheses, apply the distributive property to remove them before combining terms.' || CHAR(10) ||
    'Each step in this process preserves the mathematical value of the original expression while simplifying its structure for easier interpretation.'
);

-- Strategic Knowlege
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
    'Solving complex expressions often involves linking multiple simplification strategies.' || CHAR(10) ||
    'Start by scanning the entire expression for parentheses and use the distributive property to eliminate them.' || CHAR(10) ||
    'Then, identify all like terms across the expanded expression and group them accordingly.' || CHAR(10) ||
    'After grouping, combine the coefficients of like terms through addition or subtraction.' || CHAR(10) ||
    'Throughout this process, keep track of negative signs and the correct order of operations.' || CHAR(10) ||
    'Finally, check whether further simplification is possible by re-evaluating the structure of the expression.' || CHAR(10) ||
    'Using this layered approach helps avoid mistakes and builds a habit of structured algebraic thinking.'
);

-- Rationale knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
    'Understanding how to manipulate expressions is essential because it allows us to reframe mathematical relationships in simpler or more usable forms.' || CHAR(10) ||
    'Simplified expressions are easier to evaluate, compare, or use within equations.' || CHAR(10) ||
    'Manipulating expressions isn''t just about getting a shorter form, it''s about clarity and preparation.' || CHAR(10) ||
    'For example, transforming an expression might reveal patterns or equivalences that are otherwise hidden.' || CHAR(10) ||
    'This skill also serves as a foundation for solving equations and inequalities, which involve identifying values that make expressions equal or satisfy conditions.' || CHAR(10) ||
    'Thus, mastering expression manipulation is both a practical tool and a conceptual stepping stone.'
);

-- *** Expressions - Objective 2 *** 

-- Expressions - Objective 2: "Apply properties of operations to simplify expressions."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Translating word problems into algebraic expressions is a critical skill that connects real-world scenarios to mathematical representation.' || CHAR(10) ||
  'This process involves identifying key quantities, relationships, and operations described in words and expressing them using variables, numbers, and arithmetic symbols.' || CHAR(10) ||
  'Understanding common verbal cues and phrases helps to map language to mathematical operations accurately.' || CHAR(10) ||
  'Once translated, these expressions provide a foundation for further problem solving, such as evaluating or solving equations.'
);

-- Factual Knowledge 
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
  '**Variable:** A letter or symbol representing an unknown quantity.' || CHAR(10) ||
  '**Coefficient:** A number multiplying a variable.' || CHAR(10) ||
  '**Constant:** A fixed number.' || CHAR(10) ||
  '**Key Words:** Terms in a problem that indicate operations, such as "sum" (addition), "difference" (subtraction), "product" (multiplication), and "quotient" (division).' || CHAR(10) ||
  '**Translate:** To convert verbal information into an algebraic expression using variables and operations.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
  'Begin translating a word problem by carefully reading the problem to identify important quantities.' || CHAR(10) ||
  'Next, determine which quantity will be represented by a variable.' || CHAR(10) ||
  'Identify the operations indicated by the problem''s wording.' || CHAR(10) ||
  'Assign appropriate arithmetic symbols to these operations.' || CHAR(10) ||
  'Construct an algebraic expression by arranging the variables and numbers with their corresponding operations in the correct order.'
);

-- Strategic knowlege
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When translating multi-step verbal scenarios into expressions, first break down the problem into smaller parts.' || CHAR(10) ||
  'Identify each quantity and its role in the overall relationship.' || CHAR(10) ||
  'Determine the sequence of operations implied by the problem.' || CHAR(10) ||
  'Translate each part individually using variables and operations, then combine these parts to form a complete expression.' || CHAR(10) ||
  'Check that the resulting expression accurately models the original verbal scenario and maintains the correct order of operations.'
);

-- Rational knowlege
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Translating word problems into algebraic expressions bridges the gap between language and mathematics.' || CHAR(10) ||
  'This skill enables students to see how everyday situations can be represented symbolically, allowing the use of algebra to analyze and solve problems.' || CHAR(10) ||
  'Developing this ability enhances critical thinking, as it requires understanding both the problem''s context and the mathematical operations needed to express it.' || CHAR(10) ||
  'It lays the groundwork for setting up equations and functions, making it an essential step in algebraic reasoning.'
);

-- Goal 1.2: Combining Like Terms

-- Combining Like Terms - Objective 1: "Identify and combine like terms in algebraic expressions."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Combining like terms is a fundamental skill in simplifying algebraic expressions.' || CHAR(10) ||
  'Like terms are terms within an expression that have the same variables raised to the same powers.' || CHAR(10) ||
  'Grouping like terms allows us to rewrite expressions in simpler forms without changing their value.' || CHAR(10) ||
  'This process reduces complexity and prepares expressions for further operations such as evaluation or solving equations.' || CHAR(10) ||
  'Identifying like terms requires attention to both the variables involved and their exponents.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
  '**Like Terms:** Terms in an expression that contain the exact same variables with the same exponents.' || CHAR(10) ||
  '**Coefficient:** The numerical part of a term that multiplies the variable.' || CHAR(10) ||
  '**Variable:** A letter that represents an unknown or changeable quantity.' || CHAR(10) ||
  '**Exponent:** A number that indicates how many times the variable is multiplied by itself.' || CHAR(10) ||
  'Only like terms can be combined by adding or subtracting their coefficients.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
  'To identify like terms, compare the variables and their exponents in each term.' || CHAR(10) ||
  'Group terms that have exactly the same variables raised to the same powers.' || CHAR(10) ||
  'Ignore the coefficients when grouping since like terms can have different numerical coefficients.' || CHAR(10) ||
  'Once grouped, these terms can be combined in later steps to simplify the expression.'
);

-- Strategic Knowledge 
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When identifying like terms in complex expressions, first remove any parentheses by applying the distributive property if necessary.' || CHAR(10) ||
  'Next, write down all terms clearly, paying attention to variables and exponents.' || CHAR(10) ||
  'Group terms by matching their variables and exponents precisely.' || CHAR(10) ||
  'Label each group to keep track of which terms can be combined.' || CHAR(10) ||
  'This organized approach makes it easier to simplify the expression systematically.'
);

-- Rational Knowlege
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Identifying and grouping like terms is essential because it helps maintain the integrity of an expression while simplifying it.' || CHAR(10) ||
  'Combining unlike terms would change the value and meaning of the expression.' || CHAR(10) ||
  'Recognizing like terms ensures that simplification follows algebraic principles and prepares expressions for further operations like evaluation or solving equations.' || CHAR(10) ||
  'This skill builds precision and deeper understanding of algebraic structure.'
);  

-- Combining Like Terms - Objective 2: "Apply the distributive property to combine like terms."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Simplifying an expression means rewriting it in the most compact and understandable form without changing its value.' || CHAR(10) ||
  'This includes combining like terms, removing unnecessary parentheses, and reducing constants where possible.' || CHAR(10) ||
  'Simplification helps make expressions easier to evaluate, compare, and use in equations or functions.' || CHAR(10) ||
  'Understanding simplification prepares students to work more efficiently with more complex algebraic problems later.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
  '**Simplify:** To rewrite an expression in its simplest form by combining like terms and reducing constants.' || CHAR(10) ||
  '**Constant:** A number without a variable.' || CHAR(10) ||
  '**Simplified Expression:** An expression where no further operations can be performed to combine terms.' || CHAR(10) ||
  'Only like terms may be combined during simplification.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Combining like terms involves a process of organizing and simplifying an expression to make it more manageable.' || CHAR(10) ||
    'First, scan the expression to identify which terms are like terms; they must have the same variable part (e.g., x, or 2xy).' || CHAR(10) ||
    'Next, group the like terms together. This helps visualize which terms can be combined.' || CHAR(10) ||
    'Then, add or subtract their coefficients while keeping the variable part unchanged.' || CHAR(10) ||
    'This step reduces the number of terms and simplifies the structure of the expression, making it easier to evaluate or manipulate further.' || CHAR(10) ||
    'Always double-check that terms are truly "like" before combining, especially when variables have exponents.'
);

-- Stragegic knowlege
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When simplifying algebraic expressions, it''s important to first scan the entire expression to understand its overall structure.' || CHAR(10) ||
  'Rather than jumping straight into combining terms, consider how different parts of the expression interact—such as distributed terms, constants, or signs spread throughout.' || CHAR(10) ||
  'Look for opportunities to mentally group terms and anticipate which combinations will streamline the expression most effectively.' || CHAR(10) ||
  'This mindset prevents common mistakes like combining unrelated terms and allows for greater flexibility in how the expression is approached and rewritten.' || CHAR(10) ||
  'Mastering this strategy leads to quicker recognition of simplification patterns and prepares students for manipulating more complex algebraic forms.'
);

-- Rational
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Simplifying expressions is a critical skill because it makes mathematical communication more efficient.' || CHAR(10) ||
  'It helps reduce the chances of making errors in later steps like solving equations or graphing functions.' || CHAR(10) ||
  'Simplification also reveals the structure of an expression, making it easier to analyze and apply in real-world contexts.' || CHAR(10) ||
  'Without simplification, expressions can remain unnecessarily complex and harder to interpret.'
);

-- Goal 1.3: Properties of Real Numbers 

-- Properties of Real Numbers - Objective 1: "Recognize associative, commutative, and distributive properties."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Real numbers have several important properties that are used in algebraic operations.' || CHAR(10) ||
    'These properties include the commutative, associative, and distributive properties, which govern how numbers can be combined and manipulated.' || CHAR(10) ||
    'Understanding these properties is crucial for simplifying expressions and solving equations.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Commutative property:** The order of addition or multiplication does not change the result (e.g., a + b = b + a).' || CHAR(10) ||
    '**Associative property:** The way numbers are grouped in addition or multiplication does not change the result (e.g., (a + b) + c = a + (b + c)).' || CHAR(10) ||
    '**Distributive property:** Multiplying a number by a sum is the same as doing each multiplication separately (e.g., a(b + c) = ab + ac).' || CHAR(10) ||
    CHAR(10) ||
    'These properties are foundational for working with real numbers and are used extensively in algebra.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Understanding the properties of real numbers involves recognizing how they apply to different operations.' || CHAR(10) ||
    'For example, the commutative property allows you to rearrange terms in an expression without changing its value.' || CHAR(10) ||
    'The associative property lets you regroup terms, which can simplify calculations.' || CHAR(10) ||
    'The distributive property is particularly useful for expanding expressions and combining like terms.' || CHAR(10) ||
    'Applying these properties correctly can lead to more efficient problem-solving and clearer algebraic expressions.'
);

-- Properties of Real Numbers - Objective 2: "Recognize identity and inverse properties of addition and multiplication."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'The identity and inverse properties are key concepts in algebra that help simplify expressions and solve equations.' || CHAR(10) ||
    'The identity property states that adding zero or multiplying by one does not change a number (e.g., a + 0 = a, a * 1 = a).' || CHAR(10) ||
    'The inverse property involves adding the opposite (negative) or multiplying by the reciprocal to obtain the identity element (e.g., a + (-a) = 0, a * (1/a) = 1).'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Identity property:** Adding zero or multiplying by one does not change a number (e.g., a + 0 = a, a * 1 = a).' || CHAR(10) ||
    '**Inverse property:** Adding the opposite (negative) or multiplying by the reciprocal yields the identity element (e.g., a + (-a) = 0, a * (1/a) = 1).'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Applying the identity and inverse properties involves recognizing when to use them in algebraic expressions.' || CHAR(10) ||
    'For example, when simplifying an expression, you can add zero to a term without changing its value.' || CHAR(10) ||
    'Similarly, multiplying by one keeps the term unchanged.' || CHAR(10) ||
    'Using the inverse property allows you to eliminate terms by adding their opposites or multiplying by their reciprocals.' || CHAR(10) ||
    'These properties are essential for solving equations and simplifying algebraic expressions effectively.'
);

-- Goal 1.4: Solving Equations

-- =========================================================================
-- Topic 2: Equations
-- =========================================================================

-- Goal 2.1: Solving one-Step Equations
-- Solving One-Step Equations - Objective 1: "Identify one-step equations and their components."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'One-step equations are algebraic expressions that can be solved in a single step by performing the inverse operation.' || CHAR(10) ||
    'They typically involve a single variable and a constant, making them straightforward to solve.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**One-step equation:** An equation that can be solved in one operation (e.g., x + 5 = 10).' || CHAR(10) ||
    '**Components:** Variable (x), constant (5), and the equality sign (=).' || CHAR(10) ||
    '**Inverse operation:** The operation that reverses the effect of the original operation (e.g., subtraction for addition, division for multiplication).' || CHAR(10) ||
    'Solving one-step equations involves isolating the variable by applying the inverse operation to both sides of the equation.' || CHAR(10) ||
    'This process helps to find the value of the variable that makes the equation true.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To solve a one-step equation, first identify the operation being performed on the variable.' || CHAR(10) ||
    'Next, apply the inverse operation to both sides of the equation to isolate the variable.' || CHAR(10) ||
    'For example, if the equation is x + 5 = 10, subtract 5 from both sides to find x = 5.' || CHAR(10) ||
    'This process is straightforward and allows for quick solutions to simple equations.'
);

-- Solving One-Step Equations - Objective 2: "Recognize common mistakes in solving one-step equations."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Common mistakes in solving one-step equations include misidentifying the operation, incorrectly applying the inverse operation, and failing to isolate the variable.' || CHAR(10) ||
    'Being aware of these pitfalls can help you avoid errors and improve your problem-solving skills.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    'Misidentifying the operation, incorrectly applying the inverse operation, and failing to isolate the variable.' || CHAR(10) ||
    'These mistakes can lead to incorrect solutions and a misunderstanding of the equation-solving process.' || CHAR(10) ||
    'By recognizing these common pitfalls, you can develop strategies to avoid them and improve your overall problem-solving skills.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To avoid common mistakes in solving one-step equations, carefully read the equation and identify the operation being performed on the variable.' || CHAR(10) ||
    'Ensure you apply the correct inverse operation to both sides of the equation.' || CHAR(10) ||
    'Double-check your work by substituting the solution back into the original equation to verify its correctness.' || CHAR(10) ||
    'Practicing with various one-step equations can help reinforce these concepts and improve your accuracy.'
);

-- Goal 2.2: Solving Two-Step Equations

-- Solving Two-Step Equations - Objective 1: "Identify two-step equations and their components."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Two-step equations are algebraic equations that require two operations to isolate the variable.' || CHAR(10) ||
    'Common components of two-step equations include the variable, constants, and the equality sign.' || CHAR(10) ||
    'Recognizing these components is essential for understanding how to solve two-step equations effectively.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    'Two-step equations are defined by their requirement for two operations to isolate the variable.' || CHAR(10) ||
    'Key components include the variable (the unknown), constants (known values), and the equality sign (indicating balance).' || CHAR(10) ||
    'Understanding these definitions is crucial for effectively solving two-step equations.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To solve a two-step equation, first identify the two operations involved in isolating the variable.' || CHAR(10) ||
    'Next, apply the inverse operation to eliminate the constant term from one side of the equation.' || CHAR(10) ||
    'Finally, use the inverse operation again to solve for the variable, ensuring to maintain balance throughout the process.'
);

-- Solving Two-Step Equations - Objective 2: "Apply inverse operations to solve two-step equations."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'To solve two-step equations, you must apply inverse operations in the correct order.' || CHAR(10) ||
    'This involves first eliminating any constants from the variable side of the equation, followed by isolating the variable itself.' || CHAR(10) ||
    'Understanding the role of inverse operations is key to successfully solving these equations.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    'Two-step equations require the application of inverse operations to isolate the variable.' || CHAR(10) ||
    'Unlike one-step equations, two-step equations involve an additional constant that must be eliminated before isolating the variable.' || CHAR(10) ||
    'Understanding the correct order of operations is crucial for solving these equations effectively.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To solve a two-step equation, first identify the two operations involved in isolating the variable.' || CHAR(10) ||
    'Next, apply the inverse operation to eliminate the constant term from one side of the equation.' || CHAR(10) ||
    'Finally, use the inverse operation again to solve for the variable, ensuring to maintain balance throughout the process.'
);

-- =========================================================================
-- Topic 3: Inequalities
-- =========================================================================

-- Goal 3.1: Properties of Sets

-- Properties of Sets - Objective 1: "Understand the basic properties of sets."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Sets are collections of distinct objects, considered as an object in their own right.' || CHAR(10) ||
    'Basic properties of sets include: membership (an element is either in a set or not), subset (a set is a subset of another if all its elements are in that set), and union/intersection (combining sets or finding common elements).' || CHAR(10) ||
    'Sets are foundational in mathematics, providing a framework for organizing and analyzing collections of objects.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Set:** A collection of distinct objects, considered as an object in its own right.' || CHAR(10) ||
    '**Membership:** An element is either in a set or not.' || CHAR(10) ||
    '**Subset:** A set is a subset of another if all its elements are in that set.' || CHAR(10) ||
    '**Union:** The union of two sets is a set containing all elements from both sets.' || CHAR(10) ||
    '**Intersection:** The intersection of two sets is a set containing only the elements common to both sets.' || CHAR(10) ||
    'Sets provide a framework for organizing and analyzing collections of objects.' || CHAR(10) ||
    'Understanding these basic properties allows for effective manipulation and analysis of sets.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To work with sets effectively, one must first understand how to define a set and its elements.' || CHAR(10) ||
    'Practice identifying whether an element belongs to a set. Does it belong to one set or is it a subset of another?' || CHAR(10) ||
    'Understand the relationships between sets, including Union and Intersection.' || CHAR(10) ||
    'For example, if Set A = {1, 2, 3} and Set B = {3, 4, 5}, the Union is {1, 2, 3, 4, 5} and the Intersection is {3}.'
);

-- Properties of Sets - Objective 2: "How to apply set properties in problem-solving."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Set operations can be used to solve problems involving classification, grouping, and membership.' || CHAR(10) ||
    'Common scenarios include finding elements shared between groups (intersection), combining elements from multiple groups (union), or determining which elements belong to one group but not another (complement or difference).' || CHAR(10) ||
    'These operations allow you to organize and interpret data logically, which is useful in areas like probability, logic, and data analysis.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Set Union (A u B):** The set of elements in A, or B, or both.' || CHAR(10) ||
    '**Set Intersection (A n B):** The set of elements in both A and B.' || CHAR(10) ||
    '**Set Difference (A - B):** The set of elements in A that are not in B.' || CHAR(10) ||
    '**Complement (A''):** The set of all elements not in A, relative to the universal set.' || CHAR(10) ||
    'Understanding these operations allows for solving problems that involve grouping, exclusion, and overlap.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Sets - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To apply set properties in problem-solving, start by identifying the sets involved in the problem.' || CHAR(10) ||
    'Determine which operations are needed: Are you looking for common elements (intersection), all elements combined (union), or elements unique to one set (difference)?' || CHAR(10) ||
    'Use Venn diagrams to visualize relationships between sets, which can help clarify complex problems.' || CHAR(10) ||
    'By following these steps, you can effectively apply set properties to a wide range of problems.'
);

-- Goal 3.2: Write and graph inequalities

-- Write and Graph Inequalities - Objective 1: "Understanding inequalities."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Inequalities express a relationship between two values, indicating that one is greater than, less than, or not equal to the other.' || CHAR(10) ||
    'Common inequality symbols include > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).' || CHAR(10) ||
    'Understanding these symbols is crucial for interpreting and solving inequality problems.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Inequality Symbols:** The symbols used to represent inequalities include:' || CHAR(10) ||
    '- **>** (greater than)' || CHAR(10) ||
    '- **<** (less than)' || CHAR(10) ||
    '- **>=** (greater than or equal to)' || CHAR(10) ||
    '- **<=** (less than or equal to)' || CHAR(10) ||
    'Understanding these symbols is essential for working with inequalities.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To write an inequality, start by identifying the relationship between the two values.' || CHAR(10) ||
    'Use the appropriate inequality symbol to express this relationship.' || CHAR(10) ||
    'To solve inequalities, start by isolating the variable on one side of the inequality sign.' || CHAR(10) ||
    'Use inverse operations to eliminate terms, just as you would in an equation.' || CHAR(10) ||
    'Remember to reverse the inequality sign when multiplying or dividing by a negative number.'
);

-- Write and Graph Inequalities - Objective 2: "Graphing inequalities on a number line."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Graphing inequalities involves representing the solution set on a number line.' || CHAR(10) ||
    'Open circles indicate that an endpoint is not included, while closed circles indicate inclusion.' || CHAR(10) ||
    'Shading is used to represent all the numbers that satisfy the inequality.' || CHAR(10) ||
    'By graphing inequalities, you can visualize the range of possible solutions and better understand the relationships between values.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Open Circle:** Used on a number line to indicate that the endpoint is not included in the solution set (e.g., x < 3).' || CHAR(10) ||
    '**Closed Circle:** Used to indicate that the endpoint is included in the solution set (e.g., x <= 3).' || CHAR(10) ||
    '**Shading:** Represents all numbers that satisfy the inequality, extending infinitely in one direction.' || CHAR(10) ||
    'Understanding these concepts is essential for accurately graphing inequalities.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'To graph an inequality on a number line, start by drawing a horizontal line representing the number line.' || CHAR(10) ||
    'Next, plot the critical point (the number that makes the inequality true) on the line.' || CHAR(10) ||
    'Use an open circle for < or > inequalities and a closed circle for <= or >= inequalities.' || CHAR(10) ||
    'Finally, shade the appropriate region of the number line to indicate all possible solutions.'
);

