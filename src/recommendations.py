"""
Phase 16: Recommendation Engine (Enhanced)
Generates personalized, structured recommendations categorized into:
- 📚 Learn
- 🛠 Practice
- 💻 Build
- 📜 Certify
- 🎤 Interview Preparation
Also generates dynamic 5-phase Learning Roadmaps and Prioritized Focus Areas.
"""

try:
    from src.job_roles_data import get_job_role_info
except ImportError:
    from job_roles_data import get_job_role_info

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
        "resources": "Official Python Docs (docs.python.org), freeCodeCamp Python Certification",
        "certifications": ["PCEP - Certified Entry-Level Python Programmer", "Google IT Automation with Python"],
        "practice": "HackerRank Python Track, LeetCode Easy Python Strings & Arrays",
        "interview_prep": "Python GIL, list comprehensions vs generators, decorators, memory management"
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
        "resources": "Java Programming MOOC (University of Helsinki), Baeldung Spring Tutorials",
        "certifications": ["Oracle Certified Professional: Java SE Developer", "Spring Certified Professional"],
        "practice": "LeetCode Java Top 100, Exercism Java Track",
        "interview_prep": "JVM memory model (Stack vs Heap), Garbage Collection, HashMaps internal working, Thread synchronization"
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
        "resources": "SQLZoo, Mode Analytics SQL Tutorial, LeetCode Database Problems",
        "certifications": ["Oracle Database SQL Certified Associate", "PostgreSQL Certified Associate"],
        "practice": "LeetCode 50 SQL Study Plan, HackerRank SQL Challenges",
        "interview_prep": "Window functions vs GROUP BY, Index optimization, ACID properties, solving second-highest salary query"
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
        "resources": "Pro Git Book (git-scm.com/book), GitHub Skills Interactive Labs",
        "certifications": ["GitHub Foundations Certification"],
        "practice": "LearnGitBranching interactive visual sandbox",
        "interview_prep": "Git merge vs rebase, resolving merge conflicts, git stash and reset vs revert"
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
        "resources": "MDN Web Docs (developer.mozilla.org), Frontend Mentor Challenges",
        "certifications": ["freeCodeCamp Responsive Web Design Certification", "Meta Front-End Developer"],
        "practice": "Frontend Mentor Challenges, CSSBattle.dev",
        "interview_prep": "CSS Box Model, Flexbox vs Grid, CSS specificity rules, responsive units (rem, em, vh, vw)"
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
        "resources": "javascript.info, MDN JavaScript Guide, Odin Project Web Development",
        "certifications": ["OpenJS Certified JavaScript Developer (JSNAD)", "Meta React Native / React Certificate"],
        "practice": "JavaScript30 by Wes Bos, LeetCode JavaScript 30-Day Challenge",
        "interview_prep": "Event Loop, Closures, Prototypal Inheritance, Asynchronous execution (Promises vs async/await)"
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
        "resources": "Scikit-Learn Official User Guide, Andrew Ng Machine Learning Specialization",
        "certifications": ["DeepLearning.AI Machine Learning Specialization", "TensorFlow Developer Certificate"],
        "practice": "Kaggle Competitions and Micro-courses",
        "interview_prep": "Overfitting vs Underfitting, Bias-Variance tradeoff, Precision vs Recall tradeoffs, Random Forest mechanics"
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
        "resources": "StatQuest with Josh Starmer (YouTube), Khan Academy Statistics and Probability",
        "certifications": ["Stanford Online Probability and Statistics", "IBM Data Science Professional Certificate"],
        "practice": "Khan Academy Practice Sets, Kaggle Statistics Notebooks",
        "interview_prep": "p-value interpretation, Type I vs Type II errors, Central Limit Theorem, confidence intervals"
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
        "resources": "Tableau Public Free Training, Microsoft Power BI Learning Path",
        "certifications": ["Microsoft Certified: Power BI Data Analyst Associate (PL-300)", "Tableau Desktop Specialist"],
        "practice": "MakeoverMonday datasets, Workout Wednesday Tableau challenges",
        "interview_prep": "Choosing the right visualization for distribution vs trend, DAX calculated columns vs measures"
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
        "resources": "NeetCode.io, GeeksforGeeks Data Structures & Algorithms, LeetCode Top 150",
        "certifications": ["HackerRank Problem Solving Intermediate"],
        "practice": "NeetCode 150 roadmap, LeetCode Blind 75",
        "interview_prep": "Time & space complexity of common operations, Tree traversals, Graph BFS/DFS, SOLID principles"
    }
}

