# -*- coding:utf-8 -*-
import configparser

class ReadIni(object):
    def __init__(self, filename=None, node=None):
        if filename is None:
            filename = "../config/element.ini"
        if node is None:
            self.node = "RegisterElements"
        else:
            self.node = node
        self.cf = self.load_ini(filename)

    def load_ini(self, filename):
        cf = configparser.RawConfigParser()
        cf.read(filename, encoding='utf-8')
        return cf

    def get_value(self, key):
        value = self.cf.get(self.node, key)
        return value