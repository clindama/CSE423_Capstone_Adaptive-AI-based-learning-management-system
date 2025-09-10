
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
    'To manipulate expressions effectively, begin by identifying like terms these are terms that share identical variables and exponents.' || CHAR(10) ||
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
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  '**Simplify:** To rewrite an expression in its simplest form by combining like terms and reducing constants.' || CHAR(10) ||
  '**Constant:** A number without a variable.' || CHAR(10) ||
  '**Simplified Expression:** An expression where no further operations can be performed to combine terms.' || CHAR(10) ||
  'Only like terms may be combined during simplification.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
  'The properties of real numbers describe predictable behaviors of addition and multiplication.' || CHAR(10) ||
  'These include the commutative property (order doesn''t matter), the associative property (grouping doesn''t matter), and the distributive property (multiplying over a sum or difference).' || CHAR(10) ||
  'Knowing these rules helps in simplifying expressions, solving equations, and recognizing mathematical patterns across different problems.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    '**Commutative property:** The order of addition or multiplication does not change the result (e.g., a + b = b + a).' || CHAR(10) ||
    '**Associative property:** The way numbers are grouped in addition or multiplication does not change the result (e.g., (a + b) + c = a + (b + c)).' || CHAR(10) ||
    '**Distributive property:** Multiplying a number by a sum is the same as doing each multiplication separately (e.g., a(b + c) = ab + ac).' || CHAR(10) ||
    CHAR(10) ||
    'These properties are foundational for working with real numbers and are used extensively in algebra.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'Simplifying algebraic expressions becomes more efficient when you use properties of real numbers deliberately.' || CHAR(10) ||
  'For example, recognizing when the distributive property can help eliminate parentheses or when rearranging terms using the commutative property makes like terms easier to spot.' || CHAR(10) ||
  'These properties are tools—not just rules—and selecting the right one depends on how the expression is structured.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Rather than memorizing properties in isolation, focus on how each one helps you manipulate expressions more flexibly.' || CHAR(10) ||
  'For example, the commutative property is most helpful when you''re trying to group like terms together, while the distributive property is key when removing parentheses efficiently.' || CHAR(10) ||
  'Strategically, your goal is to recognize which property simplifies your task—not just to identify the property, but to see its purpose in context.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Mathematical properties exist to guarantee consistency, regardless of how operations are arranged.' || CHAR(10) ||
  'Understanding these properties is not about rules for their own sake, it''s about why we can safely rearrange or regroup without changing value.' || CHAR(10) ||
  'This reliability underpins everything from simple arithmetic to advanced algebra, making these properties fundamental to mathematical reasoning.'
);

-- Properties of Real Numbers - Objective 2: "Recognize identity and inverse properties of addition and multiplication."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Simplifying algebraic expressions becomes more efficient when you use properties of real numbers deliberately.' || CHAR(10) ||
  'For example, recognizing when the distributive property can help eliminate parentheses or when rearranging terms using the commutative property makes like terms easier to spot.' || CHAR(10) ||
  'These properties are tools not just rules and selecting the right one depends on how the expression is structured.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Simplifying expressions often uses:' || CHAR(10) ||
  '- The **commutative property** to reorder terms for easier grouping.' || CHAR(10) ||
  '- The **associative property** to regroup numbers or variables.' || CHAR(10) ||
  '- The **distributive property** to eliminate parentheses and combine like terms.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To simplify using the distributive property: Identify any multiplication over parentheses and distribute the multiplier to each term inside.' || CHAR(10) ||
  'After removing parentheses, use the commutative and associative properties to reorder and regroup like terms, which can then be combined.' || CHAR(10) ||
  'This step-by-step approach ensures clarity, especially in more complex expressions.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When simplifying, pause to decide *which* property helps you gain the most clarity.' || CHAR(10) ||
  'You might begin by distributing to remove parentheses, then rearrange terms using the commutative property, followed by regrouping via the associative property.' || CHAR(10) ||
  'This flexible sequencing is key: not every problem follows the same path, and skilled simplification means choosing the most efficient property at each step based on structure.' || CHAR(10) ||
  'Think of these properties as tools in a toolkit. You select and apply them strategically to simplify without introducing errors.'
);

-- Rational Knowledge 
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Properties of Real Numbers - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'These properties exist because arithmetic and algebra need consistent behavior regardless of how numbers are grouped or ordered.' || CHAR(10) ||
  'They ensure that expressions can be simplified or rearranged without changing their value.' || CHAR(10) ||
  'Without these properties, basic operations like distributing a value across a sum or swapping the order of multiplication wouldn''t be reliable—making algebra much harder to work with.'
);

