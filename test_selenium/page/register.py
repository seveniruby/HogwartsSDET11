from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, corpname):
        self._driver.find_element(By.ID, "corp_name").send_keys(corpname)
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):
        result=[]
        for element in self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg"):
            result.append(element.text)

        return result
