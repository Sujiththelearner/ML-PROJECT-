"""
Job Roles Knowledge Base
Contains detailed O*NET-aligned job descriptions, responsibilities,
required technical and soft skills, tools, interview topics, and project benchmarks.
"""

JOB_ROLES_CATALOG = {
    "Data Analyst": {
        "title": "Data Analyst",
        "onet_soc": "15-2051.01",
        "onet_title": "Business Intelligence Analysts",
        "mapped_model_career": "Data Analyst",
        "tagline": "Transform raw numbers into actionable business decisions and visual intelligence.",
        "description": "Data Analysts examine large datasets to identify market trends, create dashboards, streamline business operations, and assist leadership in making data-driven decisions.",
        "daily_tasks": [
            "Write analytical SQL queries to extract and aggregate business data from data warehouses.",
            "Clean and preprocess missing, inconsistent, or anomalous tabular data using Python or Excel.",
            "Design and maintain interactive BI executive dashboards in Power BI or Tableau.",
            "Conduct exploratory data analysis and basic statistical correlation tests.",
            "Translate quantitative findings into clear business presentations for non-technical stakeholders."
        ],
        "core_skills": ["SQL", "Python", "Excel", "Data Cleaning"],
        "technical_skills": ["Statistics", "Data Visualization", "ETL Pipelines", "Business Intelligence"],
        "soft_skills": ["Data Storytelling", "Critical Thinking", "Business Acumen", "Active Listening"],
        "common_tools": ["PostgreSQL / MySQL", "Power BI / Tableau", "Pandas & NumPy", "Jupyter Notebooks", "Advanced Excel"],
        "typical_projects": [
            "Sales & Revenue Performance Dashboard with drill-down metrics.",
            "Customer Churn Analysis & Segmentation model.",
            "E-commerce Inventory & Supply Chain Optimization Report."
        ],
        "interview_areas": [
            "Complex SQL Joins, Window Functions, and CTEs.",
            "Statistical concepts: Hypothesis testing, p-values, variance, distributions.",
            "Business case studies: interpreting metrics, identifying drop-offs.",
            "Data visualization best practices and storytelling."
        ],
        "entry_level_expectations": "Strong mastery of SQL, solid fundamentals in Python/Pandas, ability to create intuitive BI dashboards, and clear presentation of analytical insights."
    },
    "Data Scientist": {
        "title": "Data Scientist",
        "onet_soc": "15-2051.00",
        "onet_title": "Data Scientists",
        "mapped_model_career": "ML Engineer",
        "tagline": "Harness machine learning, statistical modeling, and algorithms to solve complex data challenges.",
        "description": "Data Scientists design mathematical models, apply machine learning algorithms, and derive predictive insights from high-dimensional, structured and unstructured datasets.",
        "daily_tasks": [
            "Perform comprehensive Exploratory Data Analysis (EDA) on multi-source datasets.",
            "Engineer novel features and normalize data distributions for algorithmic modeling.",
            "Train, fine-tune, and cross-validate predictive machine learning models.",
            "Evaluate model performance using Precision, Recall, ROC-AUC, and F1-score.",
            "Deploy models as REST API endpoints and monitor prediction drift."
        ],
        "core_skills": ["Python", "Machine Learning", "Statistics", "SQL"],
        "technical_skills": ["Feature Engineering", "Data Modeling", "Deep Learning basics", "Scikit-Learn"],
        "soft_skills": ["Research Mindset", "Experimental Rigor", "Problem Formulation", "Collaboration"],
        "common_tools": ["Scikit-Learn", "TensorFlow / PyTorch", "Pandas & SciPy", "Git / GitHub", "Docker"],
        "typical_projects": [
            "Predictive Healthcare Diagnosis classifier with cross-validation.",
            "Credit Card Fraud Detection using anomaly detection and class rebalancing.",
            "Customer Lifetime Value (CLV) regression and forecasting system."
        ],
        "interview_areas": [
            "Bias-Variance tradeoff, overfitting, and regularization techniques (L1/L2).",
            "Supervised vs. Unsupervised algorithms (Tree ensembles, Logistic regression, Clustering).",
            "Metrics selection: when to optimize Recall vs Precision.",
            "Coding challenges in Python (data structures and algorithmic manipulation)."
        ],
        "entry_level_expectations": "Deep understanding of machine learning algorithms, strong Python programming skills, practical experience with Scikit-learn pipelines, and at least 2 end-to-end portfolio projects."
    },
    "Machine Learning Engineer": {
        "title": "Machine Learning Engineer",
        "onet_soc": "15-2051.00",
        "onet_title": "Data Scientists / ML Engineers",
        "mapped_model_career": "ML Engineer",
        "tagline": "Build production-ready machine learning systems, automated pipelines, and scalable AI infrastructure.",
        "description": "Machine Learning Engineers bridge the gap between theoretical data science and software engineering, building automated pipelines that deploy and scale ML models in production.",
        "daily_tasks": [
            "Develop automated data ingestion, transformation, and training pipelines.",
            "Containerize machine learning services using Docker for cloud deployment.",
            "Optimize model inference latency, throughput, and memory consumption.",
            "Implement automated monitoring for model performance and data distribution drift.",
            "Write high-performance Python code adhering to OOP and clean code standards."
        ],
        "core_skills": ["Python", "Machine Learning", "Algorithms & OOP", "Git"],
        "technical_skills": ["MLOps & Pipelines", "Model Deployment", "Docker & Cloud APIs", "Linear Algebra"],
        "soft_skills": ["System Architecture", "Continuous Learning", "Debugging", "Teamwork"],
        "common_tools": ["FastAPI / Flask", "Docker", "MLflow / DVC", "PyTorch / TensorFlow", "AWS / GCP"],
        "typical_projects": [
            "Production-ready NLP Sentiment Analyzer deployed as a containerized REST API.",
            "Real-time Computer Vision Object Detection service with inference monitoring.",
            "Automated CI/CD pipeline for model retraining and validation."
        ],
        "interview_areas": [
            "ML system design: designing scalable inference pipelines.",
            "Object-oriented software development in Python.",
            "Model deployment, containerization with Docker, and API construction.",
            "Data structures and algorithmic complexity (Big-O notation)."
        ],
        "entry_level_expectations": "Strong Python OOP foundations, practical experience deploying models with FastAPI/Docker, solid grasp of ML algorithms, and version-controlled Git repositories."
    },
    "Software Developer": {
        "title": "Software Developer",
        "onet_soc": "15-1252.00",
        "onet_title": "Software Developers",
        "mapped_model_career": "Software Developer",
        "tagline": "Engineer robust software applications, design reliable architectures, and solve algorithmic challenges.",
        "description": "Software Developers design, build, test, and maintain computer software, web services, desktop applications, and backend systems that power modern digital services.",
        "daily_tasks": [
            "Write clean, modular, and maintainable code adhering to SOLID design principles.",
            "Implement algorithms and data structures to optimize software performance.",
            "Participate in code reviews, write unit tests, and resolve edge-case bugs.",
            "Manage code versions, branches, and releases using Git and GitHub workflows.",
            "Collaborate with cross-functional teams to design database schemas and API contracts."
        ],
        "core_skills": ["Algorithms & OOP", "Git", "Python or Java", "SQL"],
        "technical_skills": ["System Design", "Unit Testing", "REST APIs", "Debugging"],
        "soft_skills": ["Problem Solving", "Code Readability", "Communication", "Time Management"],
        "common_tools": ["VS Code / IntelliJ", "Git / GitHub", "Postman", "Linux Command Line", "Docker"],
        "typical_projects": [
            "Task & Project Management System with multi-user authentication and database persistence.",
            "Distributed File Sharing / Storage Microservice.",
            "High-throughput URL Shortener with caching and analytics."
        ],
        "interview_areas": [
            "Data Structures: Trees, Graphs, Hash Maps, Stacks, Queues.",
            "Algorithms: Sorting, Binary Search, Dynamic Programming, BFS/DFS.",
            "OOP Concepts: Encapsulation, Polymorphism, Inheritance, Abstraction.",
            "Database normalization and basic system design trade-offs."
        ],
        "entry_level_expectations": "Fluency in at least one major language (Java, Python, C++), strong DSA foundations for technical coding interviews, and version-controlled GitHub projects."
    },
    "Java Developer": {
        "title": "Java Developer",
        "onet_soc": "15-1251.00",
        "onet_title": "Computer Programmers (Java Specialization)",
        "mapped_model_career": "Java Developer",
        "tagline": "Architect enterprise-grade backend systems, microservices, and robust Java services.",
        "description": "Java Developers specialize in architecting server-side enterprise applications, microservices, transactional backend workflows, and scalable banking/enterprise platforms using the Java ecosystem.",
        "daily_tasks": [
            "Develop server-side business logic and RESTful microservices using Spring Boot.",
            "Design relational database schemas and write optimized JPA/Hibernate queries.",
            "Implement secure authentication, role-based authorization, and token management.",
            "Write automated unit and integration tests using JUnit and Mockito.",
            "Debug JVM performance, thread safety, and memory management issues."
        ],
        "core_skills": ["Java", "Algorithms & OOP", "SQL", "Git"],
        "technical_skills": ["Spring Boot", "Hibernate / JPA", "RESTful Architecture", "Relational Databases"],
        "soft_skills": ["Attention to Detail", "Architectural Thinking", "Resilience", "Documentation"],
        "common_tools": ["IntelliJ IDEA / Eclipse", "Spring Boot", "Maven / Gradle", "PostgreSQL / MySQL", "Postman"],
        "typical_projects": [
            "Enterprise Banking & Transaction Management API with JWT security.",
            "E-Commerce Microservices Platform with Spring Cloud and PostgreSQL.",
            "Hospital Management & Appointment Booking Backend."
        ],
        "interview_areas": [
            "Core Java: Collections Framework, Multithreading, Exception Handling, Memory Model.",
            "Spring Framework: Dependency Injection, Inversion of Control, Spring MVC, Spring Data JPA.",
            "OOP and SOLID Design Principles with real code examples.",
            "SQL query optimization and database transactions (ACID properties)."
        ],
        "entry_level_expectations": "Proficiency in Core Java (Collections, Streams, Multithreading), experience building a Spring Boot REST API, and working knowledge of SQL databases."
    },
    "Web Developer": {
        "title": "Web Developer",
        "onet_soc": "15-1254.00",
        "onet_title": "Web Developers",
        "mapped_model_career": "Web Developer",
        "tagline": "Craft responsive web applications, modern interactive user experiences, and dynamic frontend portals.",
        "description": "Web Developers create visually compelling, responsive, and high-performance websites and web applications, bridging the gap between graphical design and technical implementation.",
        "daily_tasks": [
            "Build responsive and accessible user interfaces using semantic HTML5 and modern CSS3.",
            "Develop dynamic client-side interactions and state management using JavaScript.",
            "Integrate third-party RESTful APIs and handle asynchronous data requests.",
            "Optimize web performance, browser compatibility, and mobile responsiveness.",
            "Collaborate with UI/UX designers to translate Figma mockups into clean frontend code."
        ],
        "core_skills": ["HTML & CSS", "JavaScript", "Git", "Responsive Design"],
        "technical_skills": ["Frontend Frameworks (React/Vue)", "Web APIs", "CSS Grid/Flexbox", "DOM Manipulation"],
        "soft_skills": ["Visual Aesthetics", "User Empathy", "Attention to Detail", "Communication"],
        "common_tools": ["VS Code", "Chrome DevTools", "Figma", "npm / Vite", "Git / GitHub"],
        "typical_projects": [
            "Interactive Weather & Air Quality Dashboard with geolocation and live APIs.",
            "Fully Responsive Portfolio & Blog Website with dark/light theme switching.",
            "Interactive Quiz & Assessment Platform with dynamic state management."
        ],
        "interview_areas": [
            "HTML5 semantic tags, accessibility (a11y), and SEO basics.",
            "CSS layout systems: Flexbox, CSS Grid, media queries, and specificity.",
            "JavaScript ES6+: Promises, async/await, closures, event loop, DOM events.",
            "State management, component lifecycle, and REST API consumption."
        ],
        "entry_level_expectations": "Mastery of HTML5/CSS3/JavaScript, solid experience with responsive design, ability to consume REST APIs, and a live deployed web portfolio."
    },
    "Full Stack Developer": {
        "title": "Full Stack Developer",
        "onet_soc": "15-1252.00",
        "onet_title": "Software Developers (Full Stack)",
        "mapped_model_career": "Software Developer",
        "tagline": "Master both client-side interfaces and server-side architectures to build complete digital products.",
        "description": "Full Stack Developers possess cross-disciplinary expertise across frontend interfaces, backend application servers, databases, and deployment pipelines to deliver complete web applications.",
        "daily_tasks": [
            "Design responsive user interfaces on the frontend and connect them to backend endpoints.",
            "Develop server-side business logic, authentication, and database schemas.",
            "Architect and consume RESTful APIs with structured request/response validation.",
            "Manage application state across frontend clients and backend relational databases.",
            "Deploy full-stack applications to cloud hosting platforms."
        ],
        "core_skills": ["JavaScript", "HTML & CSS", "SQL", "Git", "Python or Java"],
        "technical_skills": ["Full Stack Frameworks", "API Development", "Database Modeling", "Algorithms & OOP"],
        "soft_skills": ["Versatility", "Problem Solving", "Holistic Vision", "Product Mindset"],
        "common_tools": ["React / Next.js", "Node.js / Express or Django", "PostgreSQL", "Git / GitHub", "Vercel / Render"],
        "typical_projects": [
            "Full Stack E-Learning Portal with video player, quizzes, and user profiles.",
            "Real-time Collaborative Whiteboard & Chat application with WebSockets.",
            "Student Career Mentorship Platform with booking schedules and reviews."
        ],
        "interview_areas": [
            "Frontend vs Backend architecture and data synchronization.",
            "RESTful API design conventions, status codes, and security (CORS, JWT).",
            "Database normalization, querying, and schema design.",
            "Handling asynchronous programming across client and server."
        ],
        "entry_level_expectations": "Demonstrated ability to build, connect, and deploy a complete full-stack web application with database persistence and user authentication."
    },
    "Backend Developer": {
        "title": "Backend Developer",
        "onet_soc": "15-1252.00",
        "onet_title": "Software Developers (Backend)",
        "mapped_model_career": "Software Developer",
        "tagline": "Build secure server architectures, high-performance APIs, and data storage systems.",
        "description": "Backend Developers build the invisible engine powering digital platforms: data models, server algorithms, authentication services, third-party integrations, and database performance.",
        "daily_tasks": [
            "Design, code, and test robust RESTful and GraphQL APIs.",
            "Model relational and non-relational database schemas.",
            "Implement security protocols, encryption, and secure authorization mechanisms.",
            "Optimize backend database queries to minimize latency and memory usage.",
            "Write comprehensive integration tests for backend services."
        ],
        "core_skills": ["Python or Java", "SQL", "Algorithms & OOP", "Git"],
        "technical_skills": ["API Architecture", "Database Optimization", "Server Security", "Data Modeling"],
        "soft_skills": ["Logical Rigor", "Patience", "Security Consciousness", "System Thinking"],
        "common_tools": ["FastAPI / Django or Spring Boot", "PostgreSQL", "Redis", "Docker", "Postman"],
        "typical_projects": [
            "High-Performance Authentication & Role-Based Access Control (RBAC) Microservice.",
            "Event Booking & Ticketing Backend with concurrent seat reservation handling.",
            "Automated Notification & Email Dispatching Service with job queues."
        ],
        "interview_areas": [
            "Database indexing, transactions, and ACID principles.",
            "RESTful design principles, caching strategies (Redis), and rate limiting.",
            "Object-Oriented Programming and design patterns.",
            "API authentication (JWT, OAuth) and server error handling."
        ],
        "entry_level_expectations": "Fluency in a backend language (Python, Java, Node.js), strong SQL capabilities, ability to construct tested REST APIs, and understanding of database transactions."
    },
    "Frontend Developer": {
        "title": "Frontend Developer",
        "onet_soc": "15-1254.00",
        "onet_title": "Web Developers (Frontend)",
        "mapped_model_career": "Web Developer",
        "tagline": "Transform designs into fluid, responsive, accessible, and interactive user interfaces.",
        "description": "Frontend Developers specialize in crafting client-side visual interfaces, optimizing web performance, handling component state, and providing delightful user experiences across all devices.",
        "daily_tasks": [
            "Construct modern modular UI components using React, Vue, or modern JavaScript.",
            "Implement responsive mobile-first layouts using CSS Grid and Flexbox.",
            "Manage client-side application state and cache server responses.",
            "Ensure digital accessibility (WCAG compliance) and cross-browser stability.",
            "Profile web vital metrics to ensure sub-second page loads."
        ],
        "core_skills": ["HTML & CSS", "JavaScript", "Git", "Responsive Design"],
        "technical_skills": ["React / Modern Frameworks", "Component State Management", "CSS Systems", "Web Performance"],
        "soft_skills": ["Design Sensitivity", "User Empathy", "Precision", "Communication"],
        "common_tools": ["React", "Tailwind CSS", "TypeScript basics", "Vite", "Figma"],
        "typical_projects": [
            "Interactive SaaS Analytics Dashboard with customizable theme widgets.",
            "Streaming Movie Browser interface with debounced search and filtering.",
            "Accessible E-Commerce Product Catalog with cart drawer and checkout flow."
        ],
        "interview_areas": [
            "DOM event bubbling, delegation, and performance optimization.",
            "Component lifecycle, hooks, and state management in modern frameworks.",
            "CSS layout techniques (Flexbox vs Grid) and responsive media queries.",
            "Web accessibility (ARIA roles) and core web vitals."
        ],
        "entry_level_expectations": "Strong mastery of HTML/CSS/JavaScript, demonstrable proficiency with a modern framework like React, and a clean GitHub portfolio of live deployed projects."
    },
    "Cloud Engineer": {
        "title": "Cloud Engineer",
        "onet_soc": "15-1299.08",
        "onet_title": "Computer Systems Engineers (Cloud Infrastructure)",
        "mapped_model_career": "Software Developer",
        "tagline": "Architect, provision, and maintain resilient cloud infrastructure and distributed networks.",
        "description": "Cloud Engineers design, deploy, and monitor scalable cloud environments on major providers (AWS, GCP, Azure), ensuring high availability, security, and disaster recovery.",
        "daily_tasks": [
            "Provision and configure cloud computing instances, storage buckets, and virtual networks.",
            "Write Infrastructure-as-Code (IaC) scripts using Terraform or CloudFormation.",
            "Configure cloud security policies, IAM roles, and encryption keys.",
            "Monitor system health, cloud resource utilization, and cost optimization.",
            "Automate recurring backup, scaling, and recovery workflows."
        ],
        "core_skills": ["Git", "Python", "Linux Command Line", "Networking"],
        "technical_skills": ["AWS / Azure / GCP", "Infrastructure as Code", "Cloud Security", "Docker"],
        "soft_skills": ["Operational Discipline", "Risk Management", "Troubleshooting", "Documentation"],
        "common_tools": ["AWS Management Console / CLI", "Docker", "Terraform", "Linux (Ubuntu/CentOS)", "GitHub Actions"],
        "typical_projects": [
            "Automated Multi-Tier Web Application Infrastructure deployed with Terraform on AWS.",
            "Serverless Image Processing Pipeline utilizing cloud functions and storage triggers.",
            "Secure Virtual Private Cloud (VPC) with public and private subnets."
        ],
        "interview_areas": [
            "Cloud fundamentals: IaaS vs PaaS vs SaaS, High Availability, Load Balancing.",
            "Cloud security: IAM policies, security groups, public/private subnets.",
            "Basic Linux system administration and bash scripting.",
            "Containerization fundamentals and basic cloud networking (CIDR, DNS, VPC)."
        ],
        "entry_level_expectations": "Foundational cloud certification (e.g., AWS Certified Cloud Practitioner / Solutions Architect Associate), Linux familiarity, and basic scripting skills."
    },
    "DevOps Engineer": {
        "title": "DevOps Engineer",
        "onet_soc": "15-1252.00",
        "onet_title": "Software Developers (DevOps)",
        "mapped_model_career": "Software Developer",
        "tagline": "Unify development and IT operations through continuous integration, automation, and reliability.",
        "description": "DevOps Engineers build automated CI/CD pipelines, containerize applications, manage deployment environments, and foster seamless collaboration between development and operations teams.",
        "daily_tasks": [
            "Build and maintain automated CI/CD build and test pipelines.",
            "Package application microservices into standardized Docker containers.",
            "Automate deployment workflows to staging and production clusters.",
            "Implement centralized logging, metrics dashboards, and alert triggers.",
            "Collaborate with developers to eliminate environment discrepancies."
        ],
        "core_skills": ["Git", "Linux Command Line", "Python or Bash", "Docker"],
        "technical_skills": ["CI/CD Pipelines", "Container Orchestration", "Monitoring & Logging", "Cloud Basics"],
        "soft_skills": ["Collaboration", "Automation Mindset", "Quick Debugging", "Patience"],
        "common_tools": ["GitHub Actions", "Docker", "Kubernetes basics", "Linux", "Prometheus / Grafana"],
        "typical_projects": [
            "End-to-End Automated CI/CD Pipeline deploying a web service to cloud on Git push.",
            "Containerized Microservices Stack managed via Docker Compose.",
            "Automated Server Health Monitoring dashboard with Grafana."
        ],
        "interview_areas": [
            "Continuous Integration vs Continuous Delivery (CI/CD) pipelines.",
            "Docker commands, Dockerfiles, and multi-stage builds.",
            "Git branching strategies (Gitflow, trunk-based development).",
            "Linux permissions, process management, and shell scripting."
        ],
        "entry_level_expectations": "Hands-on experience with Docker, automated CI/CD in GitHub Actions, comfortable with Linux CLI, and basic scripting."
    },
    "Database Administrator": {
        "title": "Database Administrator",
        "onet_soc": "15-1242.00",
        "onet_title": "Database Administrators",
        "mapped_model_career": "Data Analyst",
        "tagline": "Protect database integrity, optimize performance, and manage enterprise data architectures.",
        "description": "Database Administrators ensure corporate databases operate reliably, securely, and with high throughput, overseeing backups, permissions, query indexing, and data recovery.",
        "daily_tasks": [
            "Monitor and optimize database server performance and query execution plans.",
            "Implement automated backup routines and verify disaster recovery protocols.",
            "Manage user permissions, roles, and compliance with data privacy regulations.",
            "Design and refactor relational database schemas and indexing structures.",
            "Troubleshoot database deadlocks, slow queries, and storage capacity limits."
        ],
        "core_skills": ["SQL", "Data Modeling", "Git", "Linux Basics"],
        "technical_skills": ["Query Indexing & Optimization", "Database Administration", "Backup & Recovery", "Security"],
        "soft_skills": ["Precision", "Responsibility", "Calmness Under Pressure", "Communication"],
        "common_tools": ["PostgreSQL", "MySQL", "Oracle DB / SQL Server", "pgAdmin / DBeaver", "Linux CLI"],
        "typical_projects": [
            "Database Schema Design, Optimization, and Index Tuning for a High-Volume Store.",
            "Automated Database Backup and Point-in-Time Recovery Simulation script.",
            "Database Migration & ETL pipeline between legacy schemas."
        ],
        "interview_areas": [
            "Query execution plans, B-Tree indexes, and performance bottlenecks.",
            "ACID transactions, locking levels, and concurrency control.",
            "Database normalization up to BCNF and denormalization trade-offs.",
            "High availability strategies (replication, clustering, failover)."
        ],
        "entry_level_expectations": "Expert-level SQL query writing, solid grasp of database administration tasks (backups, indexes, permissions), and understanding of relational theory."
    },
    "Business Analyst": {
        "title": "Business Analyst",
        "onet_soc": "13-1111.00",
        "onet_title": "Management Analysts / Business Analysts",
        "mapped_model_career": "Data Analyst",
        "tagline": "Bridge business objectives and technology solutions through requirements analysis and data.",
        "description": "Business Analysts evaluate organizational processes, analyze business metrics, document technical requirements, and guide software teams in delivering high-value solutions.",
        "daily_tasks": [
            "Gather, clarify, and document business requirements from executive stakeholders.",
            "Analyze business performance metrics and identify workflow bottlenecks.",
            "Formulate functional specifications, user stories, and acceptance criteria.",
            "Create process flow diagrams, wireframes, and business dashboards.",
            "Facilitate communication between business leaders and technical engineering teams."
        ],
        "core_skills": ["SQL", "Excel", "Data Visualization", "Process Modeling"],
        "technical_skills": ["Business Intelligence", "Requirements Engineering", "Basic Statistics", "Agile/Scrum"],
        "soft_skills": ["Stakeholder Management", "Negotiation", "Clear Communication", "Critical Thinking"],
        "common_tools": ["Advanced Excel", "Power BI / Tableau", "SQL", "Jira / Confluence", "Lucidchart / Visio"],
        "typical_projects": [
            "Business Process Re-engineering & Optimization analysis for customer onboarding.",
            "Product KPI & User Retention Dashboard with executive recommendations.",
            "Comprehensive Software Requirements Specification (SRS) for an enterprise app."
        ],
        "interview_areas": [
            "Translating ambiguous business problems into structured technical requirements.",
            "User stories, acceptance criteria, and Agile sprint workflows.",
            "Data interpretation and storytelling using Excel/SQL/Power BI.",
            "Stakeholder conflict resolution and requirement prioritization."
        ],
        "entry_level_expectations": "Strong analytical problem-solving skills, proficiency in Excel and basic SQL, clear documentation abilities, and good presentation skills."
    },
    "Cybersecurity Analyst": {
        "title": "Cybersecurity Analyst",
        "onet_soc": "15-1212.00",
        "onet_title": "Information Security Analysts",
        "mapped_model_career": "Software Developer",
        "tagline": "Defend networks, detect vulnerabilities, and protect digital assets from cyber threats.",
        "description": "Cybersecurity Analysts monitor computer networks and systems for security breaches, investigate malicious activities, assess vulnerabilities, and implement defensive security measures.",
        "daily_tasks": [
            "Monitor network traffic and security event logs using SIEM tools.",
            "Conduct vulnerability scans and assess system security weaknesses.",
            "Investigate and document security incidents, malware attempts, and anomalies.",
            "Configure firewalls, access controls, and endpoint protection solutions.",
            "Advise engineering teams on secure coding standards and patch management."
        ],
        "core_skills": ["Linux Basics", "Networking Fundamentals", "Python or Bash", "Git"],
        "technical_skills": ["Network Security", "Vulnerability Assessment", "SIEM & Log Analysis", "Incident Response"],
        "soft_skills": ["Vigilance", "Ethical Integrity", "Investigation", "Communication"],
        "common_tools": ["Wireshark", "Nmap", "Linux (Kali / Ubuntu)", "Splunk / ELK", "Metasploit basics"],
        "typical_projects": [
            "Network Traffic Analysis & Intrusion Detection Report using Wireshark.",
            "Automated Vulnerability Scanner & Port Audit script in Python.",
            "Comprehensive Security Policy and Incident Response Plan for an organization."
        ],
        "interview_areas": [
            "OSI model, TCP/IP handshake, and common network protocols (DNS, HTTP, SSH).",
            "Common web vulnerabilities (OWASP Top 10: SQLi, XSS, CSRF).",
            "Symmetric vs. Asymmetric encryption, hashing, and digital certificates.",
            "Steps in incident response and security monitoring."
        ],
        "entry_level_expectations": "Solid understanding of networking concepts and the OSI model, familiarity with Linux security tools, and foundational certifications (Security+, CEH, or Network+)."
    }
}

