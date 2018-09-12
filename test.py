import unittest,os
import HTMLTestRunner

class TestOne(unittest.TestCase):
        def setUp(self):
                print("start!!!")

        def test_add(self):
                print("add")

        def test_sub(self):
                print("sub")

        def tearDown(self):
                print("end")

if __name__ == "__main__":
        test_dir = os.path.join(os.getcwd())
        cases = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
        fp = open("testRes.html","wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="测试描述")
        runner.run(cases)