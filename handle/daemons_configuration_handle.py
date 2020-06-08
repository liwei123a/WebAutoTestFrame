# -*- coding:utf-8 -*-

from page.daemons_configuration_page import DaemonsConfigurationPage

class DaemonsConfigurationHandle(object):
    def __init__(self, driver, current_node):
        self.page = DaemonsConfigurationPage(driver, current_node)
        self.driver = driver

    # 点击新增app
    def click_add_app_button(self):
        self.page.get_add_app_button_element().click()

    # 输入app名称
    def send_app_name(self, app_name):
        self.page.get_app_name_element().send_keys(app_name)

    # 获取App名称
    def get_app_name(self):
        return self.page.get_app_name_element().get_attribute('value')

    # 清空App名称
    def clear_app_name(self):
        self.page.get_app_name_element().clear()

    # 输入包名
    def send_package_name(self, package_name):
        self.page.get_package_name_element().send_keys(package_name)

    # 获取包名
    def get_package_name(self):
        return self.page.get_package_name_element().get_attribute('value')

    # 清空App包名
    def clear_package_name(self):
        self.page.get_package_name_element().clear()

    # 输入启动页
    def send_launch_page(self, launch_page):
        self.page.get_launch_page_element().send_keys(launch_page)

    # 获取启动页
    def get_launch_page(self):
        return self.page.get_launch_page_element().get_attribute('value')

    # 清空启动页
    def clear_launch_page(self):
        self.page.get_launch_page_element().clear()

    # 输入版本号
    def send_version(self, version):
        self.page.get_version_element().send_keys(version)

    # 获取版本号
    def get_version(self):
        return self.page.get_version_element().get_attribute('value')

    # 清空版本号
    def clear_version(self):
        self.page.get_version_element().clear()

    # 输入下载地址
    def send_download_url(self, download_url):
        self.page.get_download_url_element().send_keys(download_url)

    # 获取下载地址
    def get_download_url(self):
        return self.page.get_download_url_element().get_attribute('value')

    # 清空下载地址
    def clear_download_url(self):
        self.page.get_download_url_element().clear()

    # 点击保存按钮
    def click_app_save_button(self):
        self.page.get_app_save_button_element().click()

    # 点击取消按钮
    def click_app_cancel_button(self):
        self.page.get_app_cancel_button_element().click()

    # 页面滚动到添加的App版本位置
    def scroll_to_new_app_version(self):
        new_app_version = self.page.get_new_app_version_element()
        self.driver.execute_script('arguments[0].scrollIntoView(false);', new_app_version)

    # 点击编辑按钮
    def click_edit_app_button(self):
        self.page.get_edit_app_button_element().click()

    # 点击删除按钮
    def click_delete_app_button(self):
        self.page.get_delete_app_button_element().click()

    # 点击确认删除按钮
    def click_delete_confirm_button(self):
        self.page.get_delete_confirm_button_element().click()

    # 获取app版本数量
    def get_total_items(self):
        total_items_s = self.page.get_total_items_element().text
        print(total_items_s)
        total_items_n = int(total_items_s.split()[1])
        return total_items_n