def get_job_role_info(target_job_name: str) -> dict:
    """
    Returns the knowledge base dictionary for a target job.
    Falls back gracefully if 'Other' or an uncataloged role is entered.
    """
    if target_job_name in JOB_ROLES_CATALOG:
        return JOB_ROLES_CATALOG[target_job_name]
    
    # Generic fallback for custom / 'Other' roles
    return {
        "title": target_job_name,
        "onet_soc": "15-1299.00",
        "onet_title": "Computer Occupations, All Other",
        "mapped_model_career": "Software Developer",
        "tagline": f"Technical specialist focused on {target_job_name}.",
        "description": f"A specialized role dedicated to technical implementation, problem solving, and domain engineering within {target_job_name}.",
        "daily_tasks": [
            "Analyze technical requirements and design domain solutions.",
            "Apply programming languages, database queries, and tools to solve problems.",
            "Collaborate with team members to test, review, and deploy projects.",
            "Continuously learn new frameworks and industry tools."
        ],
        "core_skills": ["Algorithms & OOP", "Git", "SQL", "Python"],
        "technical_skills": ["Domain Tools", "Software Architecture", "Problem Solving", "Testing"],
        "soft_skills": ["Communication", "Critical Thinking", "Adaptability", "Teamwork"],
        "common_tools": ["VS Code", "Git / GitHub", "SQL Database", "Command Line"],
        "typical_projects": [
            f"End-to-End portfolio project demonstrating practical {target_job_name} capabilities."
        ],
        "interview_areas": [
            "Technical fundamentals in programming and system design.",
            "Past project architecture and technical challenges overcome.",
            "Problem-solving and behavioral alignment."
        ],
        "entry_level_expectations": "Strong fundamentals, demonstrated problem-solving skills, and real project evidence."
    }
