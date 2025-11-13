from pathlib import Path
import pandas as pd

data_dir = Path("data")
output_dir = Path("output")
output_file = output_dir / "counts.csv"

output_dir.mkdir(exist_ok=True)

counts = []
for path in data_dir.glob("*.csv"):
    df = pd.read_csv(path)
    num_lines = len(df)
    counts.append({"filename": path.name, "num_lines": num_lines})

df = pd.DataFrame(counts)
df.to_csv(output_file, index=False)

print(f"Line counts written to {output_file}")
