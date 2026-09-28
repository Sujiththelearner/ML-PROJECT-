"""
Phase 15: Skill Gap Analyzer
Compares student skill proficiencies against O*NET benchmark requirements
for the target career. Computes a mathematically sound Skill Match Percentage.
"""

import os
import pandas as pd

BENCHMARKS_PATH = os.path.join("dataset", "processed", "career_benchmarks.csv")

class SkillGapAnalyzer:
    def __init__(self, benchmarks_path=BENCHMARKS_PATH):
        if not os.path.exists(benchmarks_path):
            raise FileNotFoundError(f"Benchmarks not found at {benchmarks_path}")
        self.benchmarks_df = pd.read_csv(benchmarks_path, index_col=0)

    def analyze(self, student_skills: dict, target_career: str) -> dict:
        """
        Performs rigorous skill gap analysis for the target career.
        
        Formula for Skill Match Percentage:
            Fulfillment_i = min(1.0, Student_i / Required_i)
            Weighted Fulfillment = sum(Fulfillment_i * Required_i)
            Total Required Weight = sum(Required_i)
            Match % = (Weighted Fulfillment / Total Required Weight) * 100
        """
        if target_career not in self.benchmarks_df.index:
            raise ValueError(f"Career '{target_career}' not found in benchmarks.")

        career_reqs = self.benchmarks_df.loc[target_career].to_dict()

        matched_skills = []
        weak_skills = []
        missing_skills = []

        total_weighted_fulfillment = 0.0
        total_required_weight = 0.0

        for skill, required_level in career_reqs.items():
            student_level = float(student_skills.get(skill, 0.0))
            
            if required_level > 0:
                fulfillment_ratio = min(1.0, student_level / required_level)
                total_weighted_fulfillment += fulfillment_ratio * required_level
                total_required_weight += required_level

            gap = round(max(0.0, required_level - student_level), 2)

            skill_info = {
                "skill": skill,
                "student_level": student_level,
                "required_level": required_level,
                "gap": gap
            }

            if student_level >= required_level:
                matched_skills.append(skill_info)
            elif student_level > 0:
                weak_skills.append(skill_info)
            else:
                missing_skills.append(skill_info)

        # Calculate overall weighted match percentage
        if total_required_weight > 0:
            match_percentage = round((total_weighted_fulfillment / total_required_weight) * 100, 1)
        else:
            match_percentage = 0.0

        # Sort weak and missing skills by largest gap first
        weak_skills.sort(key=lambda x: x["gap"], reverse=True)
        missing_skills.sort(key=lambda x: x["gap"], reverse=True)

        return {
            "target_career": target_career,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "weak_skills": weak_skills,
            "missing_skills": missing_skills
        }
