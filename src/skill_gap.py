"""
Phase 15: Skill Gap Analyzer (Enhanced)
Compares student skill evidence against O*NET benchmark requirements
for the target career role. Computes weighted match percentage and
enriches gaps with actionable explanations, learning topics, and projects.
"""

import os
import pandas as pd
try:
    from src.job_roles_data import get_job_role_info
    from src.recommendations import RECOMMENDATION_DATABASE
except ImportError:
    from job_roles_data import get_job_role_info
    from recommendations import RECOMMENDATION_DATABASE

BENCHMARKS_PATH = os.path.join("dataset", "processed", "career_benchmarks.csv")

class SkillGapAnalyzer:
    def __init__(self, benchmarks_path=BENCHMARKS_PATH):
        if not os.path.exists(benchmarks_path):
            raise FileNotFoundError(f"Benchmarks not found at {benchmarks_path}")
        self.benchmarks_df = pd.read_csv(benchmarks_path, index_col=0)

    def analyze(self, student_skills: dict, target_career: str, evidence_by_skill: dict = None) -> dict:
        """
        Performs rigorous, evidence-based skill gap analysis for any target career role.
        """
        # Resolve mapped O*NET benchmark role
        role_info = get_job_role_info(target_career)
        benchmark_role = role_info.get("mapped_model_career", "Software Developer")
        
        if benchmark_role not in self.benchmarks_df.index:
            benchmark_role = "Software Developer"

        career_reqs = self.benchmarks_df.loc[benchmark_role].to_dict()

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
            
            # Fetch qualitative advice from knowledge base
            rec_info = RECOMMENDATION_DATABASE.get(skill, {
                "importance": f"Important competency for {target_career}.",
                "action_steps": [f"Learn fundamentals of {skill}.", f"Build practical exercises in {skill}."],
                "project_idea": f"Implement a practical project utilizing {skill}.",
                "resources": "Online technical documentation."
            })

            # Retrieve evidence points if provided
            skill_evidence = []
            if evidence_by_skill and skill in evidence_by_skill:
                skill_evidence = evidence_by_skill[skill].get("proof_points", [])

            skill_info = {
                "skill": skill,
                "student_level": student_level,
                "required_level": required_level,
                "gap": gap,
                "evidence": skill_evidence,
                "why_required": rec_info.get("importance", ""),
                "what_to_learn": rec_info.get("action_steps", [])[:2],
                "how_to_improve": rec_info.get("action_steps", [])[2:] if len(rec_info.get("action_steps", [])) > 2 else rec_info.get("action_steps", []),
                "suggested_project": rec_info.get("project_idea", ""),
                "resources": rec_info.get("resources", "")
            }

            # Categorize based on student proficiency vs benchmark
            if student_level >= required_level:
                skill_info["status_label"] = "Already Demonstrated"
                skill_info["status_icon"] = "🟢"
                matched_skills.append(skill_info)
            elif student_level > 1.0:
                skill_info["status_label"] = "Needs Improvement"
                skill_info["status_icon"] = "🟡"
                weak_skills.append(skill_info)
            else:
                skill_info["status_label"] = "Not Yet Demonstrated"
                skill_info["status_icon"] = "🔴"
                missing_skills.append(skill_info)

        # Calculate overall weighted match percentage
        if total_required_weight > 0:
            match_percentage = round((total_weighted_fulfillment / total_required_weight) * 100, 1)
        else:
            match_percentage = 0.0

        # Sort weak and missing skills by largest gap
        weak_skills.sort(key=lambda x: x["gap"], reverse=True)
        missing_skills.sort(key=lambda x: x["gap"], reverse=True)

        return {
            "target_career": target_career,
            "benchmark_role": benchmark_role,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "weak_skills": weak_skills,
            "missing_skills": missing_skills,
            "role_info": role_info
        }
