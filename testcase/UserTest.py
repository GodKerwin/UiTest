# coding=utf-8

import unittest

from page.user.UserLoginPage import UserLoginPage
from page.user.UserRegisterPage import UserRegisterPage
from public.GetDriver import mydriver
from public.StartAppiumServer import Sp

driver = mydriver()
appiumserver = Sp(driver)


class User(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_register(self):
        '''
        注册
        :return:
        '''
        add = UserRegisterPage(driver)
        add.register()
        add.home()

    def test_user_login(self):
        '''
        登录
        :return:
        '''
        sort = UserLoginPage(driver)
        sort.login()
        sort.home()


if __name__ == "__main__":
    unittest.main()
