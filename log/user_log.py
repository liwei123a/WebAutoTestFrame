# -*- coding:utf-8 -*-
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        # console = logging.StreamHandler()
        # logger.addHandler(console)

        # print(os.path.abspath(__file__))
        # print(os.path.dirname(__file__))
        # print(os.path.dirname(os.path.abspath(__file__)))
        # 定义文件名
        base_dir = os.path.dirname(__file__)
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        log_name = log_dir + '/' + log_file

        # 日志写入文件
        self.file_handle = logging.FileHandler(log_name, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

    def get_logger(self):
        return self.logger

    # console.close()
    # file_handle.close()
    # logger.removeHandler(console)
    # logger.removeHandler(file_handle)