# -*- coding:utf-8 -*-

import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from business.device_management_business import DeviceManagementBusiness
from case.conftest import driver
from base.get_case_data import GetCaseData

data = GetCaseData('DeviceManagement')
data1 = data.get_data_list('test_page_load_normal')
data2 = data.get_data_list('test_add_device')

class DeviceManagementCase(object):
    def setup_class(self):
        self.current_node = 'DeviceManagementElements'
        self.business = DeviceManagementBusiness(driver, self.current_node)
        driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/deviceApk')
        time.sleep(2)
        driver.implicitly_wait(20)

    # 页面加载
    @pytest.mark.parametrize('content', data1, ids=['页面加载成功'])
    def test_page_load_normal(self, content):
        assert EC.title_contains(content)(driver),'测试失败'

    # 添加设备
    @pytest.mark.parametrize('device_id, device_name, location, longitude, latitude, height_offset, weight_offset, note, assert_info',
                             data2, ids=['添加成功'])
    def test_add_device(self, device_id, device_name, location, longitude, latitude, height_offset, weight_offset, note, assert_info):
        result = self.business.add_device(device_id, device_name, location, longitude, latitude, height_offset, weight_offset, note, assert_info)
        assert result,'测试失败'

    # 查询设备
    def test_query_device(self):
        result = self.business.query_device()
        assert result,'测试失败'

    # 修改设备信息
    def test_update_device(self):
        result = self.business.update_device()
        assert result,'测试失败'

    # 查看设备日志
    def test_view_device_log(self):
        result = self.business.view_device_log()
        assert result,'测试失败'

    # 查看设备数据
    def test_view_device_data(self):
        result = self.business.view_device_data()
        assert result,'测试失败'

    # 删除设备
    def test_delete_device(self):
        result = self.business.delete_device()
        assert result,'测试失败'
