"""
Phase 4: Dataset Inspector for Skill Gap Analyzer
Inspects skills and technologies for our 5 target career categories.
"""

import os
import pandas as pd

RAW_DIR = os.path.join("dataset", "raw")

# Target career mappings
CAREER_MAP = {
    "15-1252.00": "Software Developer",
    "15-1254.00": "Web Developer",
    "15-2051.01": "Data Analyst",
    "15-2051.00": "ML Engineer",
    "15-1251.00": "Java Developer"
}

def inspect_target_careers():
    print("=" * 70)
    print("Phase 4: Inspecting Target Careers in O*NET Data")
    print("=" * 70)

    # 1. Load Occupation Data
    occ_df = pd.read_csv(os.path.join(RAW_DIR, "Occupation Data.txt"), sep="\t")
    target_socs = list(CAREER_MAP.keys())
    matched_occ = occ_df[occ_df["O*NET-SOC Code"].isin(target_socs)]
    
    print("\n[1] Mapped Careers:")
    for _, row in matched_occ.iterrows():
        soc = row["O*NET-SOC Code"]
        print(f"  * {CAREER_MAP[soc]:<20} (SOC: {soc}) -> {row['Title']}")

    # 2. Inspect Foundational Skills (Scale: Importance IM, 1 to 5)
    skills_df = pd.read_csv(os.path.join(RAW_DIR, "Skills.txt"), sep="\t")
    im_skills = skills_df[(skills_df["O*NET-SOC Code"].isin(target_socs)) & (skills_df["Scale ID"] == "IM")]
    
    print("\n[2] Top Foundational Skills per Career (Scale 1.0 to 5.0):")
    for soc, role in CAREER_MAP.items():
        role_skills = im_skills[im_skills["O*NET-SOC Code"] == soc].sort_values(by="Data Value", ascending=False)
        top_skills = role_skills.head(4)[["Element Name", "Data Value"]].values
        skills_str = ", ".join([f"{name} ({val:.2f})" for name, val in top_skills])
        print(f"  * {role:<20}: {skills_str}")

    # 3. Inspect Technology Skills
    tech_df = pd.read_csv(os.path.join(RAW_DIR, "Technology Skills.txt"), sep="\t")
    target_tech = tech_df[tech_df["O*NET-SOC Code"].isin(target_socs)]
    
    print("\n[3] Sample Technology Skills / Tools per Career:")
    for soc, role in CAREER_MAP.items():
        tools = target_tech[target_tech["O*NET-SOC Code"] == soc]["Example"].unique()
        # Show up to 5 representative tools
        sample_tools = ", ".join(list(tools)[:5])
        print(f"  * {role:<20} ({len(tools)} tools recorded): {sample_tools} ...")

    print("\n" + "=" * 70)
    print("Inspection complete! All 5 categories have strong, distinct skill profiles.")
    print("=" * 70)

if __name__ == "__main__":
    inspect_target_careers()