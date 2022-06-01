import unittest
import loginpro
import sys
from Packageuru.HTMLTestRunner import HTMLTestRunner

#单元测试
class TestLogin(unittest.TestCase):
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
    suit_b = unittest.TestSuite()
    suit_b.addTest(TestLogin('test_login_success'))
    suit_b.addTest(TestLogin('test_user_wrong'))
    test_report='./test_report.html'
    with open(test_report,"wb") as f:
        runner = HTMLTestRunner(f,title="测试报告",description="测试报告描述")
        runner.run(suit_b)