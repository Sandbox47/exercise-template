import os
import json

# Load config
with open("Config.json", "r") as f:
    config = json.load(f)

prefix = config.get("prefix", "Prefix")
suffix = config.get("suffix", "Suffix")
sheet = config.get("sheet", "Sheet")

# Find next Sheet<Nr> folder
existing_folders = [d for d in os.listdir() if os.path.isdir(d) and d.startswith("Sheet")]
sheet_numbers = [int(d[5:]) for d in existing_folders if d[5:].isdigit()]
next_nr = max(sheet_numbers, default=-1) + 1

sheet_folder = f"{sheet}{next_nr}"
os.makedirs(sheet_folder, exist_ok=True)

# Create .tex file
filename = f"{prefix}_{sheet}{next_nr}_{suffix}.tex"
filepath = os.path.join(sheet_folder, filename)

latex_template = f"""\\documentclass[12pt]{{scrartcl}}

\\input{{../LatexTemplate/Packages.tex}} 
\\input{{../LatexTemplate/FormatAndHeader.tex}}

% \\stepcounter{{counter}} increases the number of the counter with one. Use this if you need to skip an exercise.
\\setcounter{{sheetnr}}{{{next_nr}}} 
\\setcounter{{exnum}}{{1}} 

\\begin{{document}}

\\exercise{{Example exercise}}




\\end{{document}}
"""

with open(filepath, "w") as f:
    f.write(latex_template)

print(f"Created: {filepath}")
