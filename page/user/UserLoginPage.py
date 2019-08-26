# coding=utf-8


import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os
from public.Operate import Operate

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
yamlpath = PATH("../../testyaml/user/user_login.yaml")


class UserLoginPage:

    def __init__(self, driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path, self.driver)

    def login(self):
        self.operate.check_operate_type()

    def home(self):
        self.operate.back_home()
