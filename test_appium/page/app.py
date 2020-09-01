import datetime
import os
import sys
from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity

            udid=os.getenv("udid", None)
            if udid is not None:
                caps["udid"] = os.getenv("udid", "")
            # caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
            caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"

            # caps['avd'] = 'Pixel_2_API_23'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            #grid模式
            # self._driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            print(self._driver)
            # todo:
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        # todo: wait main page
        def wait_load(driver):
            print(datetime.datetime.now())
            source=self._driver.page_source

            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 60).until(wait_load)
        return Main(self._driver)
