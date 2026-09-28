"""
Test End-to-End Pipeline: Prediction -> Skill Gap -> Recommendations
Tests with a sample student profile.
"""

from predict import CareerPredictor
from skill_gap import SkillGapAnalyzer
from recommendations import RecommendationEngine

def test_pipeline():
    print("=" * 65)
    print("Testing End-to-End Skill Gap Analyzer Pipeline")
    print("=" * 65)

    # 1. Sample Student Input Profile
    student_profile = {
        "Python": 4.0,
        "Java": 1.5,
        "SQL": 4.5,
        "Git": 3.0,
        "HTML_CSS": 1.0,
        "JavaScript": 1.5,
        "Machine_Learning": 2.5,
        "Statistics": 4.0,
        "Data_Visualization": 3.5,
        "Algorithms_OOP": 2.5
    }

    print("\n[Input] Student Profile:")
    for skill, lvl in student_profile.items():
        print(f"  * {skill:<20}: {lvl} / 5.0")

    # 2. Phase 14: Career Prediction
    predictor = CareerPredictor()
    pred_result = predictor.predict(student_profile)
    predicted_career = pred_result["predicted_career"]

    print("\n" + "-" * 65)
    print(f"[Phase 14] Predicted Career: {predicted_career}")
    print(f"Confidence: {pred_result['confidence']:.2f}% (Model: {pred_result['model_used']})")
    print("Class Probabilities:")
    for role, prob in pred_result["probabilities"].items():
        print(f"  - {role:<20}: {prob:.2f}%")

    # 3. Phase 15: Skill Gap Analysis
    analyzer = SkillGapAnalyzer()
    gap_result = analyzer.analyze(student_profile, predicted_career)

    print("\n" + "-" * 65)
    print(f"[Phase 15] Skill Gap Analysis for: {predicted_career}")
    print(f"Overall Skill Match: {gap_result['match_percentage']}%")

    print(f"\nMatched Skills ({len(gap_result['matched_skills'])}):")
    for s in gap_result["matched_skills"]:
        print(f"  [MET] {s['skill']:<20}: Student={s['student_level']} | Required={s['required_level']}")

    print(f"\nWeak Skills ({len(gap_result['weak_skills'])}):")
    for s in gap_result["weak_skills"]:
        print(f"  [WEAK] {s['skill']:<19}: Student={s['student_level']} | Required={s['required_level']} (Gap: -{s['gap']})")

    print(f"\nMissing Skills ({len(gap_result['missing_skills'])}):")
    for s in gap_result["missing_skills"]:
        print(f"  [MISSING] {s['skill']:<16}: Student={s['student_level']} | Required={s['required_level']} (Gap: -{s['gap']})")

    # 4. Phase 16: Recommendations
    rec_engine = RecommendationEngine()
    recommendations = rec_engine.generate(gap_result)

    print("\n" + "-" * 65)
    print(f"[Phase 16] Actionable Recommendations ({len(recommendations)} areas):")
    for rec in recommendations[:2]:  # Show top 2 in console test
        print(f"\nArea: {rec['skill']} ({rec['status']} - Gap: {rec['gap']})")
        print(f"  * Focus: {rec['importance']}")
        print(f"  * Recommended Action: {rec['action_steps'][0]}")
        print(f"  * Project Idea: {rec['project_idea']}")
        print(f"  * Resource: {rec['resources']}")

    print("\n" + "=" * 65)
    print("End-to-End Pipeline Verification Successful!")
    print("=" * 65)

if __name__ == "__main__":
    test_pipeline()
