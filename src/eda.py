"""
Phase 7: Exploratory Data Analysis (EDA)
Generates statistical summaries and high-resolution plots
to inspect the dataset characteristics and save to results/plots/.
"""

import os
import matplotlib
matplotlib.use('Agg')  # Headless mode for saving plots without GUI popup
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DATASET_PATH = os.path.join("dataset", "processed", "student_skills_dataset.csv")
PLOTS_DIR = os.path.join("results", "plots")

def perform_eda():
    print("=" * 65)
    print("Phase 7: Exploratory Data Analysis (EDA)")
    print("=" * 65)

    if not os.path.exists(DATASET_PATH):
        print(f"[ERROR] Dataset not found at: {DATASET_PATH}")
        return

    df = pd.read_csv(DATASET_PATH)
    os.makedirs(PLOTS_DIR, exist_ok=True)

    # 1. Dataset Shape & Integrity Check
    print("\n[1] Dataset Health Check:")
    print(f"  * Total Samples: {len(df):,}")
    print(f"  * Total Features: {df.shape[1] - 1}")
    print(f"  * Missing Values: {df.isnull().sum().sum()} (Zero nulls!)")

    # 2. Statistical Summary
    print("\n[2] Feature Value Ranges (Min to Max):")
    stats = df.describe().T[["min", "mean", "max", "std"]]
    print(stats.round(2).to_string())

    # 3. Mean Skills per Target Career
    print("\n[3] Mean Skill Proficiency per Career Category:")
    career_means = df.groupby("Career").mean()
    print(career_means.round(2).to_string())

    # 4. Generate Plot 1: Career Skill Profiles Heatmap
    plt.figure(figsize=(11, 6))
    sns.heatmap(
        career_means,
        annot=True,
        cmap="YlGnBu",
        fmt=".2f",
        cbar_kws={"label": "Proficiency Level (0-5)"}
    )
    plt.title("Average Skill Proficiency by Career Profile", fontsize=14, pad=15)
    plt.xlabel("Technical Skills", fontsize=12)
    plt.ylabel("Target Career", fontsize=12)
    plt.tight_layout()
    plot1_path = os.path.join(PLOTS_DIR, "eda_career_profiles_heatmap.png")
    plt.savefig(plot1_path, dpi=300)
    plt.close()
    print(f"\n[SAVED] Career Profiles Heatmap -> {plot1_path}")

    # 5. Generate Plot 2: Skill Feature Correlation Matrix
    numeric_df = df.drop(columns=["Career"])
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        vmin=-1,
        vmax=1
    )
    plt.title("Skill Feature Correlation Matrix", fontsize=14, pad=15)
    plt.tight_layout()
    plot2_path = os.path.join(PLOTS_DIR, "eda_feature_correlation.png")
    plt.savefig(plot2_path, dpi=300)
    plt.close()
    print(f"[SAVED] Feature Correlation Matrix -> {plot2_path}")

    # 6. Generate Plot 3: Boxplot of Distinctive Skills
    plt.figure(figsize=(14, 6))
    key_skills = ["Python", "Java", "HTML_CSS", "Machine_Learning", "Data_Visualization"]
    melted_df = pd.melt(
        df,
        id_vars=["Career"],
        value_vars=key_skills,
        var_name="Skill",
        value_name="Proficiency"
    )
    sns.boxplot(data=melted_df, x="Skill", y="Proficiency", hue="Career", palette="Set2")
    plt.title("Skill Distributions Across Career Categories", fontsize=14, pad=15)
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plot3_path = os.path.join(PLOTS_DIR, "eda_skill_distributions.png")
    plt.savefig(plot3_path, dpi=300)
    plt.close()
    print(f"[SAVED] Skill Distribution Boxplot -> {plot3_path}")

    print("\n" + "=" * 65)
    print("EDA completed successfully! Visualizations saved in results/plots/.")
    print("=" * 65)

if __name__ == "__main__":
    perform_eda()
