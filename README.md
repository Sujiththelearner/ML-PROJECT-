# Skill Gap Analyzer – ML-Based Career Prediction and Skill Gap Recommendation System
**Department:** Computer Science and Engineering (CSE)

---

## 📌 Project Overview
The **Skill Gap Analyzer** is an end-to-end Machine Learning web application designed to help engineering students identify their ideal career path and systematically close technical skill deficits. 

Unlike traditional static rule-based systems, this project employs a **trained Machine Learning classifier** benchmarked against real-world occupational data from the **U.S. Department of Labor (O*NET 28.0 Database)**.

### Key Capabilities:
1. **Multi-Class Career Prediction**: Evaluates 10 core computer science competencies to predict the best-fit career among 5 industry roles.
2. **Probability Distribution**: Displays confidence and secondary probabilities across all career options.
3. **Empirical Skill Gap Analysis**: Quantifies skill gaps by comparing student proficiency against standardized O*NET benchmarks.
4. **Weighted Skill Match Score**: Calculates a mathematically grounded percentage score using a weighted fulfillment ratio.
5. **Actionable Recommendations**: Generates tailored learning roadmaps, capstone project ideas, and documentation resources.

---

## 🏛️ Project Architecture & Pipeline

```text
       Raw O*NET 28.0 Database (Occupation, Skills, Knowledge, Tech Skills)
                                    │
                                    ▼
       Data Preprocessing & Standardization (Normalized to 0.0 - 5.0 scale)
                                    │
                                    ▼
       Empirical Dataset Generation (1,500 samples across 5 balanced classes)
                                    │
                                    ▼
       Exploratory Data Analysis (Heatmaps, Feature Correlations, Boxplots)
                                    │
                                    ▼
       Feature Preprocessing (Train/Test Split 80/20 + StandardScaler Pipeline)
                                    │
                                    ▼
       Model Training & Comparison (Logistic Regression, Decision Tree, Random Forest, KNN)
                                    │
                                    ▼
       Model Evaluation & Persistence (Best Model: Logistic Regression, 98.33% Accuracy)
                                    │
                                    ▼
       Interactive Streamlit Web Application (Home -> Assessment -> Prediction -> Gap Analysis -> Recommendations)
```

---

## 🎯 Target Career Categories & O*NET SOC Mapping

| Career Category | O*NET-SOC Code | Official O*NET Title | Role Focus & Core Skills |
| :--- | :--- | :--- | :--- |
| **Software Developer** | `15-1252.00` | Software Developers | Algorithms, Data Structures, OOP, Git, System Design |
| **Web Developer** | `15-1254.00` | Web Developers | HTML5, CSS3, JavaScript, Web APIs, Frameworks |
| **Data Analyst** | `15-2051.01` | Business Intelligence Analysts | SQL, Statistics, Data Visualization, Excel, BI Reporting |
| **ML Engineer** | `15-2051.00` | Data Scientists | Python, Machine Learning Algorithms, Mathematics, Data Modeling |
| **Java Developer** | `15-1251.00` | Computer Programmers | Core Java, Enterprise Backend (Spring/Hibernate), OOP, SQL |

---

## 📊 Model Comparison & Evaluation Results

All models were evaluated using **5-Fold Cross-Validation** on training data (1,200 samples) and evaluated on an unseen stratified test set (300 samples):

| Model | CV Accuracy (Train) | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Multinomial)** | **0.9900** | **0.9833** | **0.9838** | **0.9833** | **0.9833** | 🏆 **Best Model (Selected)** |
| **Random Forest Classifier** | 0.9883 | 0.9800 | 0.9805 | 0.9800 | 0.9800 | Candidate Model |
| **K-Nearest Neighbors (KNN)** | 0.9908 | 0.9767 | 0.9779 | 0.9767 | 0.9766 | Candidate Model |
| **Decision Tree Classifier** | 0.9525 | 0.9467 | 0.9474 | 0.9467 | 0.9465 | Candidate Model |

---

## 📐 Skill Gap Analysis Mathematical Formula

The **Skill Match Percentage** is computed using a weighted fulfillment ratio:

