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
## To a hiring manager, every commit would serve a distinct goal: exclusions, the functions script, and project documentation. The commit messages would aid in code and documentation review, as well as help break code and documentation into logical and comprehensible commits.
## 2. The impact of Git on my coding style
Git will aid in practicing making one distinct change per commit, testing the script after each change, and looking at the contents of git diff prior to committing. I would store working snapshots in the repository with descriptive commit messages. These snapshots would aid in rolling back to an older state or comparing different states, rather than using backup files or overwriting files. Completed commits would be pushed and I would verify on GitHub that the version being graded is up to date.
## 3. One more thing I would add to my workflow
In my Windows and VS Code Python environment I would add a local Python virtual environment, .venv/, to be excluded. This is already present in this repository’s .gitignore. A virtual environment stores system-specific files and installed packages. These files and packages can be regenerated so it is not necessary to track a virtual environment. However, a list of required packages (i.e. requirements.txt) could be tracked if additional packages are needed for a future lab. 


