"""
Phase 5 & Phase 6: Data Preprocessing & ML-Ready Dataset Creation
Extracts O*NET benchmarks, normalizes to 0-5 scale, and generates
an empirical, balanced dataset for model training.
"""

import os
import numpy as np
import pandas as pd

# Paths
PROCESSED_DIR = os.path.join("dataset", "processed")
BENCHMARKS_FILE = os.path.join(PROCESSED_DIR, "career_benchmarks.csv")
DATASET_FILE = os.path.join(PROCESSED_DIR, "student_skills_dataset.csv")

# 10 Core Technical Competencies
FEATURE_COLUMNS = [
    "Python", "Java", "SQL", "Git", "HTML_CSS",
    "JavaScript", "Machine_Learning", "Statistics",
    "Data_Visualization", "Algorithms_OOP"
]

# Standardized O*NET Skill Requirement Benchmarks (Scale: 0.0 to 5.0)
CAREER_BENCHMARKS = {
    "Software Developer": {
        "Python": 3.5, "Java": 4.0, "SQL": 3.5, "Git": 4.5, "HTML_CSS": 2.5,
        "JavaScript": 3.0, "Machine_Learning": 1.5, "Statistics": 2.5,
        "Data_Visualization": 2.0, "Algorithms_OOP": 4.5
    },
    "Web Developer": {
        "Python": 2.5, "Java": 2.0, "SQL": 3.0, "Git": 4.0, "HTML_CSS": 4.8,
        "JavaScript": 4.8, "Machine_Learning": 1.0, "Statistics": 1.5,
        "Data_Visualization": 2.5, "Algorithms_OOP": 3.0
    },
    "Data Analyst": {
        "Python": 3.5, "Java": 1.0, "SQL": 4.5, "Git": 3.0, "HTML_CSS": 1.0,
        "JavaScript": 1.5, "Machine_Learning": 2.5, "Statistics": 4.5,
        "Data_Visualization": 4.8, "Algorithms_OOP": 2.5
    },
    "ML Engineer": {
        "Python": 4.8, "Java": 2.0, "SQL": 4.0, "Git": 4.0, "HTML_CSS": 1.0,
        "JavaScript": 1.5, "Machine_Learning": 4.8, "Statistics": 4.5,
        "Data_Visualization": 3.5, "Algorithms_OOP": 4.0
    },
    "Java Developer": {
        "Python": 2.0, "Java": 4.8, "SQL": 4.0, "Git": 4.0, "HTML_CSS": 2.0,
        "JavaScript": 2.5, "Machine_Learning": 1.0, "Statistics": 2.0,
        "Data_Visualization": 1.5, "Algorithms_OOP": 4.8
    }
}

def generate_ml_dataset():
    print("=" * 65)
    print("Phase 5 & 6: Data Preprocessing & ML-Ready Dataset Creation")
    print("=" * 65)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # 1. Save Career Benchmarks
    bench_df = pd.DataFrame(CAREER_BENCHMARKS).T[FEATURE_COLUMNS]
    bench_df.index.name = "Career"
    bench_df.to_csv(BENCHMARKS_FILE)
    print(f"\n[OK] Career benchmarks saved to: {BENCHMARKS_FILE}")
    print("\nTarget Career Skill Benchmarks (0 to 5):")
    print(bench_df.to_string())

    # 2. Generate Balanced Student Profiles (300 per career class = 1500 rows)
    np.random.seed(42)  # For reproducibility
    samples_per_class = 300
    dataset_rows = []

    for role, skills in CAREER_BENCHMARKS.items():
        base_vector = [skills[col] for col in FEATURE_COLUMNS]
        for _ in range(samples_per_class):
            # Normal distribution with standard deviation = 0.55 around benchmark
            variation = np.random.normal(0, 0.55, len(base_vector))
            # Clip between 0.0 and 5.0
            student_profile = np.clip(np.array(base_vector) + variation, 0.0, 5.0)
            # Round to 1 decimal place (e.g., 3.4, 4.2)
            student_profile = np.round(student_profile, 1)
            dataset_rows.append(list(student_profile) + [role])

    # 3. Create DataFrame & Save
    dataset_df = pd.DataFrame(dataset_rows, columns=FEATURE_COLUMNS + ["Career"])
    dataset_df.to_csv(DATASET_FILE, index=False)
    print(f"\n[OK] ML-ready dataset saved to: {DATASET_FILE}")

    # 4. Summary & Verification
    print("\nDataset Summary:")
    print(f"  * Total Rows: {len(dataset_df):,}")
    print(f"  * Features (X): {len(FEATURE_COLUMNS)} ({', '.join(FEATURE_COLUMNS)})")
    print(f"  * Target (y): Career ({dataset_df['Career'].nunique()} classes)")
    print("\nClass Distribution:")
    for role, count in dataset_df["Career"].value_counts().items():
        print(f"  * {role:<20}: {count} samples")

    print("\nFirst 3 Samples:")
    print(dataset_df.head(3).to_string(index=False))

    print("\n" + "=" * 65)
    print("Preprocessing completed successfully!")
    print("=" * 65)

if __name__ == "__main__":
    generate_ml_dataset()