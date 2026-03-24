from functions.write_file import write_file
import unittest

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.write_file = write_file

    def test_current(self):
        result = self.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(f"""Result for lorem.txt file:
        {result}""")

    def test_pkg(self):
        result = self.write_file("calculator", "pkg/morelorem.txt","lorem ipsum dolor sit amet")
        print(f"""Result for 'pkg/morelorem.txt' file:
        {result}""")

    def test_tmp(self):
        result = self.write_file("calculator", "/tmp/temp.txt","this should not be allowed")
        print(f"""Result for '/tmp' directory:
        {result}""")

if __name__ == '__main__':
    unittest.main()