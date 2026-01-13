import pytest

class TestModule05:
    
    def test_easy_task(self, student_code):
        # 1: File Presence (Environmental)
        if student_code is None:
            pytest.skip("Submission file 'easy_05.ipynb' not found. Skipping module.")
        
        # 2: Function Presence (Grading)
        loader = student_code.get("loader")
        if not loader:
            pytest.fail("Logic Error: Document loader 'loader' is missing from the notebook!")
        
        # 3: Logic Execution - verify it has load method
        assert hasattr(loader, "load") or callable(loader), "Loader must have load method or be callable."

    def test_medium_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'medium_05.ipynb' not found.")
        
        # 2: Function Presence
        retriever = student_code.get("retriever")
        if not retriever:
            pytest.fail("Logic Error: Retriever 'retriever' is missing from the notebook!")
        
        # 3: Logic Execution
        assert hasattr(retriever, "get_relevant_documents") or hasattr(retriever, "invoke"), "Retriever must have retrieval method."

    def test_hard_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'hard_05.ipynb' not found.")
        
        # 2: Function Presence
        rag_chain = student_code.get("rag_chain")
        if not rag_chain:
            pytest.fail("Logic Error: RAG chain 'rag_chain' is missing from the notebook!")
        
        # 3: Logic Execution
        result = rag_chain.invoke({"query": "test query"})
        assert isinstance(result, (str, dict)), "RAG chain must return string or dict with sources/answer."
        
        # Verify answer field exists (common RAG output pattern)
        if isinstance(result, dict):
            assert "answer" in result or "output" in result or "result" in result, "RAG result should contain answer/output field."
