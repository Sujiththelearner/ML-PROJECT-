"""
Phase 16: Recommendation Engine
Contains a maintainable knowledge base of actionable skill recommendations,
learning steps, and project suggestions.
"""

RECOMMENDATION_DATABASE = {
    "Python": {
        "importance": "Core programming language for Data Science, ML, and Backend Development.",
        "action_steps": [
            "Review Python fundamentals: data types, loops, list comprehensions, and functions.",
            "Master Object-Oriented Programming (OOP): classes, inheritance, and encapsulation.",
            "Practice file handling, error handling (try/except), and working with virtual environments.",
            "Build a modular project such as an automated script or a command-line tool."
        ],
        "project_idea": "Build a command-line task automation tool or an API scraper using Python.",
        "resources": "Official Python Docs (docs.python.org), freeCodeCamp Python Certification"
    },
    "Java": {
        "importance": "Industry-standard language for enterprise systems, microservices, and backend development.",
        "action_steps": [
            "Learn Core Java concepts: JVM architecture, memory management, and OOP principles.",
            "Practice the Java Collections Framework (ArrayList, HashMap, HashSet).",
            "Understand multithreading, exception handling, and JDBC database connectivity.",
            "Explore enterprise frameworks like Spring Boot and Hibernate for REST APIs."
        ],
        "project_idea": "Develop a RESTful CRUD application using Spring Boot and PostgreSQL.",
        "resources": "Java Programming MOOC (University of Helsinki), Baeldung Spring Tutorials"
    },
    "SQL": {
        "importance": "Essential database language for querying, aggregating, and managing relational databases.",
        "action_steps": [
            "Master essential queries: SELECT, WHERE, GROUP BY, HAVING, and ORDER BY.",
            "Practice table joins: INNER, LEFT, RIGHT, and FULL OUTER JOINs.",
            "Learn advanced analytical SQL: Subqueries, Window Functions (ROW_NUMBER, RANK, OVER), and CTEs.",
            "Understand database indexing, normalization (3NF), and query optimization."
        ],
        "project_idea": "Design an e-commerce database schema and write 20 analytical business queries.",
        "resources": "SQLZoo, Mode Analytics SQL Tutorial, LeetCode Database Problems"
    },
    "Git": {
        "importance": "Standard distributed version control system for software development collaboration.",
        "action_steps": [
            "Master local version control commands: git init, add, commit, status, and log.",
            "Practice branching workflows: git branch, checkout, switch, and merge.",
            "Learn remote repository collaboration: git remote, push, pull, and fetch.",
            "Understand resolving merge conflicts and writing conventional commit messages."
        ],
        "project_idea": "Create a multi-branch GitHub repository with a README, branch protections, and PR workflow.",
        "resources": "Pro Git Book (git-scm.com/book), GitHub Skills Interactive Labs"
    },
    "HTML_CSS": {
        "importance": "Foundational building blocks of web interfaces and frontend presentation.",
        "action_steps": [
            "Master semantic HTML5 elements: header, nav, main, section, article, and footer.",
            "Learn modern CSS layout systems: Flexbox and CSS Grid.",
            "Implement responsive design principles using CSS media queries and mobile-first design.",
            "Explore modern CSS utility frameworks like Tailwind CSS or Bootstrap."
        ],
        "project_idea": "Build a fully responsive personal portfolio website with dark/light mode toggle.",
        "resources": "MDN Web Docs (developer.mozilla.org), Frontend Mentor Challenges"
    },
    "JavaScript": {
        "importance": "Core interactive language for modern web development and full-stack frameworks.",
        "action_steps": [
            "Learn ES6+ syntax: let/const, arrow functions, template literals, and destructuring.",
            "Master DOM manipulation and event-driven architecture.",
            "Understand asynchronous programming: Promises, async/await, and Fetch API.",
            "Familiarize yourself with modern frontend frameworks (React, Vue, or Next.js)."
        ],
        "project_idea": "Create an interactive dashboard that fetches and visualizes data from a public REST API.",
        "resources": "javascript.info, MDN JavaScript Guide, Odin Project Web Development"
    },
    "Machine_Learning": {
        "importance": "Predictive modeling and algorithm development for intelligent automated systems.",
        "action_steps": [
            "Understand supervised vs. unsupervised learning concepts.",
            "Master Scikit-learn pipelines: data preprocessing, model training, cross-validation, and metrics.",
            "Learn core algorithms: Linear/Logistic Regression, Decision Trees, Random Forests, and SVMs.",
            "Understand hyperparameter tuning, preventing overfitting, and model deployment."
        ],
        "project_idea": "Build and evaluate an end-to-end classification model on a real-world dataset and deploy it.",
        "resources": "Scikit-Learn Official User Guide, Andrew Ng Machine Learning Specialization"
    },
    "Statistics": {
        "importance": "Theoretical foundation for data analysis, hypothesis testing, and machine learning.",
        "action_steps": [
            "Master descriptive statistics: mean, median, mode, variance, and standard deviation.",
            "Understand probability distributions: Normal, Binomial, Poisson, and Central Limit Theorem.",
            "Learn inferential statistics: hypothesis testing, p-values, t-tests, ANOVA, and Chi-Square tests.",
            "Apply statistical correlation and regression analysis to interpret data patterns."
        ],
        "project_idea": "Conduct an A/B testing analysis on a sample dataset and produce an executive findings report.",
        "resources": "StatQuest with Josh Starmer (YouTube), Khan Academy Statistics and Probability"
    },
    "Data_Visualization": {
        "importance": "Translating complex data metrics into intuitive, impactful visual charts.",
        "action_steps": [
            "Master Python plotting libraries: Matplotlib and Seaborn.",
            "Learn visual storytelling: choosing the right chart (scatter, boxplot, bar, line, heatmap).",
            "Learn business intelligence (BI) tools such as Power BI or Tableau.",
            "Practice dashboard layout, color theory, and executive summary presentation."
        ],
        "project_idea": "Build an interactive multi-page business metrics dashboard in Power BI or Tableau.",
        "resources": "Tableau Public Free Training, Microsoft Power BI Learning Path"
    },
    "Algorithms_OOP": {
        "importance": "Core computer science problem solving, system architecture, and code efficiency.",
        "action_steps": [
            "Master fundamental data structures: Arrays, Linked Lists, Stacks, Queues, Trees, and Hash Tables.",
            "Learn algorithm analysis: Big-O time and space complexity.",
            "Understand classic algorithms: Binary Search, Sorting (Merge, Quick), BFS, and DFS.",
            "Apply SOLID design principles and common Design Patterns (Factory, Singleton, Observer)."
        ],
        "project_idea": "Implement and benchmark classic data structures and search algorithms from scratch.",
        "resources": "NeetCode.io, GeeksforGeeks Data Structures & Algorithms, LeetCode Top 150"
    }
}

