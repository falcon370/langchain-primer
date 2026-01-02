import pytest

class TestModule01:
    
    def test_easy_task(self, student_code):
        #   1: File Presence (Environmental)
        if student_code is None:
            pytest.skip("Submission file 'easy_01.ipynb' not found. Skipping module.")

        #   2: Function Presence (Grading)
        func = student_code.get("describe_for_audience")
        if not func:
            pytest.fail("Logic Error: Function 'describe_for_audience' is missing from the notebook!")

        #   3: Logic Execution
        result = func("AI", "child")
        assert isinstance(result, str), "The function must return a string."

    def test_medium_task(self, student_code):
        #   1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'medium_01.ipynb' not found.")

        #   2: Function Presence
        func = student_code.get("validate_input")
        if not func:
            pytest.fail("Logic Error: Function 'validate_input' is missing from the notebook!")

        #   3: Logic Execution
        assert func("", "CTO") is False

    def test_hard_task(self, student_code):
        # 1: File Presence
        if student_code is None:
            pytest.skip("Submission file 'hard_01.ipynb' not found.")

        #  2: Function Presence
        func = student_code.get("describe_with_logging")
        if not func:
            pytest.fail("Logic Error: Function 'describe_with_logging' is missing!")

        #  3: Logic Execution
        func("Artificial Intelligence", "Student")

