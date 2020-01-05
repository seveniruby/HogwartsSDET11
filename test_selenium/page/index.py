from selenium.webdriver.common.by import By

from test_selenium.page.register import Register


class Index:
    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        return Register(self.driver)