class RecommendationEngine:
    def __init__(self, db=RECOMMENDATION_DATABASE):
        self.db = db

    def generate(self, gap_analysis: dict) -> list:
        """
        Generates prioritized recommendations for missing and weak skills.
        """
        recommendations = []
        
        # Combine missing skills (highest priority) and weak skills
        priority_skills = []
        for item in gap_analysis.get("missing_skills", []):
            priority_skills.append({**item, "status": "Missing"})
        for item in gap_analysis.get("weak_skills", []):
            priority_skills.append({**item, "status": "Weak"})

        # Generate recommendation cards
        for skill_info in priority_skills:
            skill_name = skill_info["skill"]
            meta = self.db.get(skill_name, {
                "importance": "Critical industry skill.",
                "action_steps": [f"Learn {skill_name} fundamentals.", f"Practice {skill_name} exercises."],
                "project_idea": f"Build a project demonstrating {skill_name}.",
                "resources": "Online documentation and tutorials."
            })
            
            recommendations.append({
                "skill": skill_name,
                "status": skill_info["status"],
                "student_level": skill_info["student_level"],
                "required_level": skill_info["required_level"],
                "gap": skill_info["gap"],
                "importance": meta["importance"],
                "action_steps": meta["action_steps"],
                "project_idea": meta["project_idea"],
                "resources": meta["resources"]
            })

        return recommendations
