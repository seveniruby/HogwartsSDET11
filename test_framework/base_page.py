import logging

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from test_framework.log import log


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None

    def __init__(self, po_file=None):
        if po_file is not None:
            self._po_file = po_file

    @classmethod
    def start(cls):
        caps = {
            'platformName': 'android',
            'deviceName': 'ceshiren.com',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True
        }
        cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls._driver.implicitly_wait(20)
        return cls

    def stop(self):
        BasePage._driver.quit()

    def find(self, by):
        if by[0] == 'text':
            by_new = (By.XPATH, f'//*[contains(@text, "{by[1]}")]')
        else:
            by_new = by
        self._current_element = BasePage._driver.find_element(*by_new)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    def back(self):
        BasePage._driver.back()
        return self

    def po_run(self, po_method, **kwargs):
        # read yaml
        log.debug(f"po_run {po_method} {kwargs}")
        with open(self._po_file) as f:
            yaml_data = yaml.safe_load(f)
            # find search
            for step in yaml_data[po_method]:
                # find by click send_keys
                if isinstance(step, dict):
                    # id click send_keys
                    for key in step.keys():
                        if key in ['id', 'aid', 'text']:
                            locator = (key, step[key])
                            self.find(locator)

                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            text = str(step[key])
                            for k, v in kwargs.items():
                                text = text.replace('${' + k + '}', v)
                            self.send_keys(text)

                        # todo: 更多关键词
                        else:
                            logging.error(f"dont know {step}")
