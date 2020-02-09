import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    browser="reuse"

    def setup_method(self):
        browser = os.getenv("browser", "").lower() if self.browser=="" else self.browser
        print(browser)

        if browser == "phantomjs":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            options = webdriver.ChromeOptions()
            # 使用headless模式
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280,1696")

            self.driver = webdriver.Chrome(options=options)
        elif browser=='reuse':
            options = webdriver.ChromeOptions()
            # 使用已经存在的chrome进程
            #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            options.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()
            # 使用已经存在的chrome进程
            #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            # options.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)

        if browser != 'reuse':
            self.driver.get("https://testerhome.com/")

        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        # todo: 显式等待
        # 尽量使用css的定位方法集，link有可能会导致解析元素的时候出现异常

        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element)>1)

        self.driver.find_element(*element).click()
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # done：隐式等待
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_jinshuju(self):
        self.driver.get("https://testerhome.com/topics/21495")
        submit = (By.CSS_SELECTOR, ".published-form__submit")

        self.driver.switch_to.frame(0)
        self.wait(10, expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(By.CSS_SELECTOR, ".published-form__submit").click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.set_window_size(1440, 877)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        element = (By.LINK_TEXT, '演讲申请')
        self.driver.save_screenshot("1.png")
        self.wait(10, expected_conditions.presence_of_element_located(element))
        self.driver.find_element(*element).click()

    def test_js(self):
        # todo: 专项测试的时候会讲如何获取性能
        for code in [
            "return document.title",
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def test_shetuan(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/teams"]').click()

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.maximize_window()
        element_locator=(By.CSS_SELECTOR, 'a[node-type="addmember"]')
        element_locator = (By.LINK_TEXT, "添加成员")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
        element=self.driver.find_element(*element_locator)
        print(element.text)
        # sleep(5)
        element.click()
        # self.driver.execute_script("arguments[0].click();", element)

        self.driver.find_element(By.NAME, 'username').send_keys("abc")
        self.driver.find_element(By.NAME,'english_name').send_keys("abc")
        self.driver.find_element(By.NAME, "acctid").send_keys("abc")
        # self.driver.find_element(By.CSS_SELECTOR, '.ww_radio+span:contains("女")').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input input').click()
        self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="853"]').click()

    def test_import(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.LINK_TEXT, "导入通讯录").click()
        # element_locator=(By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_fileInputWrap")
        element_locator=(By.ID, "js_upload_file_input")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
        self.driver.find_element(*element_locator)\
            .send_keys("/Users/seveniruby/PycharmProjects/HogwartsSDET11/test_selenium/testcase/通讯录批量导入模板.xlsx")



    def teardown_method(self):
        sleep(5)
        self.driver.quit()
