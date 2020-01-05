from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)

            self.driver.get(self._base_url)
        else:
            self.driver = driver