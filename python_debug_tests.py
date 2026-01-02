import os
from pathlib import Path

# Simulate where conftest.py thinks the root is
# (Assuming conftest is in tests/conftest.py)
root_dir = Path.cwd()
submissions_dir = root_dir / "submissions"
target_file = submissions_dir / "easy_01.ipynb"

print(f"--- DEBUGGING PATHS ---")
print(f"Current Working Dir: {root_dir}")
print(f"Looking for folder:  {submissions_dir}")
print(f"Looking for file:    {target_file}")
print(f"---------------------")

if not submissions_dir.exists():
    print("❌ ERROR: 'submissions' folder does not exist!")
    print(f"   Contents of root: {os.listdir(root_dir)}")
elif not target_file.exists():
    print(f"❌ ERROR: File '{target_file.name}' not found!")
    print(f"   Files found in submissions/: {os.listdir(submissions_dir)}")
else:
    print("✅ SUCCESS: File found! Run pytest now.")