$$\text{Fulfillment}_i = \min\left(1.0, \frac{S_i}{R_i}\right)$$

$$\text{Skill Match \%} = \left( \frac{\sum_{i=1}^{n} \text{Fulfillment}_i \times R_i}{\sum_{i=1}^{n} R_i} \right) \times 100$$

Where:
* $S_i$: Student's self-assessed proficiency for skill $i \in [0.0, 5.0]$.
* $R_i$: O*NET benchmark requirement for skill $i \in [0.0, 5.0]$.
* **Capping at 1.0**: Ensures that over-qualification in one skill cannot falsely mask deficiency in an unrelated required skill.
* **Weights ($R_i$)**: Ensures that foundational core skills for the role carry proportionally higher influence.

---

## 📁 Project Directory Structure

```text
Skill-Gap-Analyzer/
├── app/
│   └── app.py                        # Streamlit 5-page interactive web application
├── dataset/
│   ├── raw/                          # Untouched O*NET 28.0 raw files (Occupations, Skills, Tech)
│   └── processed/
│       ├── career_benchmarks.csv     # Clean O*NET skill requirements (0-5 scale)
│       └── student_skills_dataset.csv # 1,500 balanced student profile samples
├── models/
│   └── career_model.pkl              # Saved Scikit-learn Pipeline (Scaler + Model)
├── notebooks/                        # Exploration and prototyping
├── results/
│   ├── metrics/
│   │   └── model_comparison.csv      # Model performance ranking table
│   └── plots/
│       ├── eda_career_profiles_heatmap.png
│       ├── eda_feature_correlation.png
│       ├── eda_skill_distributions.png
│       ├── best_model_confusion_matrix.png
│       └── feature_importance.png
├── src/
│   ├── download_data.py              # Automates downloading O*NET archive
│   ├── inspect_data.py               # Inspects occupational requirements
│   ├── data_preprocessing.py         # Standardizes benchmarks & generates dataset
│   ├── eda.py                        # Generates statistical plots
│   ├── train_model.py                # Trains, cross-validates, and evaluates models
│   ├── predict.py                    # Prediction inference engine
│   ├── skill_gap.py                  # Weighted skill gap analysis
│   ├── recommendations.py            # Structured learning roadmap & project knowledge base
│   └── test_pipeline.py              # End-to-end integration test
├── requirements.txt                  # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Project Locally

### 1. Activate Virtual Environment
```powershell
.\Skill-Gap-Analyzer\venv\Scripts\Activate.ps1
```

### 2. Verify / Retrain Models (Optional)
```powershell
python src\train_model.py
```

### 3. Launch Streamlit Web Application
```powershell
streamlit run app\app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🎓 College Viva Preparation Guide

### Q1: Why did you use Machine Learning instead of traditional Rule-Based if-else conditions?
> **Answer**: Traditional rule-based systems are rigid, fragile, and fail when students have overlapping or non-standard skill combinations. A Machine Learning classifier learns probabilistic decision boundaries across multiple continuous dimensions, accurately estimating model confidence and handling complex real-world skill profiles.

### Q2: Why is Logistic Regression selected over Random Forest?
> **Answer**: In our rigorous cross-validation and test set evaluation, Logistic Regression achieved a higher test F1-score (**98.33%**) and cross-validation accuracy (**99.00%**) compared to Random Forest (**98.00%**). Because skill competencies have well-defined linear and probabilistic boundaries when normalized with `StandardScaler`, a multinomial logistic regression model provided superior generalization without overfitting.

### Q3: How did you prevent data leakage during preprocessing?
> **Answer**: We applied a Scikit-learn `Pipeline` encapsulating `StandardScaler`. The scaler parameters (mean and standard deviation) were fitted strictly on the 80% training set and then applied to transform the 20% test set, preventing any statistical information from the test set from leaking into model training.

### Q4: How is the Skill Match Percentage calculated?
> **Answer**: We use a weighted fulfillment ratio: $\text{Fulfillment}_i = \min(1.0, S_i / R_i)$, weighted by the required importance $R_i$. Capping at 1.0 prevents surplus proficiency in one skill (like Python) from compensating for zero proficiency in a mandatory skill (like SQL or Data Visualization).
