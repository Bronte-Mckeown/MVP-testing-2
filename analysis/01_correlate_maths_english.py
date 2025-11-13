from pathlib import Path

import subprocess
import sys

# ---- Ensure pandas is installed ----
try:
    import pandas as pd
except ImportError:
    print("pandas not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

data_dir = Path("data")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# ---- Load results.csv ----
path = data_dir / "results.csv"
df = pd.read_csv(path)

# ---- Filter to KS4 Current Grades ----
df = df[df["assessment_type"] == "*Current Grades"]

# ---- Keep Maths + English Lit subjects ----
subjects_of_interest = ["Mathematics", "English Literature"]
df = df[df["subject"].isin(subjects_of_interest)]

# ---- Pivot to wide format ----
wide = df.pivot_table(
    index="student_id",     
    columns="subject",
    values="score",          
    aggfunc="first"
).reset_index()

# ---- Compute correlations ----
corr = wide[subjects_of_interest].corr()

# ---- Save correlation matrix ----
output_file = output_dir / "correlations.csv"
corr.to_csv(output_file)

print("Correlation matrix:")
print(corr)
print(f"\nSaved to {output_file}")