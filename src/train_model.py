"""
Phase 8 to 13: Feature Engineering, Model Training, Comparison & Evaluation
Trains and compares Logistic Regression, Decision Tree, Random Forest, and KNN.
Saves metrics, confusion matrix, feature importance, and the best trained model.
"""

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

DATASET_PATH = os.path.join("dataset", "processed", "student_skills_dataset.csv")
MODEL_DIR = "models"
METRICS_DIR = os.path.join("results", "metrics")
PLOTS_DIR = os.path.join("results", "plots")
BEST_MODEL_PATH = os.path.join(MODEL_DIR, "career_model.pkl")

def train_and_evaluate_models():
    print("=" * 70)
    print("Phase 8-13: Model Training, Comparison & Evaluation")
    print("=" * 70)

    # 1. Load Data
    df = pd.read_csv(DATASET_PATH)
    X = df.drop(columns=["Career"])
    y = df["Career"]
    feature_names = list(X.columns)

    print(f"\n[1] Features (X): {len(feature_names)} skills")
    print(f"    Classes (y): {sorted(list(y.unique()))}")

    # 2. Train-Test Split (80% Train, 20% Test) - Stratified to prevent leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n[2] Train/Test Split (Stratified 80/20):")
    print(f"    Training samples: {len(X_train):,} ({len(X_train)/len(X):.0%})")
    print(f"    Testing samples : {len(X_test):,} ({len(X_test)/len(X):.0%})")

    # 3. Define Models to Train and Compare
    candidate_models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=6, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
    }

    # 4. Train, Cross-Validate, and Test Each Model
    os.makedirs(METRICS_DIR, exist_ok=True)
    os.makedirs(PLOTS_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)

    comparison_results = []
    trained_pipelines = {}

    print("\n[3] Model Training & 5-Fold Cross-Validation:")
    for name, model in candidate_models.items():
        # Pipeline encapsulates StandardScaler to prevent data leakage
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", model)
        ])
        
        # 5-Fold Cross Validation on Training Data
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="accuracy")
        
        # Train on entire Training Set
        pipeline.fit(X_train, y_train)
        trained_pipelines[name] = pipeline

        # Predict on Unseen Test Set
        y_pred = pipeline.predict(X_test)

        # Evaluation Metrics
        test_acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="macro")
        rec = recall_score(y_test, y_pred, average="macro")
        f1 = f1_score(y_test, y_pred, average="macro")

        comparison_results.append({
            "Model": name,
            "CV Accuracy (Train)": round(cv_scores.mean(), 4),
            "Test Accuracy": round(test_acc, 4),
            "Precision (Macro)": round(prec, 4),
            "Recall (Macro)": round(rec, 4),
            "F1-Score (Macro)": round(f1, 4)
        })

    # Save Comparison Table
    comparison_df = pd.DataFrame(comparison_results).sort_values(by="F1-Score (Macro)", ascending=False)
    comparison_path = os.path.join(METRICS_DIR, "model_comparison.csv")
    comparison_df.to_csv(comparison_path, index=False)

    print("\n" + "=" * 70)
    print("MODEL COMPARISON TABLE (Ranked by Test F1-Score):")
    print("=" * 70)
    print(comparison_df.to_string(index=False))
    print(f"\n[SAVED] Comparison metrics saved to: {comparison_path}")

    # 5. Select Winning Model
    best_model_name = comparison_df.iloc[0]["Model"]
    best_pipeline = trained_pipelines[best_model_name]
    print(f"\nWinner Selected: >> {best_model_name} << based on highest generalization performance.")

    # 6. Detailed Evaluation of Winning Model
    y_test_pred = best_pipeline.predict(X_test)
    class_labels = sorted(list(y.unique()))
    
    print("\n" + "=" * 70)
    print(f"DETAILED CLASSIFICATION REPORT FOR {best_model_name.upper()}:")
    print("=" * 70)
    print(classification_report(y_test, y_test_pred, target_names=class_labels, digits=4))

    # 7. Plot Confusion Matrix
    cm = confusion_matrix(y_test, y_test_pred, labels=class_labels)
    plt.figure(figsize=(9, 7))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_labels,
        yticklabels=class_labels
    )
    plt.title(f"Confusion Matrix: {best_model_name} (Test Set)", fontsize=14, pad=15)
    plt.xlabel("Predicted Career", fontsize=12)
    plt.ylabel("Actual Career", fontsize=12)
    plt.tight_layout()
    cm_path = os.path.join(PLOTS_DIR, "best_model_confusion_matrix.png")
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"[SAVED] Confusion Matrix Plot -> {cm_path}")

    # 8. Feature Importance Plot (Using Random Forest for Feature Interpretability)
    rf_pipeline = trained_pipelines["Random Forest"]
    rf_classifier = rf_pipeline.named_steps["classifier"]
    importances = rf_classifier.feature_importances_
    feat_df = pd.DataFrame({
        "Skill": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(feat_df["Skill"], feat_df["Importance"], color="#2b5c8f")
    plt.title("Skill Feature Importance (Random Forest)", fontsize=14, pad=15)
    plt.xlabel("Relative Importance Score", fontsize=12)
    plt.ylabel("Skill Feature", fontsize=12)
    plt.tight_layout()
    feat_path = os.path.join(PLOTS_DIR, "feature_importance.png")
    plt.savefig(feat_path, dpi=300)
    plt.close()
    print(f"[SAVED] Feature Importance Plot -> {feat_path}")

    # 9. Save Best Model to models/career_model.pkl
    model_payload = {
        "pipeline": best_pipeline,
        "model_name": best_model_name,
        "feature_names": feature_names,
        "classes": class_labels,
        "metrics": comparison_df.iloc[0].to_dict()
    }
    joblib.dump(model_payload, BEST_MODEL_PATH)
    print(f"\n[SAVED] Winning model and preprocessing pipeline saved to: {BEST_MODEL_PATH}")
    print("\n" + "=" * 70)
    print("Model training, comparison, evaluation & persistence 100% COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    train_and_evaluate_models()
