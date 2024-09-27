"""
运行步骤
1.运行指定的用例
2.运行所有的用例
"""
import unittest
from symbol import suite

from HTMLTestRunner import HTMLTestRunner
from scripts.test_login import TestLogin
from scripts.test_logout import TestLogout

if __name__ == '__main__':
    # 收集指定用例
    # 创建TestSuite类对象
    # suite = unittest.TestSuite()
    # # 调用方法收集用例addTest（类名（“方法名"））
    # suite.addTest(TestLogin("test_login1"))
    # suite.addTest(TestLogout("test_case1"))

    # 收集所有用例
    suite = unittest.defaultTestLoader.discover('./scripts')
    # 生成测试报告
    with open("./report/report.html","wb") as f:
        # 1.打开的文件2.输出级别3.文件的标题4.备注
        HTMLTestRunner(f,2,"55期的测试报告","使用windows电脑chrome浏览器运行的").run(suite)

    # 运行用例
    # # 创建TextTestRunner类对象
    # runner = unittest.TextTestRunner()
    # # 调用方法运行用例run()
    # runner.run(suite)