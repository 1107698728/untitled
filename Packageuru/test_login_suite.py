import unittest
import loginpro
import sys


#测试套件
class TestLogin(unittest.TestCase):
    #初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法", sys._getframe().f_code.co_name)
    #清空类方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法", sys._getframe().f_code.co_name)
    def setUp(cls) -> None:
        print("开始运行方法",sys._getframe().f_code.co_name)
    def tearDown(cls) -> None:
        print("开始运行方法", sys._getframe().f_code.co_name)
    def test_login_success(self):
        expect_value=1
        actual_value=loginpro.login("admin","123456").get("code")
        self.assertEqual(expect_value,actual_value)
    def test_user_wrong(self):
        expect_value=0
        actual_value=loginpro.login("bca","123456").get("code")
        self.assertEqual(expect_value,actual_value)
    def test_password_null(self):
        expect_value=0
        actual_value=loginpro.login("admin","").get("code")
        self.assertEqual(expect_value,actual_value)

if __name__=='__main__':
    suit_b=unittest.TestSuite()
    suit_b.addTest(TestLogin('test_login_success'))
    suit_b.addTest(TestLogin('test_user_wrong'))
    print("-"*30)
    print(suit_b)
    runner = unittest.TestRunner()
    runner.run(suit_b)