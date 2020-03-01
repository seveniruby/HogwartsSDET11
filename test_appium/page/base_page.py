from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    #todo: 当有广告、评价等各种弹框出现的时候，要进行异常流程处理
    def find(self, locator, value: str = None):
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)