-- Goal 1.4: Exponents and Order of Operations
-- Exponents and Order of Operations - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Order of operations ensures consistency in solving expressions. ' ||
    'PEMDAS stands for Parentheses, Exponents, Multiplication and Division, Addition and Subtraction. ' || CHAR(10) ||
    'This order dictates how complex expressions are approached and guarantees uniform results regardless of who is solving them.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    'PEMDAS is an acronym used to remember the order of operations: ' ||
    'Parentheses, Exponents, Multiplication, Division, Addition, Subtraction. ' || CHAR(10) ||
    'Multiplication and division are processed from left to right, as are addition and subtraction.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
    'To apply the order of operations, begin by evaluating expressions within parentheses, ' ||
    'then apply any exponents. Next, handle all multiplication and division from left to right, ' ||
    'and finally perform addition and subtraction from left to right.'
);

-- Strategic knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
    'When facing expressions that involve nested groupings, exponents, and multiple operations, ' ||
    'scan the entire expression first to identify dependencies. Consider rewriting parts using simpler structures ' ||
    'or grouping logically related terms to avoid misapplication of operations. ' || CHAR(10) ||
    'Strategically balancing steps avoids common pitfalls like doing addition before division.'
);

-- Rational knoledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
    'Following a universal order of operations prevents ambiguity and ensures fairness in mathematics. ' ||
    'It allows individuals and systems to agree on one interpretation and ensures automated systems produce reliable results.'
);

-- Exponents and Order of Operations - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Exponent rules are shortcuts that simplify repeated multiplication. ' ||
    'They include ways to combine powers, distribute them over multiplication or division, ' ||
    'and interpret expressions with zero or negative exponents.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    'Important exponent rules include the product rule (add exponents), ' ||
    'power of a power rule (multiply exponents), and the zero exponent rule (any base to the zero power equals one).'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
    'To apply the product rule, ensure the bases are the same and then add their exponents. ' ||
    'Use the power of a power rule when an exponent is raised to another exponent. ' ||
    'Apply each rule based on the structure of the expression.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
    'Begin by identifying which rule applies to each portion of the expression. ' ||
    'If the expression involves multiple terms and operations, isolate power components and simplify them in stages. ' ||
    'Group terms with common bases and delay simplification until all like terms have been addressed. ' || CHAR(10) ||
    'This modular approach allows better control and fewer mistakes when applying multiple exponent rules together.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Exponents - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
    'Exponent rules provide efficient alternatives to repeated multiplication, ' ||
    'especially as expressions become more complex. ' ||
    'These rules reduce cognitive load and allow for generalizations that apply across algebra and higher mathematics.'
);

-- Goal 1.5: Absolute Value
-- Absolute Value - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Absolute value represents the distance of a number from zero on the number line, regardless of direction. ' || CHAR(10) ||
  'It is always a non-negative value because distance cannot be negative. ' || CHAR(10) ||
  'This concept helps students understand how numbers relate to position and magnitude rather than just their sign.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'The **absolute value** of a real number x, denoted |x|, is the distance between x and zero on the number line. ' || CHAR(10) ||
  'Formally, |x| = x if x is greater than or equal to zero, and |x| = -x if x is less than zero.' || CHAR(10) ||
  'Absolute value ignores the sign of the number and focuses on magnitude.' || CHAR(10) ||
  'This makes it useful in many areas such as measuring distance, error tolerance, and solving equations involving distances.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To find the absolute value of a number, first identify whether it is positive or negative. ' || CHAR(10) ||
  'If the number is positive or zero, its absolute value is the number itself. ' || CHAR(10) ||
  'If the number is negative, the absolute value is its opposite (change the sign to positive).'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When interpreting absolute value in problems, consider it as a measure of distance on the number line rather than a typical arithmetic operation. ' || CHAR(10) ||
  'This perspective helps in solving equations or inequalities involving absolute values by framing the problem as finding all points a certain distance from zero.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Absolute value reflects the fundamental idea of distance, which by nature cannot be negative. ' || CHAR(10) ||
  'Understanding absolute value prepares students for broader mathematical concepts such as metric spaces and vector norms, where magnitude is separated from direction. ' || CHAR(10) ||
  'It reinforces that mathematical operations can represent real-world measurements beyond simple calculations.'
);

