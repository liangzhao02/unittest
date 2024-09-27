import unittest
from time import sleep
from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        实例化浏览器驱动对象
        打开页面
        浏览器最大化
        隐式等待
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('http://info.itfeat.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        """
        关闭浏览器
        :return:
        """
        sleep(3)
        self.driver.quit()

    def test_login1(self):
        """
        登录成功的case
        :return:
        """
        self.driver.find_element_by_link_text('登录').click()

        self.driver.find_element_by_id('mobile').send_keys('15296797153')
        # 登录成功
        self.driver.find_element_by_id('password').send_keys('123456')

        self.driver.find_element_by_xpath('//input[@value="登 录"]').click()

        assert self.driver.find_element_by_id("nick_name").text == '天天向上'


    def test_login2(self):
        """
        登录失败的case
        :return:
        """
        self.driver.find_element_by_link_text('登录').click()

        self.driver.find_element_by_id('mobile').send_keys('15296797153')
        # 登录成功
        self.driver.find_element_by_id('password').send_keys('123')

        self.driver.find_element_by_xpath('//input[@value="登 录"]').click()

        sleep(3)
        alert = self.driver.switch_to.alert
        assert alert.text == '用户名或者密码错误'

