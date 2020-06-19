# -*- coding:utf-8 -*-

import time
from handle.device_management_handle import DeviceManagementHandle

class DeviceManagementBusiness(object):
    def __init__(self, driver, current_node):
        self.handle = DeviceManagementHandle(driver, current_node)

    # 添加设备
    def add_device(self, device_id, device_name, location, longitude, latitude, height_offset, weight_offset, note, assert_info):
        # 添加操作
        self.handle.click_add_device_button()
        self.handle.click_choose_app()
        self.handle.click_app_type()
        self.handle.click_choose_version()
        self.handle.click_version_type()
        self.handle.send_device_id(device_id)
        self.handle.send_device_name(device_name)
        self.handle.click_choose_organization()
        self.handle.click_organization_type()
        self.handle.click_choose_channel()
        self.handle.click_channel_type()
        self.handle.click_choose_industry()
        self.handle.click_industry_type()
        self.handle.click_choose_apk_version()
        self.handle.click_apk_version_num()
        self.handle.click_choose_language()
        self.handle.click_language_type()
        # 页面底部滚动到摄像头角度位置
        self.handle.scroll_to_camera_angle()
        self.handle.click_choose_city()
        self.handle.click_city_name()
        self.handle.send_location(location)
        self.handle.send_longitude(longitude)
        self.handle.send_latitude(latitude)
        self.handle.send_height_offset(height_offset)
        self.handle.send_weight_offset(weight_offset)
        # 页面底部滚动到备注位置
        self.handle.scroll_to_note()
        self.handle.click_inquiry_switch()
        self.handle.click_skin_check_switch()
        self.handle.send_note(note)
        self.handle.click_save_button()
        time.sleep(1)
        if self.handle.check_el_message_is_present():
            el_message = self.handle.get_el_message()
            self.handle.click_cancel_button()
            return True if el_message == assert_info else False
        else:
            self.handle.send_search_device_id(device_id)
            self.handle.click_search_button()
            time.sleep(1)
            search_device_id = self.handle.get_search_device_id()
            return True if device_id == search_device_id else False

    # 查询设备
    def query_device(self):
        pass

    # 修改设备信息
    def update_device(self):
        pass

    # 查看设备日志
    def view_device_log(self):
        pass

    # 查看设备数据
    def view_device_data(self):
        pass

    # 删除设备
    def delete_device(self):
        pass