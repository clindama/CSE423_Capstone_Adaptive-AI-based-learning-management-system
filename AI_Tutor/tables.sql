-- Users table
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    account_type TEXT NOT NULL CHECK (account_type IN ('student', 'parent', 'admin'))
);

-- Topics Table
CREATE TABLE Topic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    topic_order INTEGER
);

-- Topics Progression (Tracks Student's progress per topic) 
CREATE TABLE TopicProgress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    topic_id INTEGER  NOT NULL,
    -- Progress is stored as a percentage (0-100)%
    progress INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (topic_id) REFERENCES Topic(id),
    -- Ensures a user can only have one progression record per topic
    UNIQUE (user_id, topic_id)
);

-- Goal Table
CREATE TABLE Goal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    goal_order INTEGER,
    FOREIGN KEY (topic_id) REFERENCES Topic(id)
);

-- Goal Progression (Tracks Student's progress per goal)
CREATE TABLE GoalProgress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    goal_id INTEGER NOT NULL,
    -- Grade is stored as a percentage (0-100)%
    grade INTEGER DEFAULT 0,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (goal_id) REFERENCES Goal(id),
    -- Ensures a user can only have one progression record per goal
    UNIQUE (user_id, goal_id)
);

-- Learning Objectives Table
CREATE TABLE LearningObjective (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    obj_order INTEGER,
    FOREIGN KEY (goal_id) REFERENCES Goal(id)
);

-- Direct Instruction Methods (Simulates AI Tutor's various teaching styles)
-- This table will decide the type of content provided during direct instruction
CREATE TABLE InstructionMethod (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    method_type TEXT NOT NULL CHECK (method_type IN ('general', 'factual', 'strategic', 'procedural', 'rational')),
    method_keyword TEXT NOT NULL UNIQUE
);

-- Direct Instruction Content
CREATE TABLE InstructionContent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objective_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    instruct_content TEXT NOT NULL,
    FOREIGN KEY (objective_id) REFERENCES LearningObjective(id),
    FOREIGN KEY (method_id) REFERENCES InstructionMethod(id),
    -- Ensures that each objective can have multiple methods
    -- but each method can only be assigned once per objective
    UNIQUE(objective_id, method_id)
);

-- Instruction Completion Table
-- This table tracks which user has completed which learning objective
CREATE TABLE InstructionCompletion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    instruction_id INTEGER NOT NULL,
    completion_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (instruction_id) REFERENCES InstructionContent(id),
    UNIQUE (user_id, instruction_id)
);

-- Walkthrough Problem Table
CREATE TABLE WalkThroughProblem (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objective_id INTEGER NOT NULL,
    walkthrough_content TEXT NOT NULL,
    solution TEXT NOT NULL,
    FOREIGN KEY (objective_id) REFERENCES LearningObjective(id)
);

-- Walkthrough Completion Table
-- This table tracks which user has completed which walkthrough problems
CREATE TABLE WalkthroughCompletion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    walkthrough_id INTEGER NOT NULL,
    completion_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (walkthrough_id) REFERENCES WalkthroughProblem(id),
    UNIQUE (user_id, walkthrough_id)
);

-- Problem Table
-- Stores all problems that can be assigned to users
CREATE TABLE Problem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    goal_id INTEGER NOT NULL,
    objective_id INTEGER NOT NULL,
    prompt TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('factual', 'procedural', 'strategic', 'rational')),
    tags TEXT,
    FOREIGN KEY (topic_id) REFERENCES Topic(id),
    FOREIGN KEY (goal_id) REFERENCES Goal(id),
    FOREIGN KEY (objective_id) REFERENCES LearningObjective(id)
);

-- Practice Problems Table
-- This table tracks progress of practice problem set assigned to users
CREATE TABLE PracticeProblemSet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    goal_id INTEGER NOT NULL,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    grade INTEGER DEFAULT 0,
    -- Tracks If the user has completed entire the practice problem set 
    is_complete BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (goal_id) REFERENCES Goal(id)
);

-- Practice Problems Table
-- This table tracks individual practice problems assigned to users
CREATE TABLE PracticeProblem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    set_id INTEGER NOT NULL,
    problem_id INTEGER NOT NULL,
    student_answer TEXT,
    is_correct BOOLEAN,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (set_id) REFERENCES PracticeProblemSet(id),
    FOREIGN KEY (problem_id) REFERENCES Problem(id),
    UNIQUE (set_id, problem_id)
);

-- Student Test Table
-- This table tracks tests assigned to students for each goal (pre/post tests)
CREATE TABLE StudentTest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_id INTEGER NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('pre', 'post')),
    title TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (goal_id) REFERENCES Goal(id),
    UNIQUE (goal_id, type)
);

-- Test Problem Table
-- This table links problems to tests, allowing multiple problems per test
CREATE TABLE TestProblems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id INTEGER NOT NULL,
    problem_id INTEGER NOT NULL,
    problem_order INTEGER,
    FOREIGN KEY (test_id) REFERENCES StudentTest(id),
    FOREIGN KEY (problem_id) REFERENCES Problem(id),
    UNIQUE (test_id, problem_id)
);

-- Test Attempt Table
-- This table tracks results of student attempts at tests
CREATE TABLE TestAttempt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME,
    score INTEGER DEFAULT 0,
    is_passed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (test_id) REFERENCES StudentTest(id)
);

-- Test Report Table
-- This table stores detailed reports of student attempts at each problem in a test
CREATE TABLE TestReport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_id INTEGER NOT NULL,
    problem_id INTEGER NOT NULL,
    student_answer TEXT,
    is_correct BOOLEAN,
    is_completed BOOLEAN DEFAULT FALSE,
    completion_time DATETIME,
    FOREIGN KEY (attempt_id) REFERENCES TestAttempt(id),
    FOREIGN KEY (problem_id) REFERENCES Problem(id),
    UNIQUE (attempt_id, problem_id)
);

-- Feedback after solving
-- This table allows students to recieve feedback on answers
CREATE TABLE Feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_id INTEGER,
    content TEXT NOT NULL,
    FOREIGN KEY (answer_id) REFERENCES Answer(id)
);

-- Hints Table
CREATE TABLE Hint (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem_id INTEGER NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('goal', 'step', 'problem')),
    content TEXT NOT NULL,
    hint_order INTEGER DEFAULT 1,
    FOREIGN KEY (problem_id) REFERENCES Problem(id)
);