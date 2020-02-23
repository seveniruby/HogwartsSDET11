# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
        caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        # try:
        #     self.driver.find_element(By.XPATH, "//*[@text='同意']").click()
        # finally:
        #     pass

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # # el3.send_keys("alibaba")
        # el3.send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) > 200

    def test_search_and_get_price_from_hk(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        price = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        assert float(self.driver.find_element(*price).text) < 219
        print(self.driver.find_element(*price).get_attribute("resourceId"))

    def test_scroll(self):
        size = self.driver.get_window_size()

        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_xpath(self):
        # https://www.w3schools.com/xml/xpath_syntax.asp
        self.driver.find_element(
            By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")

    def test_uiselector(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("5小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        # http://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html

    def test_source(self):
        print(self.driver.page_source)

    def test_webview_natvie(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        # self.driver.find_element(By.ID, 'phone-number').send_keys("15600534760")
        submit=(By.XPATH, "//*[@content-desc='立即开户']")
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(submit))
        sleep(2)

        phone = (MobileBy.XPATH, "//android.widget.EditText")
        self.driver.find_element(*phone)
        # self.driver.find_element(*phone).click()
        # self.driver.find_element(*phone).send_keys("15600534760")

        for element in self.driver.find_elements(*phone):
            try:
                # element.click()
                element.send_keys("15600534760")
            except Exception as e:
                print(element.get_attribute("class"))
                print(element.get_attribute("resource-id"))
                print(element.get_attribute("content-desc"))
                print(e)

        # todo: send_keys不生效原因调查

    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

        # 首次做测试的时候，用于分析当前的上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        # print(self.driver.page_source)
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts)>1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()

        #首次做测试的时候，用于分析当前的窗口
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(0.5)
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone=(By.ID, 'phone-number')
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("15600534760")

    def teardown(self):
        pass
        # sleep(20)
        # self.driver.quit()
