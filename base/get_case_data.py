# -*- coding:utf-8 -*-

from until.excel_until import ExcelUntil

class GetCaseData(object):
    def __init__(self, sheetname):
        self.excel = ExcelUntil(sheetname=sheetname)

    # 获取列表相同值的索引
    def get_index_list(self, title, title_list):
        index_list = []
        for index, value in enumerate(title_list):
            if value == title:
                index_list.append(index)
        return index_list

    # 获取所有Title
    def get_all_titles(self):
        title_list = self.excel.get_col_values(2)
        return title_list

    # 根据title的值返回行号
    def get_title_row_list(self, title):
        title_list = self.get_all_titles()
        index_list = self.get_index_list(title, title_list)
        row_list = [index+1 for index in index_list]
        return row_list

    # 获取Data
    def get_data_list(self, title):
        row_list = self.get_title_row_list(title)
        data_list = []
        for row in row_list:
            data = str(self.excel.get_cell_value(row, 3))
            param_list = data.split(',')
            if len(param_list) > 1:
                data_list.append(tuple(param_list))
            else:
                data_list.append(data)
        return data_list


# if __name__ == '__main__':
#     data = GetCaseData('DaemonsConfiguration')
#     data_list = data.get_data_list('test_update_app')
#     print(data_list)