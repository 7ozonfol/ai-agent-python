from functions.get_file_content import get_file_content
import unittest

class TestGetFilesContent(unittest.TestCase):
    def setUp(self):
        self.get_file_content = get_file_content

    def test_current(self):
        result = self.get_file_content("calculator", "lorem.txt")
        print(f"""Result for lorem file:
        {result}""")
    
    def test_main_in_calc(self):
        result = self.get_file_content("calculator", "main.py")
        print(f"""Result for 'calculator/main.py' file:
        {result}""")

    def test_pkg(self):
        result = self.get_file_content("calculator", "pkg/calculator.py")
        print(f"""Result for 'pkg/calculator.py' file:
        {result}""")

    def test_bin(self):
        result = self.get_file_content("calculator", "/bin/cat")
        print(f"""Result for '/bin/cat' file:
        {result}""")

    def test_nofile(self):
        result = self.get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"""Result for 'pkg/does_not_exist.py' file:
        {result}""")

if __name__ == '__main__':
    unittest.main()