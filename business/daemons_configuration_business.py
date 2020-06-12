# -*- coding:utf-8 -*-

import time
from handle.daemons_configuration_handle import DaemonsConfigurationHandle

class DaemonsConfigurationBusiness(object):
    def __init__(self, driver, current_node):
        self.handle = DaemonsConfigurationHandle(driver, current_node)

    # 添加app
    def add_app(self, app_name, package_name, launch_page, version, download_url, assert_info):
        # 添加之前获取app版本数量
        total_items_before = self.handle.get_total_items()
        # 添加操作
        self.handle.click_add_app_button()
        self.handle.send_app_name(app_name)
        self.handle.send_package_name(package_name)
        self.handle.send_launch_page(launch_page)
        self.handle.send_version(version)
        self.handle.send_download_url(download_url)
        self.handle.click_app_save_button()
        # 添加之后再次获取app版本数量
        time.sleep(2)
        total_items_after = self.handle.get_total_items()
        return True if total_items_after - total_items_before == int(assert_info) else False

    # 更新app信息
    def update_app(self, app_name, package_name, launch_page, version, download_url):
        sign = None
        # 页面滚动到添加的App位置
        self.handle.scroll_to_new_app_version()
        # 点击编辑按钮，修改内容，保存
        self.handle.click_edit_app_button()
        self.handle.clear_app_name()
        self.handle.send_app_name(app_name)
        self.handle.clear_package_name()
        self.handle.send_package_name(package_name)
        self.handle.clear_launch_page()
        self.handle.send_launch_page(launch_page)
        self.handle.clear_version()
        self.handle.send_version(version)
        self.handle.clear_download_url()
        self.handle.send_download_url(download_url)
        self.handle.click_app_save_button()
        # 再次点击编辑按钮，检查各项内容是否修改成功
        self.handle.click_edit_app_button()
        time.sleep(2)
        sign = True if self.handle.get_app_name() == app_name else False
        sign = True if self.handle.get_package_name() == package_name else False
        sign = True if self.handle.get_launch_page() == launch_page else False
        sign = True if self.handle.get_version() == version else False
        sign = True if self.handle.get_download_url() == download_url else False
        self.handle.click_app_cancel_button()
        return sign

    # 删除APP版本
    def delete_app(self, assert_info):
        # 删除之前获取app版本数量
        total_items_before = self.handle.get_total_items()
        # 页面滚动到添加的App位置
        self.handle.scroll_to_new_app_version()
        # 点击删除
        self.handle.click_delete_app_button()
        self.handle.click_delete_confirm_button()
        time.sleep(2)
        # 删除之后获取app版本数量
        total_items_after = self.handle.get_total_items()
        return True if total_items_before - total_items_after == int(assert_info) else False
