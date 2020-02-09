from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button=(By.CSS_SELECTOR, "xxxx")
    def add_member(self, data):
        #self.driver.find_element("添加成员").click
        #sendkeys
        #click save
        name_locator=(By.NAME, 'username')
        acctid_locator=(By.NAME, 'acctid')
        #$('.ww_radio[value="2"]')
        gender_locator=(By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile_locator=(By.NAME, 'mobile')
        self.find(name_locator).send_keys("seveniruby")
        self.find(acctid_locator).send_keys("seveniruby")
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(mobile_locator).send_keys("15600534760")

    def add_member_error(self, data):
        return AddMemberPage()


    def search(self, name):
        pass

    def import_users(self, data):
        pass

    def export_users(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass
