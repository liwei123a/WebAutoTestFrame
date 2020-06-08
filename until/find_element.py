# -*- coding:utf-8 -*-
from until.read_ini import ReadIni

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver
        self.elements = ReadIni()

    def get_element(self, key):
        element = self.elements.get_value(key)
        by, value = element.split(">")
        find_element_dict = {
            "id":lambda value:self.driver.find_element_by_id(value),
            "xpath":lambda value:self.driver.find_element_by_xpath(value),
            "name":lambda value:self.driver.find_element_by_name(value),
            "classname":lambda value:self.driver.find_element_by_class_name(value),
            "css_selector":lambda value:self.driver.find_element_by_css_selector(value),
            "link_text":lambda value:self.driver.find_element_by_link_text(value),
            "partial_link_text":lambda value:self.driver.find_element_by_partial_link_text(value),
            "tag_name":lambda value:self.driver.find_element_by_tag_name(value)
        }
        return find_element_dict.get(by)(value)

    def get_locator(self, key, By):
        element = self.elements.get_value(key)
        by, value = element.split(">")
        locator_dict = {
            "id": lambda value:(By.ID, value),
            "xpath": lambda value:(By.XPATH, value),
            "name": lambda value:(By.NAME, value),
            "classname": lambda value:(By.CLASS_NAME, value),
            "css_selector": lambda value:(By.CSS_SELECTOR, value),
            "link_text": lambda value:(By.LINK_TEXT, value),
            "partial_link_text": lambda value:(By.PARTIAL_LINK_TEXT, value),
            "tag_name": lambda value:(By.TAG_NAME, value)
        }
        return locator_dict.get(by)(value)