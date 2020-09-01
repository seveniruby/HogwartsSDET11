from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Search(BasePage):
    # todo: 多平台、多版本、多个可能定位符
    _name_locator = (MobileBy.ID, "name")

    def search(self, key: str):
        # self.find(MobileBy.ID, "search_input_text").send_keys(key)
        # self.find(self._name_locator).click()

        self._params={}
        self._params["key"]=key
        self.steps("../page/search.yaml")

        return self

    def get_price(self, key: str) -> float:
        return float(self.find(MobileBy.ID, "current_price").text)

    def add_select(self):
        element = self.find_by_text("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已添加")
        element.click()
        return self

    def get_msg(self):
        return self.get_text(By.ID, "followed_btn")
