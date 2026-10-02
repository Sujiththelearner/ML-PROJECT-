"""
Qualitative-to-Feature Evaluation Engine
Transforms structured qualitative inputs (experience levels, project counts,
descriptions, certifications, and uploaded certificates) into model-compatible
numerical feature vectors while extracting human-readable evidence summaries.
"""

import re

# 10 Model-Compatible Features
FEATURE_NAMES = [
    "Python", "Java", "SQL", "Git", "HTML_CSS",
    "JavaScript", "Machine_Learning", "Statistics",
    "Data_Visualization", "Algorithms_OOP"
]

PRACTICAL_LEVEL_BASE_SCORES = {
    "No experience": 0.0,
    "Beginner / Learning": 1.2,
    "Academic projects": 2.2,
    "Personal projects": 3.2,
    "Internship / real-world experience": 4.2,
    "Professional experience": 4.8
}

PROJECT_COUNT_BOOST = {
    "0": 0.0,
    "1": 0.2,
    "2": 0.4,
    "3": 0.6,
    "4+": 0.8
}

# Skill Alias / Keyword Mapping for Project & Certificate Text Matching
SKILL_ALIASES = {
    "Python": ["python", "pandas", "numpy", "django", "flask", "fastapi"],
    "Java": ["java", "spring", "hibernate", "jvm", "maven", "springboot"],
    "SQL": ["sql", "mysql", "postgresql", "sqlite", "oracle", "database", "rdbms"],
    "Git": ["git", "github", "gitlab", "version control"],
    "HTML_CSS": ["html", "css", "html5", "css3", "tailwind", "bootstrap", "flexbox", "grid"],
    "JavaScript": ["javascript", "js", "typescript", "ts", "react", "node", "express", "vue", "nextjs"],
    "Machine_Learning": ["machine learning", "ml", "deep learning", "neural network", "scikit-learn", "sklearn", "tensorflow", "pytorch", "ai", "nlp"],
    "Statistics": ["statistics", "probability", "hypothesis testing", "regression", "stat", "eda"],
    "Data_Visualization": ["tableau", "power bi", "powerbi", "matplotlib", "seaborn", "dashboard", "bi", "data viz"],
    "Algorithms_OOP": ["data structures", "algorithms", "dsa", "oop", "object-oriented", "leetcode", "design patterns"]
}

def evaluate_profile_to_features(user_profile: dict) -> dict:
    """
    Transforms qualitative profile information into:
    1. 'features_dict': Numerical 0.0 to 5.0 scale for existing ML pipeline.
    2. 'evidence_by_skill': Human-readable proof points explaining the ratings.
    3. 'overall_evidence': Top qualitative strengths for career prediction explanation.
    """
    skills_input = user_profile.get("skills_experience", {})
    projects = user_profile.get("projects", [])
    uploaded_certs = user_profile.get("uploaded_certificates", [])
    
    features_dict = {}
    evidence_by_skill = {}
    overall_evidence = []

    for skill in FEATURE_NAMES:
        skill_data = skills_input.get(skill, {})
        practical_level = skill_data.get("practical_level", "No experience")
        project_count = str(skill_data.get("project_count", "0"))
        has_cert = skill_data.get("has_cert", False)
        cert_name = skill_data.get("cert_name", "").strip()
        cert_org = skill_data.get("cert_org", "").strip()
        description = skill_data.get("description", "").strip()

        # 1. Base Score from Experience Level
        base_score = PRACTICAL_LEVEL_BASE_SCORES.get(practical_level, 0.0)
        score = base_score
        proof_points = []

        if practical_level != "No experience":
            proof_points.append(f"{practical_level} background")

        # 2. Boost from Project Count
        proj_boost = PROJECT_COUNT_BOOST.get(project_count, 0.0)
        score += proj_boost
        if project_count not in ["0", "None"]:
            proof_points.append(f"{project_count} completed project(s)")

        # 3. Boost from Explicit Certification
        if has_cert and cert_name:
            score += 0.4
            org_str = f" from {cert_org}" if cert_org else ""
            proof_points.append(f"Certified: '{cert_name}'{org_str}")

        # 4. Boost from Uploaded Certificates
        for u_cert in uploaded_certs:
            detected = u_cert.get("detected_skills", [])
            cert_title = u_cert.get("title", "Certificate")
            cert_org_u = u_cert.get("organization", "")
            if skill in detected or any(alias in u_cert.get("title", "").lower() for alias in SKILL_ALIASES[skill]):
                score += 0.3
                proof_points.append(f"Uploaded Certificate: '{cert_title}' ({cert_org_u})")

        # 5. Boost from Project Portfolio Descriptions
        for p in projects:
            p_name = p.get("name", "").strip()
            p_tech = p.get("technologies", "").lower()
            p_desc = p.get("description", "").lower()
            combined_project_text = f"{p_name} {p_tech} {p_desc}"
            
            if any(re.search(r'\b' + re.escape(alias) + r'\b', combined_project_text) for alias in SKILL_ALIASES[skill]):
                score += 0.3
                proof_points.append(f"Applied in project '{p_name}'")
                break

        # 6. Detail from Description
        if len(description) > 15:
            score += 0.2
            proof_points.append(f"Hands-on application: \"{description[:60]}...\"")

        # Bound score strictly between 0.0 and 5.0
        final_score = round(min(5.0, max(0.0, score)), 1)
        features_dict[skill] = final_score

        # Status categorization
        if final_score >= 3.0:
            status = "Already Demonstrated"
            icon = "🟢"
        elif final_score >= 1.0:
            status = "Needs Improvement"
            icon = "🟡"
        else:
            status = "Not Yet Demonstrated"
            icon = "🔴"

        evidence_by_skill[skill] = {
            "score": final_score,
            "status": status,
            "icon": icon,
            "proof_points": proof_points if proof_points else ["No practical evidence recorded yet."]
        }

        # Collect top positive evidence for prediction summary
        if final_score >= 3.0:
            primary_proof = proof_points[0] if proof_points else f"Demonstrated {skill} competency"
            overall_evidence.append(f"**{skill}**: {primary_proof}")

    return {
        "features_dict": features_dict,
        "evidence_by_skill": evidence_by_skill,
        "overall_evidence": overall_evidence[:6]  # top highlights
    }
