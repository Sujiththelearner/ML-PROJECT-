# Skill Gap Analyzer – AI-Powered Career Intelligence Platform

**Department:** Computer Science and Engineering (CSE)

---

## 📌 Project Overview
The **Skill Gap Analyzer** is an AI-powered career intelligence and skill-gap recommendation platform designed to guide engineering students toward career readiness.

Unlike basic numerical rating forms where students arbitrarily guess their proficiency (e.g. "Python: 3.5"), this platform evaluates **qualitative evidence**:
* Practical experience levels (Academic projects, Personal projects, Internships, Professional work)
* Concrete project portfolios and technical descriptions
* Verified certifications & uploaded certificate documents (PDF, PNG, JPG)
* Target job role alignment across 15+ industry careers

The platform employs a **calibrated feature-engineering layer** connected to a **Machine Learning classifier** trained on empirical benchmarks from the **U.S. Department of Labor (O*NET 28.0 Database)**.

---

## 🏛️ End-to-End System Architecture

```text
    Qualitative Profile Input (Experience, Projects, Certs, Target Job)
                                │
                                ▼
              Uploaded Certificate Parser (pypdf & PIL)
          (Extracts Organization, Title, Domain, Technologies)
                                │
                                ▼
               Backend Feature Engineering Layer
     (Translates qualitative evidence into model-compatible features)
                                │
                                ▼
         Trained Machine Learning Model (Logistic Regression, 98.33% Acc)
                                │
                                ▼
           O*NET Standard Occupational Classification Benchmark
                                │
                                ▼
              Qualitative Skill Gap Analysis
        (🟢 Already Demonstrated, 🟡 Needs Improvement, 🔴 Not Yet Demonstrated)
                                │
                                ▼
       Personalized 5-Category Recommendations & Dynamic 5-Phase Roadmap
       (📚 Learn, 🛠 Practice, 💻 Build, 📜 Certify, 🎤 Interview Prep)
```

---

## 🎯 Target Career Roles (O*NET Aligned)

| Career Role | O*NET-SOC Code | Official O*NET Title | Primary Competencies |
| :--- | :--- | :--- | :--- |
| **Data Analyst** | `15-2051.01` | Business Intelligence Analysts | SQL, Statistics, Data Visualization, Excel |
| **Data Scientist** | `15-2051.00` | Data Scientists | Python, Machine Learning, Statistics, Modeling |
| **Machine Learning Engineer** | `15-2051.00` | Data Scientists / ML Engineers | Python, ML Pipelines, MLOps, Algorithms & OOP |
| **Software Developer** | `15-1252.00` | Software Developers | Algorithms, Data Structures, OOP, Git, System Design |
| **Java Developer** | `15-1251.00` | Computer Programmers | Core Java, Spring Boot, Hibernate, SQL, OOP |
| **Web Developer** | `15-1254.00` | Web Developers | HTML5, CSS3, JavaScript, Web APIs, Responsive UI |
| **Full Stack Developer** | `15-1252.00` | Software Developers (Full Stack) | Frontend + Backend, Databases, REST APIs |
| **Cloud / DevOps Engineer** | `15-1299.08` | Computer Systems Engineers | Linux, Docker, CI/CD, Infrastructure, Python |

---

## 📊 Machine Learning Model Benchmarks

| Model | CV Accuracy (Train) | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Multinomial)** | **0.9900** | **0.9833** | **0.9838** | **0.9833** | **0.9833** | 🏆 **Active Model** |
| **Random Forest Classifier** | 0.9883 | 0.9800 | 0.9805 | 0.9800 | 0.9800 | Candidate Model |
| **K-Nearest Neighbors (KNN)** | 0.9908 | 0.9767 | 0.9779 | 0.9767 | 0.9766 | Candidate Model |
| **Decision Tree Classifier** | 0.9525 | 0.9467 | 0.9474 | 0.9467 | 0.9465 | Candidate Model |

---

## 📐 Skill Gap Analysis Mathematical Formula

The **Skill Match Percentage** is calculated using a weighted fulfillment ratio:

$$\text{Fulfillment}_i = \min\left(1.0, \frac{S_i}{R_i}\right)$$

$$\text{Skill Match \%} = \left( \frac{\sum_{i=1}^{n} \text{Fulfillment}_i \times R_i}{\sum_{i=1}^{n} R_i} \right) \times 100$$

Where:
* $S_i$: Student's inferred proficiency level for skill $i \in [0.0, 5.0]$.
* $R_i$: O*NET benchmark requirement for skill $i \in [0.0, 5.0]$.
* **Capping at 1.0**: Over-qualification in one skill cannot falsely mask deficiency in an unrelated required skill.
* **Weights ($R_i$)**: Foundational core skills carry proportionally higher influence.

---

## 🚀 How to Run the Project Locally

### 1. Launch with One-Click Batch Script
Double-click `run_app.bat` or `Launch_Skill_Gap_Analyzer.bat` on your Desktop.

### 2. Manual Terminal Launch
```powershell
.\Skill-Gap-Analyzer\venv\Scripts\Activate.ps1
streamlit run app\app.py
```

The application will open in your default browser at `http://localhost:8501`.
