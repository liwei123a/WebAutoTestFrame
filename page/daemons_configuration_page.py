# -*- coding:utf-8 -*-

from base.find_element import FindElement

class DaemonsConfigurationPage(object):
    def __init__(self, driver, current_node):
        self.fd = FindElement(driver, current_node)

    # 获取添加app按钮元素
    def get_add_app_button_element(self):
        return self.fd.get_element('add_app_button')

    # 获取app名称元素
    def get_app_name_element(self):
        return self.fd.get_element('app_name')

    # 获取包名
    def get_package_name_element(self):
        return self.fd.get_element('package_name')

    # 获取启动页
    def get_launch_page_element(self):
        return self.fd.get_element('launch_page')

    # 获取版本号
    def get_version_element(self):
        return self.fd.get_element('version')

    # 获取下载地址
    def get_download_url_element(self):
        return self.fd.get_element('download_url')

    # 获取保存按钮
    def get_app_save_button_element(self):
        return self.fd.get_element('app_save_button')

    # 获取取消按钮
    def get_app_cancel_button_element(self):
        return self.fd.get_element('app_cancel_button')

    # 获取所有的编辑和删除按钮
    def get_edit_and_delete_button_elements(self):
        return self.fd.get_element('edit_and_delete_buttons')

    # 获取编辑按钮
    def get_edit_app_button_element(self):
        return self.get_edit_and_delete_button_elements()[-2]

    # 获取删除按钮
    def get_delete_app_button_element(self):
        return self.get_edit_and_delete_button_elements()[-1]

    # 获取删除确认按钮
    def get_delete_confirm_button_element(self):
        return self.fd.get_element('delete_confirm_button')

    # 获取app版本数量
    def get_total_items_element(self):
        return self.fd.get_element('total_items')[0]

    # 获取所有app版本
    def get_total_app_version_elements(self):
        return self.fd.get_element('total_app_versions')

    # 获取添加的App版本
    def get_new_app_version_element(self):
        return self.get_total_app_version_elements()[-1]