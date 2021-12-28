from appium import webdriver
import os


class PasswordTool(object):
    def __init__(self):
        super().__init__()

        rootdir = os.path.dirname(os.path.abspath(__file__))
        appPath = os.path.join(
            rootdir, "tool", "tool.exe").replace("\\", "/")
        # print(appPath)

        self.desired_caps = {}
        # rootdir + "/tool/tool.exe"
        self.desired_caps['platformName'] = 'Windows'
        self.desired_caps['automationName'] = 'Windows'
        self.desired_caps['app'] = appPath
        self.driver = webdriver.Remote(
            "http://127.0.0.1:4723", self.desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        if self.driver != None:
            self.driver.close()
            self.driver.quit()

    def get_all_windows(self):
        if self.driver != None:
            return self.driver.window_handles
        else:
            return None

    def keyin_login_password(self, pwd):
        self.driver.find_element_by_accessibility_id(
            "textPassword").send_keys(pwd)
        return self

    def click_ok(self):
        self.driver.find_element_by_accessibility_id("btnDone").click()
        return self

    def keyin_serialsn(self, sn):
        self.driver.find_element_by_accessibility_id(
            "txtSerialSN").send_keys(sn)
        return self

    def keyin_password(self, pwd):
        self.driver.find_element_by_accessibility_id(
            "txtPassword").send_keys(pwd)
        return self

    def click_generate(self):
        self.driver.find_element_by_accessibility_id("btnGenerate").click()
        return self
