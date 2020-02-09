from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # 使用已经存在的chrome进程
                #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def close(self):
        sleep(20)
        self._driver.quit()
