from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWXMicroNative:
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


    def test_search_native(self):
        self.driver.find_element(By.XPATH, "//*[@text='上证指数']").click()
        self.driver.find_element(By.XPATH, "//*[@text='5日']").click()
        self.driver.find_element(By.XPATH, "//*[@text='日K']").click()
        self.driver.find_element(By.XPATH, "//*[@text='月K']").click()
