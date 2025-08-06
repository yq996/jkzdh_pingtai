import os
import pytest

if __name__ == "__main__":
    os.makedirs("./report/json_report", exist_ok=True)
    pytest.main(["-vs", "./testcases/test_runner.py", "--alluredir", "./report/json_report", "--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
