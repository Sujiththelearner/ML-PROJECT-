"""
Phase 14: Career Prediction Engine
Loads the trained ML model pipeline and predicts the career
with confidence probabilities based on student skills.
"""

import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join("models", "career_model.pkl")

class CareerPredictor:
    def __init__(self, model_path=MODEL_PATH):
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found at {model_path}. Train the model first using src/train_model.py."
            )
        payload = joblib.load(model_path)
        self.pipeline = payload["pipeline"]
        self.model_name = payload["model_name"]
        self.feature_names = payload["feature_names"]
        self.classes = payload["classes"]

    def predict(self, student_skills: dict) -> dict:
        """
        Predicts suitable career and class probabilities.
        
        Args:
            student_skills (dict): e.g. {'Python': 4.0, 'SQL': 4.0, ...}
        Returns:
            dict: predicted career, confidence, and all class probabilities.
        """
        # Ensure all features exist in correct order
        input_vector = [student_skills.get(col, 0.0) for col in self.feature_names]
        input_df = pd.DataFrame([input_vector], columns=self.feature_names)

        # Predict class & probabilities
        pred_career = self.pipeline.predict(input_df)[0]
        probabilities = self.pipeline.predict_proba(input_df)[0]

        prob_dict = {
            cls: round(float(prob) * 100, 2)
            for cls, prob in zip(self.classes, probabilities)
        }
        sorted_probs = dict(sorted(prob_dict.items(), key=lambda item: item[1], reverse=True))

        return {
            "predicted_career": pred_career,
            "confidence": sorted_probs[pred_career],
            "probabilities": sorted_probs,
            "model_used": self.model_name
        }
