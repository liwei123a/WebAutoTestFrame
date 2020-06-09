# -*- coding:utf-8 -*-

import pytest
import time
from selenium import webdriver

driver = webdriver.Chrome()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    ** 作者：上海-悠悠 QQ交流群：588402570**
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''
    ** 作者：上海-悠悠 QQ交流群：588402570**
    截图保存为base64，展示到html中
    :return:
    '''
    return driver.get_screenshot_as_base64()

@pytest.fixture(scope='session', autouse=True)
def handle_browser():
    driver.maximize_window()
    driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/')
    time.sleep(2)
    cookie = {'name': 'SESSION', 'value': 'MzQyNGQ1YjktYWI0Ny00YTQxLTk4MWItOGQ2ZmQ0ZDY3NjM2'}
    driver.add_cookie(cookie)
    time.sleep(2)
    yield
    driver.quit()