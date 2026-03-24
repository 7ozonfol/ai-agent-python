from functions.run_python_file import run_python_file
import unittest

class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        self.run_python_file = run_python_file

    def test_calc_main(self):
        result = self.run_python_file("calculator","main.py")
        print(result)
    
    def test_calc_add(self):
        result = self.run_python_file("calculator", "main.py",["3 + 5"])
        print(result)
    
    def test_calc_test(self):
        result = self.run_python_file("calculator", "tests.py")
        print(result)

    def test_root_main(self):
        result = self.run_python_file("calculator","../main.py")
        print(result)

    def test_non_exist(self):
        result = self.run_python_file("calculator", "nonexistent.py")
        print(result)

    def test_not_python(self):
        result=self.run_python_file("calculator", "lorem.txt")
        print(result)


if __name__ =='__main__':
    unittest.main()