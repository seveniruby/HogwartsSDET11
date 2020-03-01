from appium import webdriver

from test_appium.page.main import Main


class App:
    def start(self):
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

        # caps['avd'] = 'Pixel_2_API_23'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        #todo: wait mian page
        return Main(self.driver)
