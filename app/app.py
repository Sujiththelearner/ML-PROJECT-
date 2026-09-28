"""
Skill Gap Analyzer – ML-Based Career Prediction and Skill Gap Recommendation System
Department: Computer Science and Engineering
Streamlit Interactive Multi-Page Application with Dedicated Navigation Hub
"""

import os
import sys
import pandas as pd
import numpy as np
import streamlit as st

# Add project root to sys.path to access src modules
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.predict import CareerPredictor
from src.skill_gap import SkillGapAnalyzer
from src.recommendations import RecommendationEngine

# Page configuration
st.set_page_config(
    page_title="Skill Gap Analyzer | AI Career Platform",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom SaaS/EdTech Styling
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.08) 0%, rgba(59, 130, 246, 0.12) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 20px;
        padding: 40px 32px;
        text-align: center;
        margin-bottom: 32px;
        position: relative;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(37, 99, 235, 0.12);
        color: #2563eb;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 6px 16px;
        border-radius: 9999px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 16px;
        border: 1px solid rgba(37, 99, 235, 0.2);
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        color: #4b5563;
        margin-bottom: 16px;
    }
    
    .hero-quote {
        font-size: 1.1rem;
        font-style: italic;
        color: #6b7280;
        max-width: 650px;
        margin: 0 auto 24px auto;
        line-height: 1.6;
    }

    /* Metric Cards */
    .metric-chip {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 20px;
        text-align: center;
    }

    /* Navigation Card */
    .nav-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        transition: all 0.25s ease-in-out;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .nav-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 12px 20px -3px rgba(59, 130, 246, 0.15);
        transform: translateY(-3px);
    }
    
    .nav-card-icon {
        font-size: 2.2rem;
        margin-bottom: 14px;
        display: inline-block;
    }
    
    .nav-card-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .nav-card-desc {
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.5;
        margin-bottom: 16px;
        flex-grow: 1;
    }

    .badge-tag {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    .badge-blue { background: #dbeafe; color: #1e40af; }
    .badge-green { background: #dcfce7; color: #15803d; }
    .badge-purple { background: #f3e8ff; color: #7e22ce; }
    .badge-amber { background: #fef3c7; color: #b45309; }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "page" not in st.session_state:
    st.session_state["page"] = "🧭 Navigation Hub"

if "skills" not in st.session_state:
    st.session_state["skills"] = {
        "Python": 3.0, "Java": 2.0, "SQL": 3.5, "Git": 3.0, "HTML_CSS": 2.0,
        "JavaScript": 2.0, "Machine_Learning": 2.5, "Statistics": 3.0,
        "Data_Visualization": 3.0, "Algorithms_OOP": 3.0
    }

if "prediction_result" not in st.session_state:
    st.session_state["prediction_result"] = None

if "gap_result" not in st.session_state:
    st.session_state["gap_result"] = None

if "recommendations" not in st.session_state:
    st.session_state["recommendations"] = None

# Sidebar Setup
st.sidebar.title("🧭 Skill Gap Analyzer")
st.sidebar.caption("AI-Powered Career Intelligence Platform")

PAGES = [
    "🧭 Navigation Hub",
    "📝 My Skills",
    "🎯 Career Prediction",
    "📊 Skill Gap Analysis",
    "💡 Recommendations",
    "🔬 Model Insights",
    "📖 About Project"
]

selected_page = st.sidebar.radio("Direct Access", PAGES, index=PAGES.index(st.session_state["page"]))
if selected_page != st.session_state["page"]:
    st.session_state["page"] = selected_page
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("🔬 System Health")
st.sidebar.markdown("""
* **ML Model**: Logistic Regression
* **Test Accuracy**: **98.33%**
* **Cross-Validation**: **99.00%**
* **Benchmark**: O*NET 28.0 Database
* **Dataset Size**: 1,500 Profiles
""")

def switch_to(page_name):
    st.session_state["page"] = page_name
    st.rerun()

# ==============================================================================
# DEDICATED NAVIGATION PAGE / HUB
# ==============================================================================
if st.session_state["page"] == "🧭 Navigation Hub":
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">✨ AI-Powered Career Intelligence</div>
        <div class="hero-title">SKILL GAP ANALYZER</div>
        <div class="hero-subtitle">Intelligent Career Prediction & Quantitative Skill Gap Recommendation System</div>
        <div class="hero-quote">
            "Discover your career path. Understand your skill gaps. Build the skills that matter."
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero Action Strip
    hero_col1, hero_col2, hero_col3 = st.columns([1, 2, 1])
    with hero_col2:
        if st.button("🚀 Start Skill Analysis Now", type="primary", use_container_width=True):
            switch_to("📝 My Skills")

    st.markdown("<br>", unsafe_allow_html=True)

    # Platform Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🎯 Target Careers", "5 Core Roles", "Software, Web, Data, ML, Java")
    m2.metric("📊 Benchmark Source", "O*NET 28.0", "U.S. Dept of Labor")
    m3.metric("🧠 ML Generalization", "98.33%", "Test Set Accuracy")
    m4.metric("📐 Gap Quantification", "Weighted Metric", "Capped Fulfillment Ratio")

    st.markdown("---")
    st.markdown("### 🗂️ Explore Platform Modules")
    st.caption("Select any module below to begin your analysis, explore predictions, or inspect machine learning metrics.")

    # 6 Interactive Navigation Cards (3x2 Grid)
    row1_col1, row1_col2, row1_col3 = st.columns(3)

    # Card 1: Career Prediction
    with row1_col1:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-blue">ML Inference</span><br>
                <span class="nav-card-icon">🎯</span>
                <div class="nav-card-title">1. Career Prediction</div>
                <div class="nav-card-desc">
                    Predict your optimal career match among 5 industry roles using our trained multi-class classifier with confidence probabilities.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Career Prediction ➔", key="nav_btn_pred", use_container_width=True):
            switch_to("🎯 Career Prediction")

    # Card 2: Skill Gap Analysis
    with row1_col2:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-amber">Gap Quantification</span><br>
                <span class="nav-card-icon">📊</span>
                <div class="nav-card-title">2. Skill Gap Analysis</div>
                <div class="nav-card-desc">
                    Discover your exact strengths, weak points, and missing skills compared against real-world O*NET occupational standards.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Skill Gap Analysis ➔", key="nav_btn_gap", use_container_width=True):
            switch_to("📊 Skill Gap Analysis")

    # Card 3: My Skills
    with row1_col3:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-green">Assessment Hub</span><br>
                <span class="nav-card-icon">📝</span>
                <div class="nav-card-title">3. My Skills</div>
                <div class="nav-card-desc">
                    Enter and customize your proficiency levels (0–5) across 10 core technical competencies, or load one-click student presets.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Manage My Skills ➔", key="nav_btn_skills", use_container_width=True):
            switch_to("📝 My Skills")

    st.markdown("<br>", unsafe_allow_html=True)
    row2_col1, row2_col2, row2_col3 = st.columns(3)

    # Card 4: Recommendations
    with row2_col1:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-purple">Actionable Roadmaps</span><br>
                <span class="nav-card-icon">💡</span>
                <div class="nav-card-title">4. Recommendations</div>
                <div class="nav-card-desc">
                    Receive prioritized learning checklists, capstone project ideas, and vetted free documentation resources tailored to your deficits.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Recommendations ➔", key="nav_btn_rec", use_container_width=True):
            switch_to("💡 Recommendations")

    # Card 5: Model Insights
    with row2_col2:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-blue">Performance Analytics</span><br>
                <span class="nav-card-icon">🔬</span>
                <div class="nav-card-title">5. Model Insights</div>
                <div class="nav-card-desc">
                    Inspect actual empirical model comparisons, 5-fold cross validation scores, confusion matrix, and feature importances.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Inspect Model Insights ➔", key="nav_btn_insights", use_container_width=True):
            switch_to("🔬 Model Insights")

    # Card 6: About Project
    with row2_col3:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-green">Academic Documentation</span><br>
                <span class="nav-card-icon">📖</span>
                <div class="nav-card-title">6. About Project</div>
                <div class="nav-card-desc">
                    Read the project architecture, O*NET SOC mapping justification, mathematical formula breakdown, and college viva preparation.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Read Project Overview ➔", key="nav_btn_about", use_container_width=True):
            switch_to("📖 About Project")

# ==============================================================================
# PAGE 2: MY SKILLS (ASSESSMENT)
# ==============================================================================
elif st.session_state["page"] == "📝 My Skills":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📝 My Skills Assessment")
    st.markdown("Rate your current proficiency across technical competencies from **0.0** (No experience) to **5.0** (Expert mastery).")

    st.markdown("##### ⚡ Quick Presets (Demo / Test Profiles):")
    preset_choice = st.selectbox(
        "Choose a preset profile to instantly test the system:",
        [
            "Custom (Current Values)",
            "Sample: Aspiring Data Analyst",
            "Sample: Aspiring ML Engineer",
            "Sample: Aspiring Web Developer",
            "Sample: Aspiring Java Developer",
            "Sample: Aspiring Software Developer"
        ]
    )

    if preset_choice == "Sample: Aspiring Data Analyst":
        st.session_state["skills"] = {"Python": 3.5, "Java": 1.0, "SQL": 4.5, "Git": 3.0, "HTML_CSS": 1.0, "JavaScript": 1.5, "Machine_Learning": 2.5, "Statistics": 4.5, "Data_Visualization": 4.5, "Algorithms_OOP": 2.5}
    elif preset_choice == "Sample: Aspiring ML Engineer":
        st.session_state["skills"] = {"Python": 4.8, "Java": 2.0, "SQL": 4.0, "Git": 4.0, "HTML_CSS": 1.0, "JavaScript": 1.5, "Machine_Learning": 4.8, "Statistics": 4.5, "Data_Visualization": 3.5, "Algorithms_OOP": 4.0}
    elif preset_choice == "Sample: Aspiring Web Developer":
        st.session_state["skills"] = {"Python": 2.0, "Java": 1.5, "SQL": 3.0, "Git": 4.0, "HTML_CSS": 4.8, "JavaScript": 4.8, "Machine_Learning": 1.0, "Statistics": 1.5, "Data_Visualization": 2.5, "Algorithms_OOP": 3.0}
    elif preset_choice == "Sample: Aspiring Java Developer":
        st.session_state["skills"] = {"Python": 2.0, "Java": 4.8, "SQL": 4.0, "Git": 4.0, "HTML_CSS": 2.0, "JavaScript": 2.5, "Machine_Learning": 1.0, "Statistics": 2.0, "Data_Visualization": 1.5, "Algorithms_OOP": 4.8}
    elif preset_choice == "Sample: Aspiring Software Developer":
        st.session_state["skills"] = {"Python": 3.5, "Java": 4.0, "SQL": 3.5, "Git": 4.5, "HTML_CSS": 2.5, "JavaScript": 3.0, "Machine_Learning": 1.5, "Statistics": 2.5, "Data_Visualization": 2.0, "Algorithms_OOP": 4.5}

    st.markdown("---")
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("🛠️ Core Programming & Architecture")
        python_val = st.slider("🐍 Python", 0.0, 5.0, float(st.session_state["skills"]["Python"]), 0.5)
        java_val = st.slider("☕ Java", 0.0, 5.0, float(st.session_state["skills"]["Java"]), 0.5)
        sql_val = st.slider("🗄️ SQL & Databases", 0.0, 5.0, float(st.session_state["skills"]["SQL"]), 0.5)
        git_val = st.slider("🐙 Git & Version Control", 0.0, 5.0, float(st.session_state["skills"]["Git"]), 0.5)
        algo_val = st.slider("📐 Data Structures, Algorithms & OOP", 0.0, 5.0, float(st.session_state["skills"]["Algorithms_OOP"]), 0.5)

    with col_right:
        st.subheader("🌐 Web, Data & Intelligence")
        html_val = st.slider("🎨 HTML5 & CSS3", 0.0, 5.0, float(st.session_state["skills"]["HTML_CSS"]), 0.5)
        js_val = st.slider("⚡ JavaScript", 0.0, 5.0, float(st.session_state["skills"]["JavaScript"]), 0.5)
        ml_val = st.slider("🤖 Machine Learning", 0.0, 5.0, float(st.session_state["skills"]["Machine_Learning"]), 0.5)
        stats_val = st.slider("📈 Statistics & Probability", 0.0, 5.0, float(st.session_state["skills"]["Statistics"]), 0.5)
        viz_val = st.slider("📊 Data Visualization (Tableau/Power BI)", 0.0, 5.0, float(st.session_state["skills"]["Data_Visualization"]), 0.5)

    current_skills = {
        "Python": python_val, "Java": java_val, "SQL": sql_val, "Git": git_val,
        "HTML_CSS": html_val, "JavaScript": js_val, "Machine_Learning": ml_val,
        "Statistics": stats_val, "Data_Visualization": viz_val, "Algorithms_OOP": algo_val
    }
    st.session_state["skills"] = current_skills

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Execute ML Prediction & Gap Analysis", type="primary", use_container_width=True):
        with st.spinner("Analyzing profile with trained ML Pipeline..."):
            predictor = CareerPredictor()
            pred_res = predictor.predict(current_skills)
            st.session_state["prediction_result"] = pred_res

            analyzer = SkillGapAnalyzer()
            gap_res = analyzer.analyze(current_skills, pred_res["predicted_career"])
            st.session_state["gap_result"] = gap_res

            engine = RecommendationEngine()
            rec_res = engine.generate(gap_res)
            st.session_state["recommendations"] = rec_res

            switch_to("🎯 Career Prediction")

# ==============================================================================
# PAGE 3: CAREER PREDICTION
# ==============================================================================
elif st.session_state["page"] == "🎯 Career Prediction":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("🎯 Machine Learning Career Prediction")

    if st.session_state["prediction_result"] is None:
        st.warning("Please complete your skill assessment first.")
        if st.button("Go to My Skills Assessment", type="primary"):
            switch_to("📝 My Skills")
    else:
        pred = st.session_state["prediction_result"]
        career = pred["predicted_career"]
        conf = pred["confidence"]
        probs = pred["probabilities"]

        st.success(f"### Most Suitable Career Role: **{career}**")
        st.markdown(f"**Model Confidence:** `{conf:.2f}%` &nbsp;|&nbsp; **Algorithm:** `{pred['model_used']}` &nbsp;|&nbsp; **Validation Accuracy:** `98.33%`")

        st.markdown("---")
        st.subheader("📊 Probability Distribution Across Career Roles")
        prob_df = pd.DataFrame(list(probs.items()), columns=["Career Role", "Probability (%)"])
        st.bar_chart(prob_df.set_index("Career Role"), height=300)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 💡 Decision Boundary Explanation:")
            st.markdown(f"""
            The Machine Learning model evaluated your multi-dimensional skill input against our O*NET-trained boundaries.
            Your unique strength profile aligns with the highest empirical density for **{career}**.
            """)
        with col2:
            st.markdown("#### 🚀 Next Step:")
            st.markdown("Quantify your skill gap against the official benchmark requirements.")
            if st.button("📊 View Skill Gap Analysis", type="primary", use_container_width=True):
                switch_to("📊 Skill Gap Analysis")

# ==============================================================================
# PAGE 4: SKILL GAP ANALYSIS
# ==============================================================================
elif st.session_state["page"] == "📊 Skill Gap Analysis":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📊 Empirical Skill Gap Analysis")

    if st.session_state["gap_result"] is None:
        st.warning("Please run the skill assessment and prediction first.")
        if st.button("Go to My Skills Assessment", type="primary"):
            switch_to("📝 My Skills")
    else:
        gap = st.session_state["gap_result"]
        match_pct = gap["match_percentage"]
        target = gap["target_career"]
        matched = gap["matched_skills"]
        weak = gap["weak_skills"]
        missing = gap["missing_skills"]

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Target Career", target)
        c2.metric("Skill Match Score", f"{match_pct}%")
        c3.metric("Matched Skills", len(matched))
        c4.metric("Actionable Gaps", len(weak) + len(missing))

        st.progress(match_pct / 100.0)

        st.markdown("---")
        st.subheader("📈 Student Level vs. O*NET Industry Requirement")
        comp_data = []
        for s in matched + weak + missing:
            comp_data.append({
                "Skill": s["skill"],
                "Your Proficiency": s["student_level"],
                "Industry Requirement": s["required_level"]
            })
        comp_df = pd.DataFrame(comp_data).set_index("Skill")
        st.bar_chart(comp_df, height=350)

        st.markdown("---")
        st.subheader("📋 Skill Classification Breakdown")

        tab1, tab2, tab3 = st.tabs([
            f"🟢 Matched Skills ({len(matched)})",
            f"🟡 Weak Skills ({len(weak)})",
            f"🔴 Missing Skills ({len(missing)})"
        ])

        with tab1:
            if matched:
                st.markdown("You meet or exceed the benchmark requirements for these skills:")
                for s in matched:
                    st.success(f"**{s['skill']}**: Your Level: `{s['student_level']}` / Benchmark: `{s['required_level']}`")
            else:
                st.info("No skills currently match the industry benchmark.")

        with tab2:
            if weak:
                st.markdown("You have basic knowledge, but require improvement to reach benchmark:")
                for s in weak:
                    st.warning(f"**{s['skill']}**: Your Level: `{s['student_level']}` / Benchmark: `{s['required_level']}` (Deficit: **-{s['gap']}**)")
            else:
                st.info("No weak skills detected.")

        with tab3:
            if missing:
                st.markdown("You have zero rated experience in these essential skills:")
                for s in missing:
                    st.error(f"**{s['skill']}**: Benchmark Requirement: `{s['required_level']}` (Critical Gap: **-{s['gap']}**)")
            else:
                st.info("Great job! You have experience across all required skills.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💡 View Personalized Recommendations", type="primary", use_container_width=True):
            switch_to("💡 Recommendations")

# ==============================================================================
# PAGE 5: RECOMMENDATIONS
# ==============================================================================
elif st.session_state["page"] == "💡 Recommendations":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("💡 Personalized Skill Recommendations")

    if st.session_state["recommendations"] is None or st.session_state["gap_result"] is None:
        st.warning("Please complete the assessment and gap analysis first.")
        if st.button("Go to My Skills Assessment", type="primary"):
            switch_to("📝 My Skills")
    else:
        recs = st.session_state["recommendations"]
        target = st.session_state["gap_result"]["target_career"]
        match_score = st.session_state["gap_result"]["match_percentage"]

        st.markdown(f"Curated learning plan to achieve **100% readiness** for your predicted role: **{target}** (Current Match: `{match_score}%`).")

        if not recs:
            st.balloons()
            st.success("🎉 Outstanding! You have zero skill gaps for this career profile. You are industry-ready!")
        else:
            st.info(f"Identified **{len(recs)} technical competencies** that require focused development.")

            for idx, item in enumerate(recs, 1):
                badge_type = "🔴 Critical Missing" if item["status"] == "Missing" else "🟡 Needs Improvement"
                with st.expander(f"{idx}. {item['skill']} — [{badge_type} | Gap: -{item['gap']} pts]", expanded=(idx <= 2)):
                    st.markdown(f"**🎯 Why this skill matters:** {item['importance']}")
                    st.markdown("**📋 Actionable Step-by-Step Learning Roadmap:**")
                    for step in item["action_steps"]:
                        st.markdown(f"- [ ] {step}")
                    st.markdown(f"**🛠️ Recommended Capstone Project:** {item['project_idea']}")
                    st.markdown(f"**🔗 Recommended Resources:** `{item['resources']}`")

        st.markdown("---")
        col_restart, col_share = st.columns(2)
        with col_restart:
            if st.button("🔄 Retake Skill Assessment", use_container_width=True):
                switch_to("📝 My Skills")
        with col_share:
            if st.button("🏠 Back to Navigation Hub", use_container_width=True):
                switch_to("🧭 Navigation Hub")

# ==============================================================================
# PAGE 6: MODEL INSIGHTS
# ==============================================================================
elif st.session_state["page"] == "🔬 Model Insights":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("🔬 Machine Learning Model Insights & Evaluation")
    st.markdown("Detailed verification of model comparison, cross-validation, confusion matrix, and feature importances.")

    # 1. Model Comparison Table
    metrics_path = os.path.join(ROOT_DIR, "results", "metrics", "model_comparison.csv")
    if os.path.exists(metrics_path):
        st.subheader("📊 Model Comparison Table (Trained & Evaluated)")
        comp_df = pd.read_csv(metrics_path)
        st.dataframe(comp_df, use_container_width=True)
    
    st.markdown("---")

    # 2. Plots Row
    col_cm, col_fi = st.columns(2)

    with col_cm:
        st.subheader("🎯 Test Set Confusion Matrix")
        cm_path = os.path.join(ROOT_DIR, "results", "plots", "best_model_confusion_matrix.png")
        if os.path.exists(cm_path):
            st.image(cm_path, caption="Confusion Matrix on Unseen Test Data (300 samples)")
        else:
            st.info("Confusion matrix plot not found.")

    with col_fi:
        st.subheader("⚖️ Skill Feature Importance")
        fi_path = os.path.join(ROOT_DIR, "results", "plots", "feature_importance.png")
        if os.path.exists(fi_path):
            st.image(fi_path, caption="Feature Importance across Technical Competencies")
        else:
            st.info("Feature importance plot not found.")

    st.markdown("---")
    st.subheader("📈 Exploratory Data Visualizations")
    col_heat, col_corr = st.columns(2)
    with col_heat:
        heat_path = os.path.join(ROOT_DIR, "results", "plots", "eda_career_profiles_heatmap.png")
        if os.path.exists(heat_path):
            st.image(heat_path, caption="Average Skill Proficiencies across Target Careers")
    with col_corr:
        corr_path = os.path.join(ROOT_DIR, "results", "plots", "eda_feature_correlation.png")
        if os.path.exists(corr_path):
            st.image(corr_path, caption="Feature Correlation Matrix")

# ==============================================================================
# PAGE 7: ABOUT PROJECT
# ==============================================================================
elif st.session_state["page"] == "📖 About Project":
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📖 About Skill Gap Analyzer")
    st.markdown("Comprehensive overview of project methodology, dataset provenance, mathematical formulation, and architecture.")

    st.markdown("### 🏛️ System Architecture")
    st.markdown("""
    ```text
    O*NET 28.0 Database ──► Data Preprocessing ──► 1,500 Balanced Dataset
                                                          │
    Streamlit Web App ◄── Best Model Pipeline ◄── Model Comparison (4 Models)
            │                  (98.33% Acc)
            ▼
    Skill Gap Analyzer ──► Weighted Fulfillment ──► Actionable Recommendations
    ```
    """)

    st.markdown("### 🎯 Career Categories & O*NET SOC Codes")
    st.markdown("""
    | Career Role | O*NET-SOC Code | Official O*NET Title | Role Focus |
    | :--- | :--- | :--- | :--- |
    | **Software Developer** | `15-1252.00` | Software Developers | Algorithms, System Architecture, Git |
    | **Web Developer** | `15-1254.00` | Web Developers | HTML5, CSS3, JavaScript, Web APIs |
    | **Data Analyst** | `15-2051.01` | Business Intelligence Analysts | SQL, Statistics, BI Dashboards |
    | **ML Engineer** | `15-2051.00` | Data Scientists | Python, ML Modeling, Data Pipelines |
    | **Java Developer** | `15-1251.00` | Computer Programmers | Core Java, Spring/Hibernate, OOP |
    """)

    st.markdown("### 📐 Mathematical Formulation for Skill Gap Score")
    st.latex(r"\text{Fulfillment}_i = \min\left(1.0, \frac{S_i}{R_i}\right)")
    st.latex(r"\text{Skill Match \%} = \left( \frac{\sum_{i=1}^{n} \text{Fulfillment}_i \times R_i}{\sum_{i=1}^{n} R_i} \right) \times 100")
    st.markdown(r"""
    * $S_i$: Student's proficiency level for skill $i \in [0.0, 5.0]$.
    * $R_i$: O*NET benchmark requirement for skill $i \in [0.0, 5.0]$.
    * Capped at $1.0$ so high proficiency in one skill cannot falsely mask deficits in another required competency.
    """)
