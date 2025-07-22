
-- Content for Topics 1-3 (Only the first 3 Goals and their Objectives)
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
    'An algebraic expression combines variables, constants, and arithmetic operations (such as addition, subtraction, multiplication, and division) to represent quantities or relationships.' || CHAR(10) ||
    'Unlike equations, expressions do not have an equals sign.' || CHAR(10) ||
    'Understanding expressions is foundational for algebra because it enables simplification, evaluation, and preparation for solving equations.' || CHAR(10) ||
    'Manipulating expressions allows us to rewrite them in simpler or equivalent forms, making complex problems easier to solve.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Expression:** A mathematical phrase made up of numbers, variables, and operators but without an equals sign.' || CHAR(10) ||
    '**Variable:** A symbol, often a letter, that represents an unknown or changeable quantity.' || CHAR(10) ||
    '**Coefficient:** The numerical factor multiplying a variable.' || CHAR(10) ||
    '**Constant:** A fixed number that does not change.' || CHAR(10) ||
    '**Term:** A single number, variable, or the product of numbers and variables.' || CHAR(10) ||
    '**Operator:** Symbols that indicate mathematical operations (e.g., +, -, *, /).' || CHAR(10) ||
    CHAR(10) ||
    'Expressions can be classified by the number of terms they contain, such as monomials (one term), binomials (two terms), and polynomials (many terms).' || CHAR(10) ||
    'Manipulating expressions requires knowledge of arithmetic rules and properties such as the distributive property and combining like terms.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Manipulating algebraic expressions involves understanding their structure and the relationships between terms.' || CHAR(10) ||
    'An expression is made up of terms that can include variables and constants connected by operations.' || CHAR(10) ||
    CHAR(10) ||
    'When working with expressions, the first step is to identify all the terms clearly — this helps determine which parts can be combined or simplified.' || CHAR(10) ||
    'Next, recognizing "like terms" is important because only terms with the same variables and exponents can be combined without changing the meaning.' || CHAR(10) ||
    'Combining like terms simplifies the expression, making it easier to understand and work with.' || CHAR(10) ||
    'Applying properties like the distributive property allows us to rewrite expressions by removing parentheses and making the expression clearer.' || CHAR(10) ||
    'Throughout this process, following the correct order of operations ensures that the expression remains equivalent and accurate.' || CHAR(10) ||
    CHAR(10) ||
    'Each of these steps is designed to preserve the value the expression represents, while making it simpler or more useful for problem solving.'
);

-- *** Expressions - Objective 2 *** 

-- Expressions - Objective 2: "Apply properties of operations to simplify expressions."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Translating word problems into algebraic expressions is a critical skill that bridges everyday language and mathematical reasoning.' || CHAR(10) ||
    'It allows you to model real-world situations using variables and operations, making problems solvable with algebra.' || CHAR(10) ||
    'This process involves interpreting key quantities and their relationships as mathematical symbols.' || CHAR(10) ||
    'Developing this skill strengthens problem-solving ability, helping you analyze scenarios systematically and accurately.'
);

-- Factual Knowledge 
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Word problem:** A real-world scenario described in words requiring translation into a mathematical expression.' || CHAR(10) ||
    '**Variable assignment:** Choosing symbols to represent unknown quantities in the problem.' || CHAR(10) ||
    '**Operations keywords:** Words that indicate mathematical operations, such as "sum" for addition or "product" for multiplication.' || CHAR(10) ||
    CHAR(10) ||
    'Recognizing these keywords helps convert verbal descriptions into the correct arithmetic symbols.' || CHAR(10) ||
    'Assigning variables correctly and choosing the right operations are essential to accurately model the problem.' || CHAR(10) ||
    'Errors in this translation step can lead to incorrect solutions, so careful reading and understanding are important.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Expressions - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Translating a word problem into an algebraic expression involves several important conceptual steps.' || CHAR(10) ||
    'First, reading carefully allows you to understand the situation and what quantities are involved.' || CHAR(10) ||
    'Assigning variables to unknown quantities is a way of representing the problem symbolically — this makes it possible to use algebraic methods to analyze it.' || CHAR(10) ||
    'Identifying keywords that correspond to mathematical operations helps translate verbal relationships into arithmetic expressions.' || CHAR(10) ||
    'Constructing the expression by combining variables and numbers using these operations creates a mathematical model of the problem.' || CHAR(10) ||
    'Reviewing your expression ensures it accurately represents the original scenario.' || CHAR(10) ||
    CHAR(10) ||
    'This process transforms everyday language into a precise mathematical format, which is essential for solving the problem using algebra.'
);

-- Goal 1.2: Combining Like Terms

-- Combining Like Terms - Objective 1: "Identify and combine like terms in algebraic expressions."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'Combining like terms is a fundamental skill in algebra that simplifies expressions and makes solving equations easier.' || CHAR(10) ||
    'Like terms are terms that have the same variable raised to the same power, and they can be combined by adding or subtracting their coefficients.' || CHAR(10) ||
    'This process is essential for simplifying expressions, solving equations, and understanding algebraic structures.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Like terms:** Terms in an expression that have the same variable(s) raised to the same power.' || CHAR(10) ||
    '**Coefficient:** The numerical factor in a term, which can be positive, negative, or zero.' || CHAR(10) ||
    '**Combining like terms:** The process of adding or subtracting like terms to simplify an expression.' || CHAR(10) ||
    CHAR(10) ||
    'Recognizing like terms is crucial for simplifying expressions correctly.' || CHAR(10) ||
    'Combining like terms helps to reduce the complexity of algebraic expressions, making them easier to work with.'
);

-- Procedural Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 1'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'example'),
    'Combining like terms involves a process of organizing and simplifying an expression to make it more manageable.' || CHAR(10) ||
    'First, scan the expression to identify which terms are like terms; they must have the same variable part (e.g., x, or 2xy).' || CHAR(10) ||
    'Next, group the like terms together. This helps visualize which terms can be combined.' || CHAR(10) ||
    'Then, add or subtract their coefficients while keeping the variable part unchanged.' || CHAR(10) ||
    'This step reduces the number of terms and simplifies the structure of the expression, making it easier to evaluate or manipulate further.' || CHAR(10) ||
    'Always double-check that terms are truly "like" before combining, especially when variables have exponents.'
);

-- Combining Like Terms - Objective 2: "Apply the distributive property to combine like terms."
-- General Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'overview'),
    'The distributive property states that a(b + c) = ab + ac. This property can be used to combine like terms in an expression.' || CHAR(10) ||
    'By distributing a factor across terms inside parentheses, you can simplify expressions and combine like terms more easily.' || CHAR(10) ||
    'This technique is essential for solving equations and simplifying algebraic expressions.'
);

-- Factual Knowledge
INSERT INTO InstructionContent (objective_id, method_id, instruct_content)
VALUES (
    (SELECT id FROM LearningObjective WHERE title = 'Combine Like Terms - Objective 2'),
    (SELECT id FROM InstructionMethod WHERE method_keyword = 'definition'),
    '**Distributive property:** A mathematical property that allows you to multiply a single term by each term inside parentheses.' || CHAR(10) ||
    '**Factor:** A number or expression that is multiplied by another to form a product.' || CHAR(10) ||
    '**Combining like terms with distribution:** Using the distributive property to simplify expressions by combining like terms.' || CHAR(10) ||
    CHAR(10) ||
    'Understanding the distributive property is crucial for manipulating algebraic expressions effectively.' || CHAR(10) ||
    'It allows for simplification and helps in solving equations by breaking down complex expressions.'
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
