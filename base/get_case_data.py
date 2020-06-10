# -*- coding:utf-8 -*-

from until.excel_until import ExcelUntil

class GetCaseData(object):
    def __init__(self, sheetname):
        self.excel = ExcelUntil(sheetname=sheetname)

    # 获取所有Title
    def get_all_titles(self):
        title_list = self.excel.get_col_values(2)
        return title_list

    # 根据title的值返回行号
    def get_title_row(self, title):
        title_list = self.get_all_titles()
        row = title_list.index(title) + 1
        return row

    # 获取Data
    def get_data(self, title):
        row = self.get_title_row(title)
        data = self.excel.get_cell_value(row, 3)
        return data

    # 获取ErrorInfo
    def get_error_info(self, title):
        row = self.get_title_row(title)
        error_info = self.excel.get_cell_value(row, 4)
        return error_info