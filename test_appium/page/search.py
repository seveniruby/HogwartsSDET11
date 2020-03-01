from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.base_page import BasePage


class Search(BasePage):
    #todo: 多平台、多版本、多个可能定位符
    _name_locator = (MobileBy.ID, "name")
    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(self._name_locator).click()
        return self
        # todo:

    def get_price(self, key: str) -> float:
        return float(self.find(MobileBy.ID, "current_price").text)
