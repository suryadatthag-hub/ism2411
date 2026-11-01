# ISM2411 — Python for Business

**Name:** Surya Gottimukkala

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411 at the University of South Florida. Module folders organize the Python scripts, and Git tracks changes to the code and documentation.

## Modules

- `week07/` — Functions and debugging: `calculate_tax`, `apply_discount`, and `final_price`, with sample calculations and loop exercises.
- Module 8 — Git and GitHub: repository setup, `.gitignore`, documentation, and reflection in this README.

## How to Run

Install Python 3, open a terminal in the repository folder, and run:

```bash
python week07/functions.py
```

The script uses only Python built-in features and prints tax, discount, final-price, sales-total, and variable-scope examples. No extra packages are required.

## Reflection

### 1. Commit history and work habits

Output of `git log --oneline`, captured before adding this reflection:

```text
2599992 add README with module listing and run instructions
a1c9078 add module 7 functions: calculate_tax, apply_discount, final_price
f29d00d add .gitignore for Python and OS files
d12bbf3 Initial commit
```

A hiring manager could see that each commit has a specific purpose: setting up exclusions, adding the functions script, and documenting the project. The descriptive messages make the work easier to review and show that code and documentation are organized into separate, understandable changes.

### 2. How Git should change my editing approach

Using Git should encourage me to make one focused change at a time, run the script to check the result, and inspect `git diff` before committing. Instead of relying on overwritten files or separate backup copies, I should save working milestones with clear commit messages so I can compare versions or recover an earlier one. I should also push finished commits and check GitHub to confirm that the version being graded is up to date.

### 3. An additional exclusion for my workflow

For my Windows and VS Code Python workflow, I would add `.venv/` to exclude a local Python virtual environment; this pattern is included in this repository's `.gitignore`. A virtual environment contains installed packages and machine-specific files that can be recreated, so tracking it would add unnecessary files and could cause problems on another computer. If a future lab needs extra packages, I would track a dependency list such as `requirements.txt` instead.
