from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWXMicroWebView:
    # 为了演示方便，未使用page object模式
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "测试人社区 ceshiren.com"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        caps['chromedriverExecutable'] = \
            '/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_78.0.3904.11'

        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }

        caps['adbPort'] = 5038

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

        self.enter_micro_program()
        print(self.driver.contexts)

    def enter_micro_program(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.9)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选']")

    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)

    def test_search_webview(self):
        # 进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()
