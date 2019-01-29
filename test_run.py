import time
import HTMLTestRunner
import unittest
from test_case import me_case, tokencat_case

data = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))      # 获取当前时间
report = ".\\report\\" + str(data) + ".html"                         # 生成文件名以及存放路径
report_open = open(report, "wb")        # 测试报告文件名，以当前时间命名

suite = unittest.TestSuite()
loader = unittest.TestLoader()

case_1 = unittest.TestLoader().loadTestsFromModule(me_case)        # 加载测试实例
case_2 = unittest.TestLoader().loadTestsFromModule(tokencat_case)

suite.addTest(case_1)
suite.addTest(case_2)

""" 所有测试用例执行完成后，将会自动生成测试报告"""
runner = HTMLTestRunner.HTMLTestRunner(
    verbosity=1, stream=report_open, title='TokenCat通证猫')
runner.run(suite)
