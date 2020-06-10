# -*- coding:utf-8 -*-

import sys
import time
from selenium.webdriver.support import expected_conditions as EC
from business.daemons_configuration_business import DaemonsConfigurationBusiness
from case.conftest import driver
from base.get_case_data import GetCaseData

class DaemonsConfigurationCase(object):
    def setup_class(self):
        self.current_node = 'DaemonsConfigurationElements'
        self.business = DaemonsConfigurationBusiness(driver, self.current_node)
        self.data = GetCaseData('DaemonsConfiguration')
        driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/magicmirrorOld')
        time.sleep(2)

    # 页面加载
    def test_page_load_normal(self):
        title = sys._getframe().f_code.co_name
        data = self.data.get_data(title)
        error_info = self.data.get_error_info(title)
        assert EC.title_contains(data)(driver),error_info

    # 添加app
    def test_add_app(self):
        title = sys._getframe().f_code.co_name
        data = self.data.get_data(title)
        error_info = self.data.get_error_info(title)
        app_name, package_name, launch_page, version, download_url = data.split(',')
        result = self.business.add_app(app_name, package_name, launch_page, version, download_url)
        assert result,error_info

    # 更新app信息
    def test_update_app(self):
        title = sys._getframe().f_code.co_name
        data = self.data.get_data(title)
        error_info = self.data.get_error_info(title)
        app_name, package_name, launch_page, version, download_url = data.split(',')
        result = self.business.update_app(app_name, package_name, launch_page, version, download_url)
        assert result,error_info

    # 删除app
    def test_delete_app(self):
        title = sys._getframe().f_code.co_name
        error_info = self.data.get_error_info(title)
        result = self.business.delete_app()
        assert result,error_info
