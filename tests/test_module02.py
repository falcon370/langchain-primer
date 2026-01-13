import pytest

class TestModule02:
    
    def test_easy_task(self, student_code):
        # 1: File Presence (Environmental)
        if student_code is None:
            pytest.skip("Submission file 'easy_02.ipynb' not found. Skipping module.")
        
        # 2: Function Presence (Grading)
        prompt_template = student_code.get("prompt_template")
        if not prompt_template:
            pytest.fail("Logic Error: PromptTemplate 'prompt_template' is missing from the notebook!")
        
        # 3: Logic Execution
        result = prompt_template.format(topic="Machine Learning", audience="Student")
        assert isinstance(result, str), "The PromptTemplate must format to a string."
        assert "Machine Learning" in result, "Topic should be present in formatted prompt."
        assert "Student" in result, "Audience should be present in formatted prompt."

    def test_medium_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'medium_02.ipynb' not found.")
        
        # 2: Function Presence
        chain = student_code.get("llm_chain")
        if not chain:
            pytest.fail("Logic Error: LLMChain 'llm_chain' is missing from the notebook!")
        
        # 3: Logic Execution - verify it's callable
        assert callable(chain.invoke) or callable(chain), "Chain must be invokable."

    def test_hard_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'hard_02.ipynb' not found.")
        
        # 2: Function Presence
        safety_chain = student_code.get("safety_chain")
        if not safety_chain:
            pytest.fail("Logic Error: Safety chain function is missing from the notebook!")
        
        # 3: Logic Execution
        result = safety_chain("test input")
        assert isinstance(result, (str, dict)), "Safety chain must return string or dict response."
