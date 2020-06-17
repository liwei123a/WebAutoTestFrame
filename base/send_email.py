# -*- coding:utf-8 -*-

from case.conftest import test_result_summary
from until.email_until import EmailUntil
from until.read_ini import ReadIni

# total = test_result_summary['total']
# passed = test_result_summary['passed']
# failed = test_result_summary['failed']
# error = test_result_summary['error']
# skipped = test_result_summary['skipped']
# pass_rate = test_result_summary['pass_rate']
# test_time = test_result_summary['test_time']

email_ini = ReadIni(filename='config/email.ini', node='email')

class SendEmail(object):
    def __init__(self):
        self.smtpserver = email_ini.get_value('smtpserver')
        self.sender = email_ini.get_value('sender')
        self.password = email_ini.get_value('password')
        self.receiver = email_ini.get_value('receiver').split(',')
        self.username = email_ini.get_value('username')
        self.subject = email_ini.get_value('subject')
        self.content = email_ini.get_value('content') % (test_result_summary['total'], test_result_summary['passed'],
                                                         test_result_summary['failed'], test_result_summary['error'],
                                                         test_result_summary['skipped'], test_result_summary['pass_rate'],
                                                         test_result_summary['test_time'])
        self.filename = email_ini.get_value('filename')
        self.email = EmailUntil(self.smtpserver, self.sender, self.password)

    def send(self):
        self.email.send(self.username, self.receiver, self.subject, self.content, self.filename)