-- Absolute Value - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Evaluating absolute value expressions means applying the definition of absolute value to calculate the distance from zero. ' || CHAR(10) ||
  'This includes recognizing when to change the sign of negative numbers and understanding the results in the context of the problem.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'When evaluating |x|, if x is positive or zero, the result is x itself. ' || CHAR(10) ||
  'If x is negative, the result is -x, which is positive. ' || CHAR(10) ||
  'Absolute value expressions can also involve variables, requiring evaluation after substituting numerical values.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To evaluate an absolute value expression, first simplify inside the absolute value symbols if necessary. ' || CHAR(10) ||
  'Then determine the sign of the result and apply the absolute value definition accordingly, ' || CHAR(10) ||
  'ensuring the final answer is always non-negative.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When evaluating expressions involving absolute values, analyze the structure to determine if multiple absolute values interact. ' || CHAR(10) ||
  'Plan to simplify each absolute value component individually before combining results, especially in more complex algebraic expressions.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Absolute Value - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Evaluating absolute value expressions requires an understanding of how absolute value reflects distance and magnitude, ' || CHAR(10) ||
  'not just numerical value. ' || CHAR(10) ||
  'This conceptual understanding helps you to correctly interpret results in real-world contexts such as error measurement and distance comparisons.'
);

-- Goal 1.6 Simplify Expressions
-- Simplify Expresions - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Simplifying expressions involves using arithmetic and algebraic properties such as the associative, commutative, and distributive properties. ' || CHAR(10) ||
  'These properties allow rearranging and grouping terms to make expressions easier to work with and understand. ' || CHAR(10) ||
  'Recognizing when and how to apply these properties is key to effective simplification.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'The **associative property** states that how numbers are grouped does not affect their sum or product.' || CHAR(10) ||
  'The **commutative property** means numbers can be added or multiplied in any order.' || CHAR(10) ||
  'The **distributive property** allows multiplication over addition or subtraction to be rewritten as a sum or difference of products.' || CHAR(10) ||
  'These properties underpin many simplification techniques in algebra.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To simplify an expression, identify parts where properties of operations apply. ' || CHAR(10) ||
  'Group like terms and rearrange terms using commutative or associative properties. ' || CHAR(10) ||
  'Apply distributive property to remove parentheses and combine terms where possible.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Effective simplification involves planning the order in which properties are applied. ' || CHAR(10) ||
  'Consider simplifying inside parentheses first, then combining like terms, and finally using distributive or associative properties to rewrite the expression efficiently. ' || CHAR(10) ||
  'Strategically approaching simplification helps prevent errors and reduces the expression to its simplest form.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Simplifying expressions is fundamental to algebra as it transforms complex problems into manageable ones. ' || CHAR(10) ||
  'Understanding the properties that justify simplification ensures students grasp not just how but why expressions are equivalent before and after simplification.'
);

-- Simplify Expressions - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Solving complex expressions requires integrating multiple simplification techniques, careful order of operations, and accurate application of algebraic properties. ' || CHAR(10) ||
  'Complex expressions often include nested operations, exponents, and multiple terms that must be handled systematically.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Complex expressions may contain multiple layers such as nested parentheses, exponents, multiplication, division, addition, and subtraction. ' || CHAR(10) ||
  'Accurate simplification depends on the correct order of operations and application of algebraic properties at each step.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'Approach complex expressions by simplifying innermost parentheses first. ' || CHAR(10) ||
  'Next, apply exponent rules and multiplication or division, then combine like terms. ' || CHAR(10) ||
  'Maintain careful tracking of operations to ensure each step preserves equivalence.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Tackle complex expressions by decomposing them into smaller, simpler components. ' || CHAR(10) ||
  'Identify sequences where properties and operations interact, and plan simplification in stages. ' || CHAR(10) ||
  'This layered strategy reduces errors and helps manage complexity effectively.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Simplify - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Developing skill in simplifying complex expressions builds confidence for higher-level mathematics. ' || CHAR(10) ||
  'It promotes understanding of algebraic structure and the logical flow of operations, essential for problem solving across math disciplines.'
);

-- Goal 1.7 Evaluate Expressions
-- Evalualte Expressions - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Evaluating algebraic expressions involves replacing variables with specific numerical values. ' || CHAR(10) ||
  'This process transforms abstract expressions into concrete numbers, allowing calculation of their value. ' || CHAR(10) ||
  'Understanding the substitution process lays the foundation for solving equations and interpreting formulas.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Substitution is the process of replacing each variable in an expression with a given numerical value. ' || CHAR(10) ||
  'The expression is then simplified by performing arithmetic operations on the substituted values. ' || CHAR(10) ||
  'Correct substitution requires careful attention to each variable and its corresponding value to avoid errors.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To substitute values, identify each variable in the expression. ' || CHAR(10) ||
  'Replace the variable with the assigned number. ' || CHAR(10) ||
  'Perform arithmetic operations following standard rules to simplify the expression to a single numerical result.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When evaluating expressions with multiple variables and operations, consider substituting all variables first, ' || CHAR(10) ||
  'then simplify systematically to reduce mistakes. ' || CHAR(10) ||
  'Plan the evaluation to follow the order of operations strictly after substitution.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Substitution connects abstract algebraic concepts to concrete numeric values, ' || CHAR(10) ||
  'allowing students to interpret and evaluate mathematical models and formulas practically. ' || CHAR(10) ||
  'This understanding is essential for problem solving in science, engineering, and real-world applications.'
);

