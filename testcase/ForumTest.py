# coding=utf-8


import time
import unittest

from page.forum.ForumSearchPage import ForumSearchPage
from public.GetDriver import mydriver
from public.StartAppiumServer import Sp

driver = mydriver()
appiumserver = Sp(driver)


class Cm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_001searchpd(self):
        '''
        搜索商品
        :return:
        '''
        add = ForumSearchPage(driver)
        add.operateap()
        add.home()

    def test_999close(self):
        driver.quit()
        appiumserver.stop_appium()
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
