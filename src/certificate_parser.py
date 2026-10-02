"""
Certificate Parser and Analysis Engine
Handles saving certificate files (PDF, PNG, JPG, JPEG) to disk,
extracting textual metadata via pypdf and regex entity detection,
and structuring certification evidence.
"""

import os
import re
import datetime
from PIL import Image

try:
    import pypdf
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

UPLOADS_DIR = "uploads"

# Known Issuing Organizations Dictionary
KNOWN_ORGANIZATIONS = [
    "Oracle", "Amazon Web Services", "AWS", "Google Cloud", "Google",
    "Microsoft", "IBM", "Meta", "DeepLearning.AI", "Coursera",
    "Udemy", "edX", "Cisco", "HackerRank", "freeCodeCamp",
    "LinkedIn Learning", "Stanford Online", "HarvardX", "MongoDB",
    "NPTEL", "Infosys Springboard", "TCS iON"
]

# Skill & Domain Mapping Keywords
SKILL_DOMAIN_MAP = {
    "Python": ["python", "pandas", "numpy", "django", "flask"],
    "Java": ["java", "spring", "hibernate", "jvm", "j2ee"],
    "SQL": ["sql", "mysql", "postgresql", "database", "rdbms", "queries"],
    "Machine_Learning": ["machine learning", "deep learning", "neural network", "artificial intelligence", "ai", "nlp", "computer vision"],
    "Statistics": ["statistics", "probability", "statistical analysis", "data analysis"],
    "Data_Visualization": ["tableau", "power bi", "powerbi", "visualization", "dashboard", "matplotlib", "seaborn"],
    "HTML_CSS": ["html", "css", "web design", "frontend", "responsive design"],
    "JavaScript": ["javascript", "js", "react", "node", "typescript", "vue", "angular"],
    "Git": ["git", "github", "version control"],
    "Algorithms_OOP": ["data structures", "algorithms", "dsa", "object oriented", "oop", "problem solving"]
}

def ensure_uploads_dir():
    os.makedirs(UPLOADS_DIR, exist_ok=True)

def save_uploaded_certificate(uploaded_file) -> str:
    """
    Saves an uploaded Streamlit file to the uploads/ directory.
    Returns the saved absolute path.
    """
    ensure_uploads_dir()
    # Sanitize filename with timestamp prefix to prevent overwrite collisions
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', uploaded_file.name)
    saved_filename = f"{timestamp}_{clean_name}"
    file_path = os.path.join(UPLOADS_DIR, saved_filename)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    return file_path

def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from PDF or extracts filename/metadata clues for images.
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    
    if ext == ".pdf" and PYPDF_AVAILABLE:
        try:
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += " " + extracted
        except Exception:
            pass

    # If text is empty or image file, use filename and image metadata as fallback
    if not text.strip():
        base_name = os.path.basename(file_path)
        # Convert separators to spaces for entity matching
        text = re.sub(r'[_\-.]+', ' ', base_name)
        if ext in [".png", ".jpg", ".jpeg"]:
            try:
                with Image.open(file_path) as img:
                    text += f" Image Format: {img.format} Size: {img.size}"
            except Exception:
                pass
                
    return text

def parse_certificate(file_path: str, original_filename: str) -> dict:
    """
    Analyzes certificate text to identify:
    - Certificate Title
    - Issuing Organization
    - Skill/Domain
    - Certification Type
    - Relevant Technologies
    - Year
    - Verification Status
    """
    extracted_text = extract_text_from_file(file_path)
    text_lower = extracted_text.lower()
    
    # 1. Detect Organization
    detected_org = "Independent / Online Provider"
    for org in KNOWN_ORGANIZATIONS:
        if re.search(r'\b' + re.escape(org.lower()) + r'\b', text_lower):
            detected_org = org
            break

    # 2. Detect Skills & Technologies
    detected_skills = []
    for skill_name, keywords in SKILL_DOMAIN_MAP.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
                detected_skills.append(skill_name)
                break

    # 3. Detect Domain
    detected_domain = "Computer Science & Engineering"
    if "Machine_Learning" in detected_skills or "ai" in text_lower:
        detected_domain = "Artificial Intelligence & Data Science"
    elif "Data_Visualization" in detected_skills or "SQL" in detected_skills:
        detected_domain = "Data Analytics & Business Intelligence"
    elif "HTML_CSS" in detected_skills or "JavaScript" in detected_skills:
        detected_domain = "Web & Full Stack Development"
    elif "Java" in detected_skills:
        detected_domain = "Enterprise Backend & Java Systems"
    elif "Python" in detected_skills:
        detected_domain = "Software Development & Python"

    # 4. Detect Year
    current_year = datetime.datetime.now().year
    year_match = re.search(r'\b(20[1-2][0-9])\b', extracted_text)
    detected_year = int(year_match.group(1)) if year_match else current_year

    # 5. Detect Title
    clean_base = re.sub(r'[_\-]+', ' ', os.path.splitext(original_filename)[0]).strip().title()
    title_candidates = [
        "Specialization Certificate",
        "Foundations Associate",
        "Professional Certificate",
        "Course Completion",
        "Certified Developer"
    ]
    detected_title = clean_base
    for cand in title_candidates:
        if cand.lower() in text_lower:
            detected_title = f"{detected_org} {cand}"
            break

    # 6. Certification Type
    cert_type = "Course Certificate"
    if "specialization" in text_lower:
        cert_type = "Specialization"
    elif "professional certificate" in text_lower:
        cert_type = "Professional Certificate"
    elif "assessment" in text_lower or "hackerrank" in text_lower:
        cert_type = "Technical Assessment"

    return {
        "file_name": original_filename,
        "saved_path": file_path,
        "title": detected_title,
        "organization": detected_org,
        "domain": detected_domain,
        "type": cert_type,
        "detected_skills": detected_skills if detected_skills else ["Computer Science"],
        "year": detected_year,
        "status": "Detected (User-confirmed)",
        "upload_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