-- Evaluate Expressions - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Order of operations dictates the sequence in which parts of an expression are evaluated to ensure consistent and correct results. ' || CHAR(10) ||
  'It is essential when evaluating expressions that contain multiple operations to follow this hierarchy precisely.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'The standard order of operations is remembered by PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction. ' || CHAR(10) ||
  'Operations inside parentheses are evaluated first, followed by exponents, then multiplication and division (left to right), and finally addition and subtraction (left to right).'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To evaluate an expression accurately, first perform calculations inside parentheses. ' || CHAR(10) ||
  'Next, apply exponentiation, then multiplication and division from left to right. ' || CHAR(10) ||
  'Finally, carry out addition and subtraction from left to right to simplify the expression completely.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Before calculating, analyze the expression to identify nested operations and prioritize calculations accordingly. ' || CHAR(10) ||
  'Breaking down the expression mentally or on paper helps prevent misapplication of the order of operations, especially in complex expressions involving several operation types.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Evaluate - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Strict adherence to the order of operations is crucial because it provides a universal standard ensuring all students and mathematicians arrive at the same result for the same expression. ' || CHAR(10) ||
  'This consistency is foundational to clear mathematical communication and problem solving.'
);

-- Goal 1.8 Write Expressions from Verbal
-- Write Expressions from Verbal - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Translating verbal phrases into algebraic expressions requires understanding common keywords that represent operations and relationships. ' || CHAR(10) ||
  'This skill enables students to convert real-world descriptions into mathematical language for analysis and problem solving.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Common keywords include: "sum" meaning addition, "difference" meaning subtraction, "product" meaning multiplication, and "quotient" meaning division. ' || CHAR(10) ||
  '"More than," "increased by," and "added to" usually indicate addition, while "less than," "decreased by," and "subtracted from" indicate subtraction. ' || CHAR(10) ||
  'Recognizing these keywords helps accurately translate phrases into symbols like +, -, *, and /.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To translate verbal phrases, first identify the keywords representing mathematical operations. ' || CHAR(10) ||
  'Next, assign variables to unknown quantities mentioned in the phrase. ' || CHAR(10) ||
  'Finally, write the corresponding algebraic expression using symbols that match the keywords.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When translating more complex verbal statements, break down the sentence into smaller parts, identifying operations in sequence. ' || CHAR(10) ||
  'Analyze the relationship between quantities and how each part connects before forming the complete expression.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Translating verbal phrases to algebraic expressions builds a bridge between everyday language and mathematical reasoning. ' || CHAR(10) ||
  'This process improves problem comprehension and prepares students for solving algebraic problems based on real-world scenarios.'
);

-- Write Expressions from Verbal - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'Multi-step verbal scenarios involve several operations and relationships that must be translated carefully into algebraic expressions. ' || CHAR(10) ||
  'Understanding the sequence and connection between parts is essential for accurate expression construction.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Multi-step expressions combine multiple operations such as addition, subtraction, multiplication, and division, often with variables representing unknown quantities. ' || CHAR(10) ||
  'Proper interpretation requires identifying each operation and its position within the scenario.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To construct expressions from multi-step scenarios, begin by breaking the problem into parts. ' || CHAR(10) ||
  'Translate each part into an algebraic expression using variables and operations. ' || CHAR(10) ||
  'Then, combine these parts according to the relationships described to form the full expression.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Approach multi-step translations by planning the order of operations represented in the scenario. ' || CHAR(10) ||
  'Consider grouping related operations with parentheses to clarify structure and ensure correct interpretation.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Verbal - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Mastering multi-step translation sharpens analytical skills and helps students to interpret and solve complex real-world problems using algebraic methods. ' || CHAR(10) ||
  'It deepens understanding of how mathematical expressions model relationships between quantities.'
);