class RecommendationEngine:
    def __init__(self, db=RECOMMENDATION_DATABASE):
        self.db = db

    def generate_categorized_recommendations(self, gap_analysis: dict, user_profile: dict) -> dict:
        """
        Structures recommendations into the 5 core requested categories:
        - 📚 Learn
        - 🛠 Practice
        - 💻 Build
        - 📜 Certify
        - 🎤 Interview Preparation
        """
        target_role = gap_analysis.get("target_career", "Software Developer")
        role_info = gap_analysis.get("role_info", get_job_role_info(target_role))
        
        weak_and_missing = gap_analysis.get("weak_skills", []) + gap_analysis.get("missing_skills", [])
        
        # Priority gap skills (up to 4 key areas)
        priority_skills = [item["skill"] for item in weak_and_missing[:4]]
        if not priority_skills:
            # If no gaps, recommend next-level advanced skills for the role
            priority_skills = ["Algorithms_OOP", "Git"]

        learn_items = []
        practice_items = []
        build_items = []
        certify_items = []
        interview_items = []

        # 1. Learn items (Core concepts for gaps)
        for s in priority_skills:
            meta = self.db.get(s, {})
            steps = meta.get("action_steps", [])
            if steps:
                learn_items.append({
                    "skill": s,
                    "title": f"Master {s} Fundamentals & Core Techniques",
                    "details": steps[:2]
                })

        # 2. Practice items
        for s in priority_skills:
            meta = self.db.get(s, {})
            practice_items.append({
                "skill": s,
                "platform": meta.get("practice", f"Coding and query practice for {s}"),
                "focus": meta.get("action_steps", ["Practice daily"])[-1]
            })

        # 3. Build items (Capstone project tailored to target job)
        typical_projs = role_info.get("typical_projects", [])
        for idx, proj in enumerate(typical_projs[:2]):
            build_items.append({
                "title": proj,
                "scope": f"Capstone portfolio project demonstrating {target_role} competencies.",
                "tools": ", ".join(role_info.get("common_tools", ["Git", "Python"]))
            })
        for s in priority_skills[:2]:
            meta = self.db.get(s, {})
            build_items.append({
                "title": meta.get("project_idea", f"Hands-on {s} application"),
                "scope": f"Targeted project to eliminate your {s} gap.",
                "tools": s
            })

        # 4. Certify items
        for s in priority_skills[:3]:
            meta = self.db.get(s, {})
            certs = meta.get("certifications", [f"Industry Certification in {s}"])
            for c in certs:
                certify_items.append({
                    "skill": s,
                    "certificate_name": c,
                    "provider": meta.get("resources", "Accredited provider")
                })

        # 5. Interview Preparation
        role_interviews = role_info.get("interview_areas", [])
        for topic in role_interviews:
            interview_items.append({
                "topic": topic,
                "category": f"{target_role} Technical Assessment"
            })
        for s in priority_skills[:2]:
            meta = self.db.get(s, {})
            interview_items.append({
                "topic": meta.get("interview_prep", f"Core conceptual questions in {s}"),
                "category": f"{s} Technical Screening"
            })

        return {
            "learn": learn_items,
            "practice": practice_items,
            "build": build_items,
            "certify": certify_items,
            "interview": interview_items
        }

    def generate_focus_areas(self, gap_analysis: dict, user_profile: dict) -> list:
        """
        Identifies top 4-5 focus areas with specific rationale.
        """
        target_role = gap_analysis.get("target_career", "Software Developer")
        weak_and_missing = gap_analysis.get("missing_skills", []) + gap_analysis.get("weak_skills", [])
        
        focus_list = []
        for item in weak_and_missing[:4]:
            skill = item["skill"]
            gap = item["gap"]
            why = item["why_required"]
            focus_list.append({
                "area": skill,
                "urgency": "High Priority" if item in gap_analysis.get("missing_skills", []) else "Moderate Priority",
                "gap": gap,
                "why": f"{why} This is critical to reaching the industry requirement for {target_role}."
            })
            
        focus_list.append({
            "area": "Portfolio Capstone Projects",
            "urgency": "High Priority",
            "gap": 0.0,
            "why": f"Employers in {target_role} prioritize live GitHub repositories and demonstrated project experience over credentials alone."
        })
        return focus_list

    def generate_learning_roadmap(self, gap_analysis: dict, user_profile: dict) -> list:
        """
        Generates dynamic 5-phase sequential learning roadmap based on target job & gaps.
        """
        target_role = gap_analysis.get("target_career", "Software Developer")
        role_info = gap_analysis.get("role_info", get_job_role_info(target_role))
        
        core_skills_str = ", ".join(role_info.get("core_skills", ["Core Programming", "SQL"]))
        tech_skills_str = ", ".join(role_info.get("technical_skills", ["Tools", "Frameworks"]))
        tools_str = ", ".join(role_info.get("common_tools", ["Git", "Databases"])[:3])
        projs_str = role_info.get("typical_projects", ["Capstone Portfolio Project"])[0]

        roadmap = [
            {
                "phase": "PHASE 1",
                "title": "Strengthen Core Fundamentals",
                "skills": core_skills_str,
                "goal": "Build robust syntactic and algorithmic mastery without relying on tutorials.",
                "duration": "Weeks 1–3"
            },
            {
                "phase": "PHASE 2",
                "title": "Role-Specific Technical Skills",
                "skills": tech_skills_str,
                "goal": f"Master the primary methodologies and packages needed for a {target_role}.",
                "duration": "Weeks 4–7"
            },
            {
                "phase": "PHASE 3",
                "title": "Applied Tools & Frameworks",
                "skills": tools_str,
                "goal": "Gain fluency with the industry tools and development environments used daily on the job.",
                "duration": "Weeks 8–10"
            },
            {
                "phase": "PHASE 4",
                "title": "Build Portfolio Capstone Projects",
                "skills": projs_str,
                "goal": "Construct 2 complete, well-documented, version-controlled GitHub repositories.",
                "duration": "Weeks 11–13"
            },
            {
                "phase": "PHASE 5",
                "title": "Career Readiness & Interview Preparation",
                "skills": "Resume tailoring, LinkedIn profile, LeetCode / SQL challenges, Mock interviews",
                "goal": "Master technical interview questions, case studies, and behavioral communication.",
                "duration": "Weeks 14–16"
            }
        ]
        return roadmap
