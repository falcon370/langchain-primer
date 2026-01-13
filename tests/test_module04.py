import pytest

class TestModule04:
    
    def test_easy_task(self, student_code):
        # 1: File Presence (Environmental)
        if student_code is None:
            pytest.skip("Submission file 'easy_04.ipynb' not found. Skipping module.")
        
        # 2: Function Presence (Grading)
        memory = student_code.get("buffer_memory")
        if not memory:
            pytest.fail("Logic Error: ConversationBufferMemory 'buffer_memory' is missing!")
        
        # 3: Logic Execution
        memory.save_context({"input": "Hello"}, {"output": "Hi there!"})
        history = memory.load_memory_variables({})
        assert "history" in history or "buffer" in str(history).lower(), "Memory should store conversation history."

    def test_medium_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'medium_04.ipynb' not found.")
        
        # 2: Function Presence
        chat_chain = student_code.get("chat_chain")
        if not chat_chain:
            pytest.fail("Logic Error: Chat chain 'chat_chain' is missing from the notebook!")
        
        # 3: Logic Execution - verify callable
        assert callable(chat_chain.invoke) or callable(chat_chain), "Chat chain must be invokable."

    def test_hard_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'hard_04.ipynb' not found.")
        
        # 2: Function Presence
        session_manager = student_code.get("session_manager")
        if not session_manager:
            pytest.fail("Logic Error: Session manager 'session_manager' is missing!")
        
        # 3: Logic Execution
        assert hasattr(session_manager, "save_session") or callable(session_manager), "Session manager must have save functionality."
