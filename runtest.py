# coding=utf-8

import os
import smtplib
import time
import unittest

import HTMLTestRunner
from public.Sendemail import Email
from public.readConfig import Readconfig
from testcase.UserTest import User

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(User)])

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    now = time.strftime("%y-%m-%d-%H-%M-%S")
    dirpath = PATH("./results/waiqin365-")

    filename = dirpath + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='waiqin365 6.0.6beta test result', description=u'result:')

    runner.run(suite)
    fp.close()


def send_email():
    # 定义发件箱
    conf = Readconfig()
    smtpsever = conf.getemailValue('smtpsever')
    user = conf.getemailValue('user')
    password = conf.getemailValue('password')
    sender = conf.getemailValue('sender')
    receiver = conf.getemailValue('receiver')

    sendemail = Email()
    msg = sendemail.email()

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpsever)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver.split(','), msg.as_string())
    smtp.quit()
    print(u'邮件发送成功')


if __name__ == "__main__":
    testsuit()
    # send_email()
