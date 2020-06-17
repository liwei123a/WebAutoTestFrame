# -*- coding:utf-8 -*-

import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from business.daemons_configuration_business import DaemonsConfigurationBusiness
from case.conftest import driver
from case.conftest import logger
from base.get_case_data import GetCaseData

# 获取测试数据
data = GetCaseData('DaemonsConfiguration')
data1 = data.get_data_list('test_page_load_normal')
data2 = data.get_data_list('test_add_app')
data3 = data.get_data_list('test_update_app')
data4 = data.get_data_list('test_delete_app')

class DaemonsConfigurationCase(object):
    def setup_class(self):
        self.current_node = 'DaemonsConfigurationElements'
        self.business = DaemonsConfigurationBusiness(driver, self.current_node)
        # self.data = GetCaseData('DaemonsConfiguration')
        driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/magicmirrorOld')
        logger.debug('WebAutoTest starting...')
        time.sleep(2)

    # def setup_method(self, method):
    #     title = method.__name__
    #     data_list = data.get_data_list(title)

    # 页面加载
    @pytest.mark.parametrize('content', data1, ids=['页面加载成功'])
    def test_page_load_normal(self, content):
        assert EC.title_contains(content)(driver),'测试失败'

    # 添加app
    @pytest.mark.parametrize('app_name, package_name, launch_page, version, download_url, assert_info', data2,
                             ids=['未输入package_name,添加失败', '添加成功', '已存在相同App,不能重复添加'])
    def test_add_app(self, app_name, package_name, launch_page, version, download_url, assert_info):
        result = self.business.add_app(app_name, package_name, launch_page, version, download_url, assert_info)
        assert result,'测试失败'

    # 更新app信息
    @pytest.mark.parametrize('app_name, package_name, launch_page, version, download_url', data3, ids=['更新App成功'])
    def test_update_app(self, app_name, package_name, launch_page, version, download_url):
        result = self.business.update_app(app_name, package_name, launch_page, version, download_url)
        assert result,'测试失败'

    # 删除app
    @pytest.mark.parametrize('assert_info', data4, ids=['删除app成功'])
    def test_delete_app(self, assert_info):
        result = self.business.delete_app(assert_info)
        assert result,'测试失败'
