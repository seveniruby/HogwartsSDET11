from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact


class Main(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def download(self):
        pass

    def import_user(self, path):
        self.find((By.PARTIAL_LINK_TEXT, "导入成员")).click()
        self.find((By.LINK_TEXT, "批量导入")).click()
        self.find((By.ID, "js_upload_file_input")).send_keys(path)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ["aaa", "bbbb"]

    def add_member(self):
        locator=(By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)
