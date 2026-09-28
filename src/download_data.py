"""
Phase 3: Dataset Downloader for Skill Gap Analyzer
Source: O*NET 28.0 Database (U.S. Department of Labor)
URL: https://www.onetcenter.org/
"""

import os
import urllib.request
import zipfile
import io
import pandas as pd

ONET_ZIP_URL = "https://www.onetcenter.org/dl_files/database/db_28_0_text.zip"
TARGET_DIR = os.path.join("dataset", "raw")

# Specific files we need from the archive
FILES_TO_EXTRACT = [
    "Occupation Data.txt",
    "Skills.txt",
    "Knowledge.txt",
    "Technology Skills.txt"
]

def download_and_extract_onet():
    print("=" * 60)
    print("Phase 3: Downloading Official O*NET Dataset")
    print("=" * 60)
    
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    print(f"Connecting to: {ONET_ZIP_URL}")
    req = urllib.request.Request(ONET_ZIP_URL, headers={"User-Agent": "Mozilla/5.0"})
    
    with urllib.request.urlopen(req) as response:
        print("Downloading archive (~11.5 MB)... Please wait.")
        zip_bytes = response.read()
        print(f"Download complete: {len(zip_bytes) / (1024 * 1024):.2f} MB received.")
        
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        archive_file_list = zf.namelist()
        print("\nExtracting required files into dataset/raw/ ...")
        
        for file_name in FILES_TO_EXTRACT:
            # Match exact file basename so 'Skills.txt' does not match 'Technology Skills.txt'
            matched = [f for f in archive_file_list if os.path.basename(f) == file_name]
            if matched:
                source_path = matched[0]
                target_path = os.path.join(TARGET_DIR, file_name)
                with zf.open(source_path) as source_file, open(target_path, "wb") as target_file:
                    target_file.write(source_file.read())
                print(f"  [SAVED] {file_name} -> {target_path}")
            else:
                print(f"  [WARNING] Could not locate {file_name} in archive.")

    print("\n" + "=" * 60)
    print("Dataset Inspection Summary:")
    print("=" * 60)
    
    # 1. Occupation Data
    occ_path = os.path.join(TARGET_DIR, "Occupation Data.txt")
    if os.path.exists(occ_path):
        occ_df = pd.read_csv(occ_path, sep="\t")
        print(f"1. Occupation Data.txt:")
        print(f"   - Rows: {len(occ_df):,}")
        print(f"   - Occupations count: {occ_df['O*NET-SOC Code'].nunique():,}")
        print(f"   - Key columns: {list(occ_df.columns)}")
        
    # 2. Skills Data
    skills_path = os.path.join(TARGET_DIR, "Skills.txt")
    if os.path.exists(skills_path):
        skills_df = pd.read_csv(skills_path, sep="\t")
        print(f"\n2. Skills.txt:")
        print(f"   - Rows: {len(skills_df):,}")
        print(f"   - Unique Skill Elements: {skills_df['Element Name'].nunique():,}")
        print(f"   - Key columns: {list(skills_df.columns)}")
        
    # 3. Knowledge Data
    know_path = os.path.join(TARGET_DIR, "Knowledge.txt")
    if os.path.exists(know_path):
        know_df = pd.read_csv(know_path, sep="\t")
        print(f"\n3. Knowledge.txt:")
        print(f"   - Rows: {len(know_df):,}")
        print(f"   - Unique Knowledge Elements: {know_df['Element Name'].nunique():,}")
        print(f"   - Key columns: {list(know_df.columns)}")
        
    # 4. Technology Skills Data
    tech_path = os.path.join(TARGET_DIR, "Technology Skills.txt")
    if os.path.exists(tech_path):
        tech_df = pd.read_csv(tech_path, sep="\t")
        print(f"\n4. Technology Skills.txt:")
        print(f"   - Rows: {len(tech_df):,}")
        print(f"   - Unique Technologies: {tech_df['Example'].nunique():,}")
        print(f"   - Key columns: {list(tech_df.columns)}")

    print("\nDataset successfully acquired in dataset/raw/!")

if __name__ == "__main__":
    download_and_extract_onet()
