# -*- coding:utf-8 -*-

import time
from selenium.webdriver.support import expected_conditions as EC
from business.daemons_configuration_business import DaemonsConfigurationBusiness
from case.conftest import driver

class DaemonsConfigurationCase(object):
    # def __init__(self):
    #     self.current_node = 'DaemonsConfigurationElements'
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/')
    #     time.sleep(2)
    #     self.cookie = {'name': 'SESSION', 'value': 'MzQyNGQ1YjktYWI0Ny00YTQxLTk4MWItOGQ2ZmQ0ZDY3NjM2'}
    #     self.driver.add_cookie(self.cookie)
    #     time.sleep(2)
    #     self.driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/magicmirrorOld')
    #     self.driver.maximize_window()
    #     self.business = DaemonsConfigurationBusiness(self.driver, self.current_node)
    #     time.sleep(2)
    def setup_class(self):
        self.current_node = 'DaemonsConfigurationElements'
        self.business = DaemonsConfigurationBusiness(driver, self.current_node)
        driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/magicmirrorOld')
        time.sleep(2)

    # 页面加载
    def test_page_load_normal(self):
        # if EC.title_contains('守护进程配置')(driver):
        #     print('页面加载成功')
        # else:
        #     print('页面加载失败')
        assert EC.title_contains('守护进程配置')(driver),'页面加载失败'

    # 添加app
    def test_add_app(self):
        app_name = '添加app名称'
        package_name = 'add_package_name'
        launch_page = 'add_launch_page'
        version = 'add_version'
        download_url = 'add_download_url'
        result = self.business.add_app(app_name, package_name, launch_page, version, download_url)
        # if result:
        #     print('添加成功')
        # else:
        #     print('添加失败')
        assert result,'添加失败'

    # 更新app信息
    def test_update_app(self):
        app_name = '更新app名称'
        package_name = 'update_package_name'
        launch_page = 'update_launch_page'
        version = 'update_version'
        download_url = 'update_download_url'
        result = self.business.update_app(app_name, package_name, launch_page, version, download_url)
        # if result:
        #     print('更新成功')
        # else:
        #     print('更新失败')
        assert result,'更新失败'

    # 删除app
    def test_delete_app(self):
        result = self.business.delete_app()
        # if result:
        #     print('删除成功')
        # else:
        #     print('删除失败')
        assert result,'删除失败'

    # 清理环境，退出测试
    # def clear_env(self):
    #     self.driver.quit()

# if __name__ == '__main__':
#     test_case = DaemonsConfigurationCase()
#     test_case.test_page_load_normal()
#     test_case.test_add_app()
#     test_case.test_update_app()
#     test_case.test_delete_app()
    # test_case.clear_env()
