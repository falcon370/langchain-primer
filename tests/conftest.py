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
    and module number from the test file/module name.
    """
    # 1. Identify which level we are testing
    node_name = request.node.name.lower()  # e.g., "test_easy_task"
    
    if "easy" in node_name:
        level = "easy"
    elif "medium" in node_name:
        level = "medium"
    elif "hard" in node_name:
        level = "hard"
    else:
        level = "module"
    
    # 2. Identify which module we're testing from the module/file name
    # The module name is something like "test_module01" or "test_module02"
    module_name = request.module.__name__  # e.g., "tests.test_module01"
    
    # Extract the number from module name
    import re
    module_number = "01"  # default
    
    # Look for patterns like module01, module02 in the module path
    match = re.search(r'module(\d{2})', module_name)
    if match:
        module_number = match.group(1)
    else:
        # Try alternative pattern
        match = re.search(r'_(\d{2})', module_name)
        if match:
            module_number = match.group(1)
    
    # 3. Form the notebook name
    notebook_name = f"{level}_{module_number}.ipynb"
    
    # 4. Path handling
    root_dir = Path(__file__).parent.parent
    submission_path = root_dir / "submissions" / notebook_name
    
    print(f"\n🔍 Looking for notebook: {notebook_name} at {submission_path}")
    
    return load_notebook_code(str(submission_path))

