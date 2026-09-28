"""
Environment verification script for Skill Gap Analyzer
"""
import sys

def verify():
    print(f"Python version: {sys.version.split()[0]}")
    
    libraries = ["numpy", "pandas", "sklearn", "matplotlib", "seaborn", "streamlit", "joblib"]
    all_ok = True
    
    for lib in libraries:
        try:
            mod = __import__(lib)
            ver = getattr(mod, "__version__", "installed")
            print(f"[OK] {lib:<15} : version {ver}")
        except ImportError as e:
            print(f"[FAILED] {lib:<11} : {e}")
            all_ok = False
            
    if all_ok:
        print("\nAll dependencies verified successfully! Environment is ready.")
    else:
        print("\nSome dependencies failed to load.")

if __name__ == "__main__":
    verify()