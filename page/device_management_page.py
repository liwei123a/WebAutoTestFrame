# -*- coding:utf-8 -*-

from base.find_element import FindElement

class DeviceManagementPage(object):
    def __init__(self, driver, current_node):
        self.fd = FindElement(driver, current_node)

    # 获取设备数量
    def get_total_items_element(self):
        return self.fd.get_element('total_items')

    # 获取添加设备按钮
    def get_add_device_button_element(self):
        return self.fd.get_element('add_device_button')

    # 获取app下拉框
    def get_choose_app_element(self):
        return self.fd.get_element('choose_app')

    # 获取app类型
    def get_app_type_element(self):
        return self.fd.get_element('app_type')

    # 获取版本下拉框
    def get_choose_version_element(self):
        return self.fd.get_element('choose_version')

    # 获取版本类型
    def get_version_type_element(self):
        return self.fd.get_element('version_type')

    # 获取设备id
    def get_device_id_element(self):
        return self.fd.get_element('device_id')

    # 获取设备名称
    def get_device_name_element(self):
        return self.fd.get_element('device_name')

    # 获取机构下拉框
    def get_choose_organization_element(self):
        return self.fd.get_element('choose_organization')

    # 获取机构
    def get_organization_type_element(self):
        return self.fd.get_element('organization_type')

    # 获取渠道下拉框
    def get_choose_channel_element(self):
        return self.fd.get_element('choose_channel')

    # 获取渠道
    def get_channel_type_element(self):
        return self.fd.get_element('channel_type')

    # 获取行业下拉框
    def get_choose_industry_element(self):
        return self.fd.get_element('choose_industry')

    # 获取行业
    def get_industry_type_element(self):
        return self.fd.get_element('industry_type')

    # 获取apk版本下拉框
    def get_choose_apk_version_element(self):
        return self.fd.get_element('choose_apk_version')

    # 获取apk版本
    def get_apk_version_num_element(self):
        return self.fd.get_element('apk_version_num')

    # 获取语言下拉框
    def get_choose_language_element(self):
        return self.fd.get_element('choose_language')

    # 获取语言
    def get_language_type_element(self):
        return self.fd.get_element('language_type')

    # 获取摄像头角度
    def get_camera_angle_element(self):
        return self.fd.get_element('camera_angle')

    # 获取城市下拉框
    def get_choose_city_element(self):
        return self.fd.get_element('choose_city')

    # 获取城市
    def get_city_name_element(self):
        return self.fd.get_element('city_name')

    # 获取位置
    def get_location_element(self):
        return self.fd.get_element('location')

    # 获取经度
    def get_longitude_element(self):
        return self.fd.get_element('longitude')

    # 获取纬度
    def get_latitude_element(self):
        return self.fd.get_element('latitude')

    # 获取身高偏移
    def get_height_offset_element(self):
        return self.fd.get_element('height_offset')

    # 获取体重偏移
    def get_weight_offset_element(self):
        return self.fd.get_element('weight_offset')

    # 获取备注
    def get_note_element(self):
        return self.fd.get_element('note')

    # 获取视频问诊开关
    def get_inquiry_switch_element(self):
        return self.fd.get_element('inquiry_switch')

    # 获取肤质检测开关
    def get_skin_check_switch_element(self):
        return self.fd.get_element('skin_check_switch')

    # 获取保存按钮
    def get_save_button_element(self):
        return self.fd.get_element('save_button')

    # 获取取消按钮
    def get_cancel_button_element(self):
        return self.fd.get_element('cancel_button')

    # 获取搜索的设备id
    def get_search_device_id_element(self):
        return self.fd.get_element('search_device_id')

    # 获取搜索按钮
    def get_search_button_element(self):
        return self.fd.get_element('search_button')

    # 获取输入的设备id
    def get_input_device_id_element(self):
        return self.fd.get_element('input_device_id')

    # 获取提示文案
    def get_el_message_element(self):
        return self.fd.get_element('el_message')