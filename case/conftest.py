# -*- coding:utf-8 -*-

import pytest
import time
from selenium import webdriver
from _pytest import terminal
from log.user_log import UserLog

# 定义driver
driver = webdriver.Chrome()

# 定义日志
log = UserLog()
logger = log.get_logger()

# 定义测试结果
test_result_summary = {}

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
    '''浏览器初始化'''
    driver.maximize_window()
    driver.get('https://web-qa.doctorwork.com/app/smart-device-panel/')
    time.sleep(2)
    cookie = {'name': 'SESSION', 'value': 'ZTQwZGQxODctZWMwYy00N2M4LTgxY2EtODA2ZmIyYjBkZDZl'}
    driver.add_cookie(cookie)
    time.sleep(2)
    yield
    log.close_handle()
    driver.quit()

# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    # print("total:", terminalreporter._numcollected)
    # print('passed:', len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown']))
    # print('failed:', len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']))
    # print('error:', len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']))
    # print('skipped:', len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown']))
    # print('成功率：%.2f' % (len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100)+'%')

    # terminalreporter._sessionstarttime 会话开始时间
    duration = '{:.2f}'.format(time.time() - terminalreporter._sessionstarttime)
    # print('total times:', duration, 'seconds')
    test_result_summary['total'] = terminalreporter._numcollected
    test_result_summary['passed'] = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    test_result_summary['failed'] = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    test_result_summary['error'] = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    test_result_summary['skipped'] = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    test_result_summary['pass_rate'] = '%.2f' % (len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100)+'%'
    test_result_summary['test_time'] = duration
