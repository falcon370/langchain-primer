import pytest

class TestModule03:
    
    def test_easy_task(self, student_code):
        # 1: File Presence (Environmental)
        if student_code is None:
            pytest.skip("Submission file 'easy_03.ipynb' not found. Skipping module.")
        
        # 2: Function Presence (Grading)
        create_tool = student_code.get("create_tool")
        if not create_tool:
            pytest.fail("Logic Error: Function 'create_tool' (or @tool decorated function) is missing!")
        
        # 3: Logic Execution
        result = create_tool("sample input")
        assert isinstance(result, str), "Tool must return a string response."

    def test_medium_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'medium_03.ipynb' not found.")
        
        # 2: Function Presence
        agent = student_code.get("agent")
        tools = student_code.get("tools")
        if not agent:
            pytest.fail("Logic Error: Agent 'agent' is missing from the notebook!")
        if not tools:
            pytest.fail("Logic Error: Tools list 'tools' is missing from the notebook!")
        
        # 3: Logic Execution
        assert isinstance(tools, (list, tuple)), "Tools should be a list or tuple."
        assert len(tools) > 0, "Agent should have at least one tool."

    def test_hard_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'hard_03.ipynb' not found.")
        
        # 2: Function Presence
        agent_with_logging = student_code.get("agent_with_logging")
        if not agent_with_logging:
            pytest.fail("Logic Error: Agent with logging 'agent_with_logging' is missing!")
        
        # 3: Logic Execution
        result = agent_with_logging("test query")
        assert isinstance(result, (str, dict)), "Agent result must be string or dict."
