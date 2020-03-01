from appium import webdriver
from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
            caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"

            # caps['avd'] = 'Pixel_2_API_23'

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(30)
        else:
            print(self._driver)
            # todo:
            self._driver.start_activity(self._package, self._activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        # todo: wait man page
        return Main(self._driver)
