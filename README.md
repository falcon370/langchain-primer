# langchain-primer

## Overview 🚀

This repo is built to be a **hands-on** learning repo to help you understand LangChain, LLM providers, vector stores, and basic RAG/back-end patterns through Jupyter notebooks and small scripts.
The project is structured around modules in `notebooks/` and supporting utilities in `scripts/`, with tests in `tests/` to verify your solutions. 

## Project structure 📂

- `notebooks/`: Guided notebooks for LangChain fundamentals, chains, tools, RAG, and simple apps.   
- `scripts/`: Helper scripts for running or checking notebook code from the CLI.   
- `tests/`: Pytest-based checks for your solutions, useful for self-evaluation and CI.   
- `resources/`: Reference material to guide you throught the course.   
- `submissions/`: Place your own implementations or checkpoint notebooks here if you are following as a course.  
- `docs/`: Product-style docs such as `product_overview.md` and `pricing_faq.md` used as realistic content for RAG experiments.
- `.env.example`: Template for API keys and environment configuration.   
- `requirements.txt`: Dependency list for notebooks, API backends, and tooling.

## Tech stack 🧠

- **LangChain** ecosystem: `langchain`, `langchain-openai`, `langchain-anthropic`, `langchain-community` for building LLM chains and tools.
- LLM providers: `openai>=1.0.0`, `anthropic` for hosted models.
- Vector and document stack: `faiss-cpu`, `chromadb`, `pypdf`, `python-docx` to build simple RAG pipelines.
- Web backend: `fastapi`, `uvicorn[standard]`, `pydantic>=2.0.0`, `requests` for minimal LangChain-powered APIs.
- Dev experience: Jupyter stack (`jupyter`, `jupyterlab`, `notebook`, `ipython`, `ipykernel`, `ipywidgets`) plus testing and linting (`pytest`, `pytest-asyncio`, `pytest-cov`, `black`, `flake8`, `mypy`, `pylint`).

## Setup instructions ⚙️

### 1. Clone the repository

```bash
git clone https://github.com/bdaccell-nitw/langchain-primer.git
cd langchain-primer
```


### 2. Create and activate a virtual environment

macOS
```bash
python3 -m venv .venv
source .venv/bin/activate   
```
Windows (PowerShell)
```bash 
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Windows (CMD)
```bash 
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```


### 4. Configure environment variables 🔐

- Copy the example env file:   
    macOS (terminal) :
  ```bash
  cp .env.example .env 
  ```  
   Windows (Powershell):
  ```bash
  copy .env.example .env 
  ```  
- Edit `.env` and set keys such as `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, and any other required credentials used inside the notebooks or FastAPI examples.

### 5. Run Jupyter notebooks 📓

From the project root:

```bash
jupyter lab     # or: jupyter notebook
```

Then open the notebooks under `notebooks/` and follow the instructions in each module. 

### 6. Run tests ✅

- To run a single test 
```bash
 pytest tests/test_filename.py
```
- To run all tests under tests/.
```bash
pytest 
```
#### Note : Run pytest commands in your root directory

## How to use?

- Start with the earliest module in `notebooks/`.
- Create a new .ipynb file following the format <level>_0<number>.ipynb
 `Eg: easy_01.ipynb`
- Copy the template code in modules and paste it in your newly created file under submissions folder
- Implement the TODOs
- Run `pytest` to check correctness. 

- If all tests pass ,Open a Pull Request on your with the below format <br>

 ` fix(module_<module_no.>): <difficultylevel>` 
 <br>
 Eg: fix(module_3): easy
- Note : Follow this [guide](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13$0) for commit message conventions

