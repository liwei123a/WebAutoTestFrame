# -*- coding:utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from page.device_management_page import DeviceManagementPage

class DeviceManagementHandle(object):
    def __init__(self, driver, current_node):
        self.page = DeviceManagementPage(driver, current_node)
        self.driver = driver

    # 获取设备数量
    def get_total_items(self):
        total_items_s = self.page.get_total_items_element().text
        total_items_n = int(total_items_s.split()[1])
        return total_items_n

    # 点击添加设备按钮
    def click_add_device_button(self):
        self.page.get_add_device_button_element().click()

    # 点击选择app下拉框
    def click_choose_app(self):
        self.page.get_choose_app_element().click()

    # 选择app类型
    def click_app_type(self):
        self.page.get_app_type_element().click()

    # 点击选择版本下拉框
    def click_choose_version(self):
        self.page.get_choose_version_element().click()

    # 选择版本类型
    def click_version_type(self):
        self.page.get_version_type_element().click()

    # 输入设备id
    def send_device_id(self, device_id):
        self.page.get_device_id_element().send_keys(device_id)

    # 输入设备名称
    def send_device_name(self, device_name):
        self.page.get_device_name_element().send_keys(device_name)

    # 点击选择机构下拉框
    def click_choose_organization(self):
        self.page.get_choose_organization_element().click()

    # 选择机构类型
    def click_organization_type(self):
        self.page.get_organization_type_element().click()

    # 点击选择渠道下拉框
    def click_choose_channel(self):
        self.page.get_choose_channel_element().click()

    # 选择渠道
    def click_channel_type(self):
        self.page.get_channel_type_element().click()

    # 点击选择行业下拉框
    def click_choose_industry(self):
        self.page.get_choose_industry_element().click()

    # 选择行业
    def click_industry_type(self):
        self.page.get_industry_type_element().click()

    # 点击选择apk版本下拉框
    def click_choose_apk_version(self):
        self.page.get_choose_apk_version_element().click()

    # 选择apk版本
    def click_apk_version_num(self):
        self.page.get_apk_version_num_element().click()

    # 点击选择语言下拉框
    def click_choose_language(self):
        self.page.get_choose_language_element().click()

    # 选择语言
    def click_language_type(self):
        self.page.get_language_type_element().click()

    # 页面底部滚动到摄像头角度位置
    def scroll_to_camera_angle(self):
        camera_angle_element = self.page.get_camera_angle_element()
        self.driver.execute_script('arguments[0].scrollIntoView(false);', camera_angle_element)

    # 点击选择城市下拉框
    def click_choose_city(self):
        self.page.get_choose_city_element().click()

    # 选择城市
    def click_city_name(self):
        self.page.get_city_name_element().click()

    # 输入位置
    def send_location(self, location):
        self.page.get_location_element().send_keys(location)

    # 输入经度
    def send_longitude(self, longitude):
        self.page.get_longitude_element().send_keys(longitude)

    # 输入纬度
    def send_latitude(self, latitude):
        self.page.get_latitude_element().send_keys(latitude)

    # 输入身高偏移
    def send_height_offset(self, height_offset):
        self.page.get_height_offset_element().send_keys(height_offset)

    # 输入体重偏移
    def send_weight_offset(self, weight_offset):
        self.page.get_weight_offset_element().send_keys(weight_offset)

    # 页面底部滚动到备注位置
    def scroll_to_note(self):
        note_element = self.page.get_note_element()
        self.driver.execute_script('arguments[0].scrollIntoView(false);', note_element)

    # 打开视频问诊开关
    def click_inquiry_switch(self):
        self.page.get_inquiry_switch_element().click()

    # 打开肤质检测开关
    def click_skin_check_switch(self):
        self.page.get_skin_check_switch_element().click()

    # 输入备注
    def send_note(self, note):
        self.page.get_note_element().send_keys(note)

    # 点击保存按钮
    def click_save_button(self):
        self.page.get_save_button_element().click()

    # 点击取消按钮
    def click_cancel_button(self):
        self.page.get_cancel_button_element().click()

    # 获取搜索的设备id
    def get_search_device_id(self):
        return self.page.get_search_device_id_element().text

    # 输入查询的设备id
    def send_search_device_id(self, device_id):
        self.page.get_input_device_id_element().send_keys(device_id)

    # 点击搜索按钮
    def click_search_button(self):
        self.page.get_search_button_element().click()

    # 检查提示文案是否出现
    def check_el_message_is_present(self):
        try:
            el_message_element = self.page.get_el_message_element()
        except NoSuchElementException as e:
            return False
        else:
            return True

    # 获取提示文案内容
    def get_el_message(self):
        return self.page.get_el_message_element()[0].text
