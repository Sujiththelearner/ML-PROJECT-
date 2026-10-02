"""
Skill Gap Analyzer – AI-Powered Career Intelligence Platform
Department: Computer Science and Engineering
Interactive Multi-Page Streamlit Application
"""

import os
import sys
import pandas as pd
import numpy as np
import streamlit as st

# Add project root to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.predict import CareerPredictor
from src.skill_gap import SkillGapAnalyzer
from src.recommendations import RecommendationEngine
from src.job_roles_data import JOB_ROLES_CATALOG, get_job_role_info
from src.certificate_parser import save_uploaded_certificate, parse_certificate
from src.feature_engineering import evaluate_profile_to_features, FEATURE_NAMES

# Page Configuration
st.set_page_config(
    page_title="Skill Gap Analyzer | AI Career Platform",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (SaaS / Modern EdTech Design)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.08) 0%, rgba(59, 130, 246, 0.12) 100%);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 20px;
        padding: 40px 32px;
        text-align: center;
        margin-bottom: 28px;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(37, 99, 235, 0.12);
        color: #2563eb;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 6px 18px;
        border-radius: 9999px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 14px;
        border: 1px solid rgba(37, 99, 235, 0.25);
    }
    .hero-title {
        font-size: 2.7rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        color: #4b5563;
        margin-bottom: 14px;
    }
    .hero-quote {
        font-size: 1.1rem;
        font-style: italic;
        color: #6b7280;
        max-width: 680px;
        margin: 0 auto 20px auto;
        line-height: 1.6;
    }

    /* Navigation & Feature Cards */
    .nav-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        min-height: 220px;
        transition: all 0.25s ease-in-out;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 12px;
    }
    .nav-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 12px 22px -3px rgba(59, 130, 246, 0.16);
        transform: translateY(-3px);
    }
    .nav-card-icon {
        font-size: 2.2rem;
        margin-bottom: 10px;
        display: inline-block;
    }
    .nav-card-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 6px;
    }
    .nav-card-desc {
        font-size: 0.92rem;
        color: #64748b;
        line-height: 1.5;
        flex-grow: 1;
        margin-bottom: 12px;
    }

    .badge-tag {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .badge-blue { background: #dbeafe; color: #1e40af; }
    .badge-green { background: #dcfce7; color: #15803d; }
    .badge-purple { background: #f3e8ff; color: #7e22ce; }
    .badge-amber { background: #fef3c7; color: #b45309; }

    /* Section Cards */
    .info-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 18px 20px;
        margin-bottom: 16px;
    }
    .status-badge {
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.82rem;
        display: inline-block;
    }
    .status-green { background: #dcfce7; color: #166534; }
    .status-amber { background: #fef3c7; color: #92400e; }
    .status-red { background: #fee2e2; color: #991b1b; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Session State Initialization
# ------------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "🧭 Navigation Hub"

if "user_profile" not in st.session_state:
    st.session_state["user_profile"] = {
        "target_job": "Data Analyst",
        "target_job_custom": "",
        "career_focus": ["Getting my first job", "Building projects"],
        "career_goal": "Secure an entry-level position as a Data Analyst",
        "education": {
            "level": "Undergraduate",
            "degree": "B.E. / B.Tech",
            "department": "Computer Science and Engineering",
            "year": "3rd Year"
        },
        "experience_summary": {
            "years_exp": "0–1 years",
            "internships": "1 internship completed"
        },
        "skills_experience": {
            "Python": {
                "practical_level": "Personal projects",
                "description": "Used Pandas and Matplotlib for data cleaning, EDA, and basic statistical plots.",
                "project_count": "2",
                "has_cert": True,
                "cert_name": "Python for Data Science",
                "cert_org": "Coursera"
            },
            "SQL": {
                "practical_level": "Internship / real-world experience",
                "description": "Wrote multi-table joins, subqueries, and window functions to query e-commerce schemas.",
                "project_count": "3",
                "has_cert": True,
                "cert_name": "SQL Intermediate Assessment",
                "cert_org": "HackerRank"
            },
            "Statistics": {
                "practical_level": "Academic projects",
                "description": "Learned probability distributions, hypothesis testing, and correlation analysis.",
                "project_count": "1",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "Data_Visualization": {
                "practical_level": "Personal projects",
                "description": "Built interactive sales dashboards in Power BI and plotted visual distributions.",
                "project_count": "2",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "Git": {
                "practical_level": "Academic projects",
                "description": "Familiar with git init, commit, branching, and pushing code to GitHub repositories.",
                "project_count": "2",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "Algorithms_OOP": {
                "practical_level": "Academic projects",
                "description": "Completed coursework in Data Structures, sorting algorithms, and object-oriented principles.",
                "project_count": "1",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "Java": {
                "practical_level": "Beginner / Learning",
                "description": "Studied basic syntax, classes, and loops during introductory college course.",
                "project_count": "0",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "HTML_CSS": {
                "practical_level": "Beginner / Learning",
                "description": "Basic tags and simple webpage layout.",
                "project_count": "0",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "JavaScript": {
                "practical_level": "No experience",
                "description": "",
                "project_count": "0",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            },
            "Machine_Learning": {
                "practical_level": "Beginner / Learning",
                "description": "Implemented linear regression and decision trees using Scikit-Learn.",
                "project_count": "1",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            }
        },
        "projects": [
            {
                "name": "E-Commerce Customer Churn Analysis",
                "description": "Analyzed customer transaction patterns using SQL and Pandas to identify retention bottlenecks.",
                "technologies": "SQL, Python, Pandas, Power BI",
                "role": "Data Analyst"
            }
        ],
        "uploaded_certificates": []
    }

if "analysis_results" not in st.session_state:
    st.session_state["analysis_results"] = None

def switch_to(page_name):
    st.session_state["page"] = page_name
    st.rerun()

# ------------------------------------------------------------------------------
# Sidebar Navigation (Icon & Card Based)
# ------------------------------------------------------------------------------
st.sidebar.markdown("### 🧭 Skill Gap Analyzer")
st.sidebar.caption("AI-Powered Career Intelligence Platform")

NAVIGATION_ITEMS = [
    {"name": "🧭 Navigation Hub", "desc": "Start your career assessment"},
    {"name": "📝 My Skills & Experience", "desc": "Tell us about your background"},
    {"name": "🎯 Career Prediction", "desc": "Explore matching careers"},
    {"name": "📊 Skill Gap Analysis", "desc": "Identify required skills"},
    {"name": "💡 Recommendations", "desc": "Personalized learning suggestions"},
    {"name": "🔬 Model Insights", "desc": "Understand how AI analysis works"},
    {"name": "📘 About Project", "desc": "System and methodology"}
]

st.sidebar.markdown("---")
st.sidebar.markdown("**DIRECT ACCESS**")

for item in NAVIGATION_ITEMS:
    is_active = (st.session_state["page"] == item["name"])
    btn_label = f"👉 {item['name']}" if is_active else item['name']
    if st.sidebar.button(btn_label, key=f"side_{item['name']}", use_container_width=True, type="primary" if is_active else "secondary"):
        switch_to(item["name"])

st.sidebar.markdown("---")
st.sidebar.caption("Benchmark Data: O*NET 28.0 (U.S. Dept of Labor)")
st.sidebar.caption("ML Architecture: Calibrated Feature Pipeline (98.33% Acc)")


# ==============================================================================
# 1. NAVIGATION HUB PAGE
# ==============================================================================
if st.session_state["page"] == "🧭 Navigation Hub":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">✨ AI-Powered Career Intelligence</div>
        <div class="hero-title">SKILL GAP ANALYZER</div>
        <div class="hero-subtitle">Intelligent Career Guidance & Qualitative Skill Gap Platform</div>
        <div class="hero-quote">
            "Discover your career path. Understand your skill gaps. Build the skills that matter."
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_btn_l, col_btn_c, col_btn_r = st.columns([1, 2, 1])
    with col_btn_c:
        if st.button("🚀 Start Skill & Career Assessment", type="primary", use_container_width=True):
            switch_to("📝 My Skills & Experience")

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Value Props Strip
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🎯 Job Roles", "15+ Tech Careers", "O*NET Aligned")
    m2.metric("📜 Certificate Parser", "PDF, PNG, JPG", "Smart Extraction")
    m3.metric("🧠 Evidence-Based", "No Number Sliders", "Projects & Experience")
    m4.metric("📈 Learning Roadmap", "Dynamic 5 Phases", "Tailored to Your Gap")

    st.markdown("---")
    st.subheader("🗂️ Explore Platform Modules")
    st.caption("Select any module below to begin your evaluation, upload certifications, or inspect learning roadmaps.")

    # 3x2 Modern Navigation Cards Grid
    r1c1, r1c2, r1c3 = st.columns(3)

    with r1c1:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-blue">Experience Profile</span>
                <span class="nav-card-icon">📝</span>
                <div class="nav-card-title">My Skills & Experience</div>
                <div class="nav-card-desc">
                    Tell us about your background, projects, coursework, and upload your certifications. No artificial numerical scoring.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open My Skills & Experience ➔", key="hub_skills", use_container_width=True):
            switch_to("📝 My Skills & Experience")

    with r1c2:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-green">AI Assessment</span>
                <span class="nav-card-icon">🎯</span>
                <div class="nav-card-title">Career Prediction</div>
                <div class="nav-card-desc">
                    Explore careers matching your actual profile with clear explanations of why your experience aligns with specific roles.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Career Prediction ➔", key="hub_pred", use_container_width=True):
            switch_to("🎯 Career Prediction")

    with r1c3:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-amber">Gap Analysis</span>
                <span class="nav-card-icon">📊</span>
                <div class="nav-card-title">Skill Gap Analysis</div>
                <div class="nav-card-desc">
                    Identify demonstrated vs. missing competencies for your target role, with detailed rationale for every requirement.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Skill Gap Analysis ➔", key="hub_gap", use_container_width=True):
            switch_to("📊 Skill Gap Analysis")

    st.markdown("<br>", unsafe_allow_html=True)
    r2c1, r2c2, r2c3 = st.columns(3)

    with r2c1:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-purple">Roadmaps & Projects</span>
                <span class="nav-card-icon">💡</span>
                <div class="nav-card-title">Recommendations</div>
                <div class="nav-card-desc">
                    Get structured learning roadmaps organized by: Learn, Practice, Build, Certify, and Interview Preparation.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Recommendations ➔", key="hub_rec", use_container_width=True):
            switch_to("💡 Recommendations")

    with r2c2:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-blue">ML Performance</span>
                <span class="nav-card-icon">🔬</span>
                <div class="nav-card-title">Model Insights</div>
                <div class="nav-card-desc">
                    Inspect the machine learning pipeline, 5-fold cross-validation scores, confusion matrix, and feature importances.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Model Insights ➔", key="hub_insights", use_container_width=True):
            switch_to("🔬 Model Insights")

    with r2c3:
        st.markdown("""
        <div class="nav-card">
            <div>
                <span class="badge-tag badge-green">Documentation</span>
                <span class="nav-card-icon">📘</span>
                <div class="nav-card-title">About Project</div>
                <div class="nav-card-desc">
                    Learn about the O*NET database provenance, quantitative fulfillment formula, and college viva preparation notes.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open About Project ➔", key="hub_about", use_container_width=True):
            switch_to("📘 About Project")


# ==============================================================================
# 2. MY SKILLS & EXPERIENCE (EXPERIENCE-BASED FORM + CERTIFICATE UPLOADER)
# ==============================================================================
elif st.session_state["page"] == "📝 My Skills & Experience":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📝 My Skills & Technical Experience")
    st.markdown("""
    Tell us about your background, hands-on experience, projects, and certifications. 
    **You are not asked to rate yourself with arbitrary numerical scores.** The system infers your profile based on real evidence.
    """)

    # Tabbed Experience Input Workflow
    tab_target, tab_skills, tab_projects, tab_certs = st.tabs([
        "1️⃣ Target Job & Background",
        "2️⃣ Practical Skill Experience",
        "3️⃣ Projects Portfolio",
        "4️⃣ 📜 Upload Your Certifications"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: Target Job & Background
    # --------------------------------------------------------------------------
    with tab_target:
        st.subheader("🎯 Career Goal & Academic Profile")
        
        job_options = list(JOB_ROLES_CATALOG.keys()) + ["Other"]
        current_target = st.session_state["user_profile"].get("target_job", "Data Analyst")
        default_idx = job_options.index(current_target) if current_target in job_options else 0
        
        selected_job = st.selectbox(
            "What job role are you preparing for? (Primary Target)",
            job_options,
            index=default_idx
        )
        
        custom_job = ""
        if selected_job == "Other":
            custom_job = st.text_input("Enter your target job title:", value=st.session_state["user_profile"].get("target_job_custom", ""))
            target_job_effective = custom_job if custom_job else "Custom Tech Role"
        else:
            target_job_effective = selected_job

        st.session_state["user_profile"]["target_job"] = target_job_effective
        st.session_state["user_profile"]["target_job_custom"] = custom_job

        # Career Focus Multi-select
        focus_options = [
            "Getting my first job", "Internship preparation", "Campus placement",
            "Switching career", "Improving technical skills", "Becoming job-ready",
            "Preparing for interviews", "Building projects", "Earning certifications", "Higher studies"
        ]
        chosen_focus = st.multiselect(
            "What do you want to focus on?",
            focus_options,
            default=st.session_state["user_profile"].get("career_focus", ["Getting my first job", "Building projects"])
        )
        st.session_state["user_profile"]["career_focus"] = chosen_focus

        career_goal = st.text_input(
            "What is your main career goal?",
            value=st.session_state["user_profile"].get("career_goal", "Secure an entry-level position as a Data Analyst")
        )
        st.session_state["user_profile"]["career_goal"] = career_goal

        st.markdown("---")
        st.subheader("🎓 Education & Experience Level")
        col_ed1, col_ed2 = st.columns(2)
        with col_ed1:
            ed_level = st.selectbox("Education Level", ["Undergraduate", "Postgraduate", "Diploma / Boot Camp", "Working Professional"], index=0)
            degree = st.text_input("Degree & Specialization", value=st.session_state["user_profile"]["education"].get("degree", "B.E. / B.Tech"))
            dept = st.text_input("Department / Major", value=st.session_state["user_profile"]["education"].get("department", "Computer Science and Engineering"))
        with col_ed2:
            curr_year = st.selectbox("Current Year of Study", ["1st Year", "2nd Year", "3rd Year", "Final Year", "Graduated"], index=2)
            years_exp = st.selectbox("Years of Professional Experience", ["0 years (Student/Fresher)", "0–1 years", "1–3 years", "3+ years"], index=1)
            internship = st.selectbox("Internship Experience", ["No internship experience yet", "1 internship completed", "2+ internships completed"], index=1)

        st.session_state["user_profile"]["education"] = {
            "level": ed_level, "degree": degree, "department": dept, "year": curr_year
        }
        st.session_state["user_profile"]["experience_summary"] = {
            "years_exp": years_exp, "internships": internship
        }

    # --------------------------------------------------------------------------
    # TAB 2: Practical Skill Experience (NO SLIDERS)
    # --------------------------------------------------------------------------
    with tab_skills:
        st.subheader("🛠️ Technical Competency Background")
        st.info("💡 For each technical domain, select your practical experience level, completed projects, and any formal certifications.")

        EXPERIENCE_LEVELS = [
            "No experience",
            "Beginner / Learning",
            "Academic projects",
            "Personal projects",
            "Internship / real-world experience",
            "Professional experience"
        ]

        PROJECT_OPTIONS = ["0", "1", "2", "3", "4+"]

        skills_dict = st.session_state["user_profile"].setdefault("skills_experience", {})

        for skill_name in FEATURE_NAMES:
            current_data = skills_dict.setdefault(skill_name, {
                "practical_level": "Beginner / Learning",
                "description": "",
                "project_count": "1",
                "has_cert": False,
                "cert_name": "",
                "cert_org": ""
            })

            with st.expander(f"📌 {skill_name.replace('_', ' ')}", expanded=(skill_name in ["Python", "SQL", "Machine_Learning"])):
                c_lvl, c_count = st.columns([3, 2])
                with c_lvl:
                    p_idx = EXPERIENCE_LEVELS.index(current_data["practical_level"]) if current_data["practical_level"] in EXPERIENCE_LEVELS else 0
                    chosen_lvl = st.selectbox(
                        f"How much practical experience do you have with {skill_name}?",
                        EXPERIENCE_LEVELS,
                        index=p_idx,
                        key=f"lvl_{skill_name}"
                    )
                    current_data["practical_level"] = chosen_lvl

                with c_count:
                    cnt_idx = PROJECT_OPTIONS.index(current_data["project_count"]) if current_data["project_count"] in PROJECT_OPTIONS else 0
                    chosen_count = st.selectbox(
                        f"Projects completed using {skill_name}:",
                        PROJECT_OPTIONS,
                        index=cnt_idx,
                        key=f"cnt_{skill_name}"
                    )
                    current_data["project_count"] = chosen_count

                desc_val = st.text_area(
                    f"Describe your practical experience with {skill_name}:",
                    value=current_data.get("description", ""),
                    placeholder=f"e.g. I used {skill_name} for data preprocessing and built an exploratory dashboard.",
                    key=f"desc_{skill_name}"
                )
                current_data["description"] = desc_val

                c_cert_bool, c_cert_details = st.columns([1, 2])
                with c_cert_bool:
                    has_c = st.radio(
                        f"Certification in {skill_name}?",
                        ["No", "Yes"],
                        index=1 if current_data.get("has_cert") else 0,
                        key=f"cert_bool_{skill_name}"
                    )
                    current_data["has_cert"] = (has_c == "Yes")

                with c_cert_details:
                    if current_data["has_cert"]:
                        c_name = st.text_input("Certification Name:", value=current_data.get("cert_name", ""), key=f"cname_{skill_name}")
                        c_org = st.text_input("Issuing Organization:", value=current_data.get("cert_org", ""), key=f"corg_{skill_name}")
                        current_data["cert_name"] = c_name
                        current_data["cert_org"] = c_org

    # --------------------------------------------------------------------------
    # TAB 3: Projects Portfolio
    # --------------------------------------------------------------------------
    with tab_projects:
        st.subheader("💻 Project Portfolio")
        st.caption("Tell us about real projects you have built. Technologies mentioned here provide direct evidence for your skill profile.")

        existing_projs = st.session_state["user_profile"].setdefault("projects", [])

        if existing_projs:
            st.markdown("##### Existing Project Entries:")
            for idx, p in enumerate(existing_projs):
                st.markdown(f"""
                <div class="info-card">
                    <b>📁 {p['name']}</b> (Role: <i>{p.get('role', 'Developer')}</i>)<br>
                    <span style="color:#64748b;">{p.get('description', '')}</span><br>
                    <small><b>Technologies:</b> <code>{p.get('technologies', '')}</code></small>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"🗑️ Remove Project {idx+1}", key=f"rm_proj_{idx}"):
                    existing_projs.pop(idx)
                    st.rerun()

        st.markdown("---")
        st.markdown("##### ➕ Add a Project to Your Profile:")
        with st.form("add_project_form"):
            new_p_name = st.text_input("Project Name *", placeholder="e.g. AI-Based Fake Internship Detection")
            new_p_desc = st.text_area("Description *", placeholder="e.g. Built an NLP model to classify fraudulent internship postings with 94% accuracy.")
            new_p_tech = st.text_input("Technologies Used *", placeholder="e.g. Python, Machine Learning, Pandas, Scikit-learn, SQL")
            new_p_role = st.text_input("Your Role in Project", placeholder="e.g. Lead ML Developer / Data Analyst")
            submit_proj = st.form_submit_button("Save Project Entry")

            if submit_proj:
                if new_p_name and new_p_desc and new_p_tech:
                    existing_projs.append({
                        "name": new_p_name,
                        "description": new_p_desc,
                        "technologies": new_p_tech,
                        "role": new_p_role
                    })
                    st.success(f"Project '{new_p_name}' successfully added to profile!")
                    st.rerun()
                else:
                    st.warning("Please provide Project Name, Description, and Technologies.")

    # --------------------------------------------------------------------------
    # TAB 4: Upload Your Certifications
    # --------------------------------------------------------------------------
    with tab_certs:
        st.subheader("📜 Upload Your Certifications")
        st.markdown("""
        Upload proof of your technical certificates (PDF, PNG, JPG, JPEG). 
        The system will parse the certificate content to detect issuing organizations, relevant domains, and key technologies.
        """)

        uploaded_file = st.file_uploader(
            "Choose a certificate file (PDF, PNG, JPG, JPEG)",
            type=["pdf", "png", "jpg", "jpeg"]
        )

        if uploaded_file is not None:
            if st.button("➕ Process & Add Certificate", type="primary"):
                with st.spinner("Saving file and analyzing certificate content..."):
                    saved_path = save_uploaded_certificate(uploaded_file)
                    parsed_cert = parse_certificate(saved_path, uploaded_file.name)
                    st.session_state["user_profile"].setdefault("uploaded_certificates", []).append(parsed_cert)
                    st.success(f"Certificate '{uploaded_file.name}' uploaded and analyzed successfully!")
                    st.rerun()

        # Display Uploaded Certificates List
        current_certs = st.session_state["user_profile"].get("uploaded_certificates", [])
        if current_certs:
            st.markdown("---")
            st.markdown("##### 🗃️ Uploaded & Detected Certifications:")
            for idx, c in enumerate(current_certs):
                with st.container():
                    st.markdown(f"""
                    <div class="info-card">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <b>📜 {c['title']}</b>
                            <span class="status-badge status-green">{c.get('status', 'Detected (User-confirmed)')}</span>
                        </div>
                        <p style="margin: 8px 0; color:#475569;">
                            <b>Organization:</b> {c['organization']} &nbsp;|&nbsp; 
                            <b>Domain:</b> {c['domain']} &nbsp;|&nbsp; 
                            <b>File:</b> <code>{c['file_name']}</code> &nbsp;|&nbsp; 
                            <b>Year:</b> {c['year']}
                        </p>
                        <small><b>Detected Skills / Keywords:</b> {', '.join(c.get('detected_skills', []))}</small>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"🗑️ Remove Certificate {idx+1}", key=f"rm_cert_{idx}"):
                        current_certs.pop(idx)
                        st.rerun()
        else:
            st.info("No certificates uploaded yet. Upload a certificate above to boost your skill evidence!")

    # --------------------------------------------------------------------------
    # Master Action: Run AI Analysis
    # --------------------------------------------------------------------------
    st.markdown("<br><hr>", unsafe_allow_html=True)
    if st.button("🚀 Run AI Career & Skill Gap Analysis", type="primary", use_container_width=True):
        # Validation
        target_role = st.session_state["user_profile"].get("target_job", "").strip()
        if not target_role:
            st.error("Please specify your target job in Tab 1 before running the analysis.")
        else:
            with st.spinner("Evaluating profile, extracting evidence, and executing ML models..."):
                # 1. Feature Engineering (Qualitative to ML Features + Evidence)
                fe_result = evaluate_profile_to_features(st.session_state["user_profile"])
                features_dict = fe_result["features_dict"]
                evidence_by_skill = fe_result["evidence_by_skill"]
                overall_evidence = fe_result["overall_evidence"]

                # 2. Career Prediction (via Model Pipeline)
                predictor = CareerPredictor()
                pred_result = predictor.predict(features_dict)

                # 3. Skill Gap Analysis (for Target Job)
                analyzer = SkillGapAnalyzer()
                gap_result = analyzer.analyze(features_dict, target_role, evidence_by_skill)

                # 4. Categorized Recommendations, Focus Areas & Roadmap
                rec_engine = RecommendationEngine()
                categorized_recs = rec_engine.generate_categorized_recommendations(gap_result, st.session_state["user_profile"])
                focus_areas = rec_engine.generate_focus_areas(gap_result, st.session_state["user_profile"])
                roadmap = rec_engine.generate_learning_roadmap(gap_result, st.session_state["user_profile"])

                # Store in Session State
                st.session_state["analysis_results"] = {
                    "features_dict": features_dict,
                    "evidence_by_skill": evidence_by_skill,
                    "overall_evidence": overall_evidence,
                    "prediction": pred_result,
                    "gap_result": gap_result,
                    "categorized_recs": categorized_recs,
                    "focus_areas": focus_areas,
                    "roadmap": roadmap
                }

                switch_to("🎯 Career Prediction")


# ==============================================================================
# 3. CAREER PREDICTION PAGE (NO PROBABILITY GRAPH - STUDENT-FRIENDLY EXPLANATION)
# ==============================================================================
elif st.session_state["page"] == "🎯 Career Prediction":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("🎯 Career Assessment & Suitability")

    if st.session_state["analysis_results"] is None:
        st.warning("Please complete your profile and run the analysis first.")
        if st.button("Go to My Skills & Experience", type="primary"):
            switch_to("📝 My Skills & Experience")
    else:
        res = st.session_state["analysis_results"]
        predicted_career = res["prediction"]["predicted_career"]
        target_job = res["gap_result"]["target_career"]
        evidence_points = res["overall_evidence"]
        role_info = res["gap_result"]["role_info"]

        # Student-Friendly Career Hero
        st.markdown(f"""
        <div class="hero-container" style="padding: 28px 24px; margin-bottom: 24px;">
            <span class="hero-badge">AI Career Alignment Result</span>
            <h2 style="margin: 8px 0; color: #1e3a8a;">Based on your experience, projects, and certifications:</h2>
            <h1 style="color: #2563eb; font-size: 2.6rem; margin: 4px 0;">{predicted_career.upper()}</h1>
            <p style="color: #4b5563; font-size: 1.1rem; max-width: 700px; margin: 0 auto;">
                Target Goal Role: <b>{target_job}</b> &nbsp;|&nbsp; Alignment Confidence: <b>{res['prediction']['confidence']:.1f}%</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("💡 Why this role matches your profile")
        st.markdown("""
        Our AI evaluated your hands-on project portfolio, practical experience levels, and certifications against 
        verified occupational benchmarks. Here is the concrete evidence demonstrating alignment:
        """)

        if evidence_points:
            for ev in evidence_points:
                st.markdown(f"- ✓ {ev}")
        else:
            st.markdown("- ✓ Core computer science coursework and fundamental technical background demonstrated.")

        st.markdown("---")

        # Career Role Information ("What does a [Role] do?")
        st.subheader(f"💼 What does a {target_job} do?")
        st.markdown(f"*{role_info.get('tagline', '')}*")
        st.markdown(f"{role_info.get('description', '')}")

        col_tasks, col_expect = st.columns(2)
        with col_tasks:
            st.markdown("##### 📌 Typical Daily Tasks:")
            for task in role_info.get("daily_tasks", []):
                st.markdown(f"• {task}")

        with col_expect:
            st.markdown("##### 🎯 Entry-Level Expectations:")
            st.info(role_info.get("entry_level_expectations", "Strong foundations in core programming and domain tools."))

            st.markdown("##### 🛠️ Common Industry Tools:")
            tools_chips = " &nbsp;|&nbsp; ".join([f"`{t}`" for t in role_info.get("common_tools", [])])
            st.markdown(tools_chips)

        st.markdown("---")

        # "What Do I Need To Become Job-Ready?"
        st.subheader(f"🚀 What Do I Need To Become Job-Ready for {target_job}?")
        jr_c1, jr_c2, jr_c3 = st.columns(3)
        with jr_c1:
            st.markdown("###### 🔑 CORE SKILLS")
            for cs in role_info.get("core_skills", []):
                st.markdown(f"- {cs}")
        with jr_c2:
            st.markdown("###### ⚙️ TECHNICAL SKILLS")
            for ts in role_info.get("technical_skills", []):
                st.markdown(f"- {ts}")
        with jr_c3:
            st.markdown("###### 🤝 SOFT SKILLS")
            for ss in role_info.get("soft_skills", []):
                st.markdown(f"- {ss}")

        st.markdown("<br>", unsafe_allow_html=True)
        col_next1, col_next2 = st.columns([1, 1])
        with col_next1:
            if st.button("📊 Inspect Detailed Skill Gap Analysis ➔", type="primary", use_container_width=True):
                switch_to("📊 Skill Gap Analysis")
        with col_next2:
            if st.button("💡 Jump Directly to Personalized Recommendations ➔", use_container_width=True):
                switch_to("💡 Recommendations")


# ==============================================================================
# 4. SKILL GAP ANALYSIS PAGE (DEMONSTRATED / DEVELOPING / MISSING)
# ==============================================================================
elif st.session_state["page"] == "📊 Skill Gap Analysis":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📊 Qualitative & Empirical Skill Gap Analysis")

    if st.session_state["analysis_results"] is None:
        st.warning("Please complete your profile and run the analysis first.")
        if st.button("Go to My Skills & Experience", type="primary"):
            switch_to("📝 My Skills & Experience")
    else:
        gap = st.session_state["analysis_results"]["gap_result"]
        target = gap["target_career"]
        match_score = gap["match_percentage"]
        matched = gap["matched_skills"]
        weak = gap["weak_skills"]
        missing = gap["missing_skills"]
        focus_areas = st.session_state["analysis_results"]["focus_areas"]

        # KPI Metrics
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Target Role", target)
        c2.metric("Weighted Skill Match", f"{match_score}%")
        c3.metric("Already Demonstrated", len(matched))
        c4.metric("Competency Gaps", len(weak) + len(missing))

        st.progress(match_score / 100.0)

        # Focus Area Section
        st.markdown("---")
        st.subheader("🎯 Your Immediate Focus Areas")
        st.caption("Based on your target role and current evidence, prioritize these high-impact areas:")

        for f_idx, fa in enumerate(focus_areas, 1):
            with st.container():
                st.markdown(f"""
                <div class="info-card">
                    <b>{f_idx}. {fa['area'].replace('_', ' ')}</b> 
                    <span class="status-badge {'status-red' if fa['urgency']=='High Priority' else 'status-amber'}">{fa['urgency']}</span><br>
                    <span style="color:#475569; font-size:0.95rem;">{fa['why']}</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("📋 In-Depth Skill Classification & Gap Explanations")

        tab_m, tab_w, tab_ms = st.tabs([
            f"🟢 Already Demonstrated ({len(matched)})",
            f"🟡 Needs Improvement ({len(weak)})",
            f"🔴 Not Yet Demonstrated ({len(missing)})"
        ])

        with tab_m:
            if matched:
                st.markdown("You have demonstrated verifiable evidence or experience meeting industry requirements:")
                for s in matched:
                    with st.expander(f"🟢 {s['skill'].replace('_', ' ')} — [Meets Benchmark: {s['required_level']}]", expanded=False):
                        st.markdown(f"**Why this skill matters:** {s['why_required']}")
                        st.markdown("**Your Evidence:**")
                        for ev in s["evidence"]:
                            st.markdown(f"- ✓ {ev}")
            else:
                st.info("No skills meet the complete benchmark level yet.")

        with tab_w:
            if weak:
                st.markdown("You have foundational knowledge, but need to build deeper portfolio or project evidence:")
                for s in weak:
                    with st.expander(f"🟡 {s['skill'].replace('_', ' ')} — [Deficit: -{s['gap']} pts to Benchmark {s['required_level']}]", expanded=True):
                        st.markdown(f"**🎯 Why it is required:** {s['why_required']}")
                        st.markdown("**📋 What to learn:**")
                        for step in s["what_to_learn"]:
                            st.markdown(f"- {step}")
                        st.markdown("**🚀 How to improve:**")
                        for step in s["how_to_improve"]:
                            st.markdown(f"- {step}")
                        st.markdown(f"**🛠️ Suggested Project:** `{s['suggested_project']}`")
            else:
                st.info("No skills in the 'Needs Improvement' bracket.")

        with tab_ms:
            if missing:
                st.markdown("No project or certification evidence was detected for these essential competencies:")
                for s in missing:
                    with st.expander(f"🔴 {s['skill'].replace('_', ' ')} — [Missing Requirement: {s['required_level']}]", expanded=True):
                        st.markdown(f"**🎯 Why it is required:** {s['why_required']}")
                        st.markdown("**📋 What to learn first:**")
                        for step in s["what_to_learn"]:
                            st.markdown(f"- {step}")
                        st.markdown("**🚀 Action steps:**")
                        for step in s["how_to_improve"]:
                            st.markdown(f"- {step}")
                        st.markdown(f"**🛠️ Suggested Starter Project:** `{s['suggested_project']}`")
            else:
                st.success("Great job! You have established evidence across all required competencies.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💡 View Personalized Action Recommendations ➔", type="primary", use_container_width=True):
            switch_to("💡 Recommendations")


# ==============================================================================
# 5. RECOMMENDATIONS & LEARNING ROADMAP PAGE
# ==============================================================================
elif st.session_state["page"] == "💡 Recommendations":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("💡 Personalized Learning Recommendations")

    if st.session_state["analysis_results"] is None:
        st.warning("Please complete your profile and run the analysis first.")
        if st.button("Go to My Skills & Experience", type="primary"):
            switch_to("📝 My Skills & Experience")
    else:
        recs = st.session_state["analysis_results"]["categorized_recs"]
        roadmap = st.session_state["analysis_results"]["roadmap"]
        target = st.session_state["analysis_results"]["gap_result"]["target_career"]

        st.markdown(f"Target Role: **{target}** &nbsp;|&nbsp; Curated learning path to achieve **100% job readiness**.")

        # 5 Categorized Recommendation Sections
        tab_learn, tab_practice, tab_build, tab_certify, tab_interview = st.tabs([
            "📚 Learn",
            "🛠 Practice",
            "💻 Build",
            "📜 Certify",
            "🎤 Interview Preparation"
        ])

        with tab_learn:
            st.subheader("📚 Conceptual Learning Areas")
            st.caption("Deep-dive topics to bridge your theoretical knowledge gaps:")
            for item in recs.get("learn", []):
                st.markdown(f"""
                <div class="info-card">
                    <b>📘 {item['title']}</b><br>
                    <ul style="margin: 6px 0;">
                        {"".join([f"<li>{d}</li>" for d in item.get('details', [])])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        with tab_practice:
            st.subheader("🛠 Practice Exercises & Platforms")
            st.caption("Recommended coding problems and query sandboxes:")
            for item in recs.get("practice", []):
                st.markdown(f"""
                <div class="info-card">
                    <b>🎯 {item['skill'].replace('_', ' ')} Practice</b><br>
                    <b>Platform / Track:</b> <code>{item['platform']}</code><br>
                    <span style="color:#475569;">Focus: {item['focus']}</span>
                </div>
                """, unsafe_allow_html=True)

        with tab_build:
            st.subheader("💻 Capstone Portfolio Projects")
            st.caption("Build and deploy these projects to showcase concrete proof of capability:")
            for item in recs.get("build", []):
                st.markdown(f"""
                <div class="info-card">
                    <b>🛠️ {item['title']}</b><br>
                    <span style="color:#475569;">{item['scope']}</span><br>
                    <small><b>Recommended Tools:</b> <code>{item['tools']}</code></small>
                </div>
                """, unsafe_allow_html=True)

        with tab_certify:
            st.subheader("📜 Industry Certifications")
            st.caption("Accredited certifications that validate your capabilities to recruiters:")
            for item in recs.get("certify", []):
                st.markdown(f"""
                <div class="info-card">
                    <b>🏆 {item['certificate_name']}</b><br>
                    <b>Skill Domain:</b> {item['skill'].replace('_', ' ')} &nbsp;|&nbsp; 
                    <b>Provider:</b> {item['provider']}
                </div>
                """, unsafe_allow_html=True)

        with tab_interview:
            st.subheader("🎤 Interview Preparation Questions")
            st.caption("Common technical and conceptual questions asked for this role:")
            for item in recs.get("interview", []):
                st.markdown(f"""
                <div class="info-card">
                    <b>💬 Topic:</b> {item['topic']}<br>
                    <small style="color:#2563eb;"><b>Assessment Type:</b> {item['category']}</small>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        # Dynamic 5-Phase Learning Roadmap
        st.subheader("🗺️ Dynamic 5-Phase Learning Roadmap")
        st.caption(f"Structured timeline to guide your journey to becoming a job-ready {target}:")

        for phase in roadmap:
            st.markdown(f"""
            <div class="info-card" style="border-left: 4px solid #2563eb;">
                <div style="display:flex; justify-content:space-between;">
                    <b>{phase['phase']}: {phase['title']}</b>
                    <span style="color:#2563eb; font-weight:700;">{phase['duration']}</span>
                </div>
                <p style="margin: 6px 0; color:#334155;"><b>Focus Areas:</b> {phase['skills']}</p>
                <small style="color:#64748b;">🎯 <i>Goal: {phase['goal']}</i></small>
            </div>
            """, unsafe_allow_html=True)


# ==============================================================================
# 6. MODEL INSIGHTS PAGE
# ==============================================================================
elif st.session_state["page"] == "🔬 Model Insights":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("🔬 Machine Learning Model Insights & Architecture")
    st.markdown("Detailed verification of model comparison, cross-validation, confusion matrix, and feature importances.")

    metrics_path = os.path.join(ROOT_DIR, "results", "metrics", "model_comparison.csv")
    if os.path.exists(metrics_path):
        st.subheader("📊 Empirical Model Comparison (Evaluated on Unseen Test Data)")
        comp_df = pd.read_csv(metrics_path)
        st.dataframe(comp_df, use_container_width=True)

    st.markdown("---")
    col_cm, col_fi = st.columns(2)
    with col_cm:
        st.subheader("🎯 Test Set Confusion Matrix")
        cm_path = os.path.join(ROOT_DIR, "results", "plots", "best_model_confusion_matrix.png")
        if os.path.exists(cm_path):
            st.image(cm_path, caption="Confusion Matrix on Unseen Test Set (300 samples)")
    with col_fi:
        st.subheader("⚖️ Skill Feature Importance")
        fi_path = os.path.join(ROOT_DIR, "results", "plots", "feature_importance.png")
        if os.path.exists(fi_path):
            st.image(fi_path, caption="Relative Feature Importance (Random Forest Ensemble)")

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
# 7. ABOUT PROJECT PAGE
# ==============================================================================
elif st.session_state["page"] == "📘 About Project":
    col_back, _ = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Back to Navigation Hub"):
            switch_to("🧭 Navigation Hub")

    st.title("📘 About Skill Gap Analyzer")
    st.markdown("Comprehensive overview of project methodology, O*NET dataset provenance, mathematical formulation, and architecture.")

    st.markdown("### 🏛️ System Architecture")
    st.markdown("""
    ```text
    Qualitative Profile (Experience, Projects, Certs)
                           │
                           ▼
          Backend Feature Engineering Layer
        (Converts qualitative evidence to ML features)
                           │
                           ▼
          Trained Machine Learning Pipeline (98.33% Acc)
                           │
                           ▼
       Target Job Benchmarking (O*NET 28.0 Database)
                           │
                           ▼
       Weighted Skill Gap Analysis & 5-Phase Roadmap
    ```
    """)

    st.markdown("### 🎯 O*NET Standard Occupational Classification (SOC) Mappings")
    st.markdown("""
    | Role | O*NET-SOC Code | Official O*NET Title | Role Focus |
    | :--- | :--- | :--- | :--- |
    | **Software Developer** | `15-1252.00` | Software Developers | Algorithms, Systems, Architecture |
    | **Web Developer** | `15-1254.00` | Web Developers | HTML/CSS, JavaScript, Frontend APIs |
    | **Data Analyst** | `15-2051.01` | Business Intelligence Analysts | SQL, Statistics, Data Viz |
    | **Data Scientist / ML** | `15-2051.00` | Data Scientists | Python, Machine Learning Modeling |
    | **Java Developer** | `15-1251.00` | Computer Programmers | Core Java, Spring/Hibernate, OOP |
    """)

    st.markdown("### 📐 Mathematical Formulation for Skill Gap Score")
    st.latex(r"\text{Fulfillment}_i = \min\left(1.0, \frac{S_i}{R_i}\right)")
    st.latex(r"\text{Skill Match \%} = \left( \frac{\sum_{i=1}^{n} \text{Fulfillment}_i \times R_i}{\sum_{i=1}^{n} R_i} \right) \times 100")
    st.markdown(r"""
    * $S_i$: Student's inferred proficiency level for skill $i \in [0.0, 5.0]$.
    * $R_i$: O*NET benchmark requirement for skill $i \in [0.0, 5.0]$.
    * **Capping at 1.0**: Ensures that over-qualification in one skill cannot falsely mask deficiency in an unrelated required skill.
    """)
