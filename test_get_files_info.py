from functions.get_files_info import get_files_info
import unittest

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_current(self):
        result = self.get_files_info("calculator", ".")
        print(f"""Result for current directory:
        {result}""")

    def test_pkg(self):
        result = self.get_files_info("calculator", "pkg")
        print(f"""Result for 'pkg' directory:
        {result}""")

    def test_bin(self):
        result = self.get_files_info("calculator", "/bin")
        print(f"""Result for '/bin' directory:
        {result}""")

    def test_root(self):
        result = self.get_files_info("calculator", "../")
        print(f"""Result for '../' directory:
        {result}""")

if __name__ == '__main__':
    unittest.main()