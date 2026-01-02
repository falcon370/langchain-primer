import pytest
import nbformat
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
##----------CONFIG TESTS -------that run every time testing is done
def load_notebook_code(notebook_path):
    """
    Reads a Jupyter Notebook, cleans it, executes it, and returns the variables/functions.
    """
    if not os.path.exists(notebook_path):
        return None

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Container for the student's executed code
    student_context = {}
    for cell in nb.cells:
        if cell.cell_type == 'code':
            clean_lines = [line for line in cell.source.split('\n') 
                           if not line.strip().startswith(('!', '%'))]
            clean_code = '\n'.join(clean_lines)
            try:
                exec(clean_code, student_context)
            except Exception as e:
                # ADD THIS PRINT TO SEE THE REAL ERROR
                print(f"\n❌ Error executing cell in {notebook_path}: {e}")
    return student_context
    
    



@pytest.fixture
def student_code(request):
    """
    Improved fixture: Detects level (easy/medium/hard) from the test function name
    to find the correct notebook file.
    """
    # 1. Identify which level we are testing
    node_name = request.node.name.lower() # e.g., "test_easy_task"
    
    if "easy" in node_name:
        notebook_name = "easy_01.ipynb"
    elif "medium" in node_name:
        notebook_name = "medium_01.ipynb"
    elif "hard" in node_name:
        notebook_name = "hard_01.ipynb"
    else:
        # Fallback to a default if the name doesn't match
        notebook_name = "module_01.ipynb"
    
    # 2. Path handling
    root_dir = Path(__file__).parent.parent
    submission_path = root_dir / "submissions" / notebook_name
    
    # Debug print (will show up if you run pytest -s)
    # print(f"\n🔍 Searching for: {submission_path}")
    
    return load_notebook_code(str(submission_path))