-- Goal 1.9: Intro to Equations
-- Intro to Equations - Objective 1
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'An equation is a mathematical statement that asserts the equality of two expressions by using an equals sign (=). ' || CHAR(10) ||
  'Solving an equation means finding the value(s) of the variable(s) that make the equation true. ' || CHAR(10) ||
  'Simple equations typically involve one variable and straightforward operations.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'An **equation** is a statement that two expressions are equal, using the symbol "=". ' || CHAR(10) ||
  'A **variable** is a symbol representing an unknown value to be found. ' || CHAR(10) ||
  'The goal of solving is to isolate the variable on one side of the equation to determine its value.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To solve a simple equation, perform operations that isolate the variable step by step. ' || CHAR(10) ||
  'Use inverse operations such as addition/subtraction or multiplication/division to both sides of the equation. ' || CHAR(10) ||
  'Maintain equality by performing the same operation on both sides until the variable is alone.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'When solving equations, plan your approach by identifying the simplest inverse operations first. ' || CHAR(10) ||
  'Consider the order of operations in reverse to systematically undo operations applied to the variable. ' || CHAR(10) ||
  'Check your solution by substituting it back into the original equation.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 1'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Solving equations is fundamental because it allows us to find unknown quantities and understand relationships expressed mathematically. ' || CHAR(10) ||
  'The process builds logical thinking by balancing both sides of an equation to maintain equality.'
);

-- Intro to Equations - Objective 2
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
  'More complex equations may involve multiple steps, variables on both sides, parentheses, or requiring the use of distributive property. ' || CHAR(10) ||
  'Solving these requires applying several algebraic techniques in combination.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
  'Complex equations might include expressions on both sides of the equals sign and require simplification before isolating the variable. ' || CHAR(10) ||
  'Use of properties such as the distributive property is often necessary to remove parentheses and combine like terms.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
  'To solve complex equations, first simplify each side by applying distributive property and combining like terms. ' || CHAR(10) ||
  'Next, collect variable terms on one side and constants on the other by adding or subtracting both sides accordingly. ' || CHAR(10) ||
  'Finally, isolate the variable by performing inverse operations.'
);

-- Strategic Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'strategy'),
  'Develop a plan to simplify and reorganize the equation stepwise: ' || CHAR(10) ||
  'Start with removing parentheses, then combine like terms, next move variables and constants to separate sides, and lastly isolate the variable. ' || CHAR(10) ||
  'Review each step carefully to avoid mistakes and verify solutions at the end.'
);

-- Rational Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
  (SELECT id FROM LearningObjective WHERE title = 'Equations - Objective 2'),
  (SELECT id FROM InstructionMethod WHERE method_keyword = 'rationale'),
  'Mastering complex equations helps students handle real-world problems where relationships between quantities are not simple. ' || CHAR(10) ||
  'Understanding the logic behind each step strengthens problem-solving skills and algebraic thinking.'
);

-- ************************************************************************* - End of Topic 1

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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    'Misidentifying the operation, incorrectly applying the inverse operation, and failing to isolate the variable.' || CHAR(10) ||
    'These mistakes can lead to incorrect solutions and a misunderstanding of the equation-solving process.' || CHAR(10) ||
    'By recognizing these common pitfalls, you can develop strategies to avoid them and improve your overall problem-solving skills.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving One-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    'Two-step equations are defined by their requirement for two operations to isolate the variable.' || CHAR(10) ||
    'Key components include the variable (the unknown), constants (known values), and the equality sign (indicating balance).' || CHAR(10) ||
    'Understanding these definitions is crucial for effectively solving two-step equations.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    'Two-step equations require the application of inverse operations to isolate the variable.' || CHAR(10) ||
    'Unlike one-step equations, two-step equations involve an additional constant that must be eliminated before isolating the variable.' || CHAR(10) ||
    'Understanding the correct order of operations is crucial for solving these equations effectively.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Solving Two-Step Equations - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
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
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'fact'),
    '**Open Circle:** Used on a number line to indicate that the endpoint is not included in the solution set (e.g., x < 3).' || CHAR(10) ||
    '**Closed Circle:** Used to indicate that the endpoint is included in the solution set (e.g., x <= 3).' || CHAR(10) ||
    '**Shading:** Represents all numbers that satisfy the inequality, extending infinitely in one direction.' || CHAR(10) ||
    'Understanding these concepts is essential for accurately graphing inequalities.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Write and Graph Inequalities - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'procedure'),
    'To graph an inequality on a number line, start by drawing a horizontal line representing the number line.' || CHAR(10) ||
    'Next, plot the critical point (the number that makes the inequality true) on the line.' || CHAR(10) ||
    'Use an open circle for < or > inequalities and a closed circle for <= or >= inequalities.' || CHAR(10) ||
    'Finally, shade the appropriate region of the number line to indicate all possible solutions.'
);

