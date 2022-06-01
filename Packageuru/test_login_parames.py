from parameterized import parameterized
from loginpro import login
import unittest

#数据参数化
lis=[(1,"admin","123456"),(0,"cba","123456")]
class Testlogin(unittest.TestCase):
    #装饰器提供参数列表
    @parameterized.expand(lis)
    def test_login(self,expect_value,name,password):
        actual_value=login(name,password).get("code")
        self.assertEqual(expect_value,actual_value)

if __name__=='__main__':
    unittest.main()