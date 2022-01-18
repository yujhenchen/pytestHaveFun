import imp
from unittest.mock import NonCallableMagicMock
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSuite(object):
    driver = None
    url = "https://www.google.com/"
    remote_url_chrome = "http://localhost:4445/wd/hub"
    element_wait_time = 10

    # # Remove init method to allow run using pytest
    # def __init__(self):
    #     super().__init__()

    def setup_class(self):
        # init driver
        self.driver = webdriver.Remote(self.remote_url_chrome)
        self.driver.get(self.url)

    def teardown_class(self):
        if self.driver is not None:
            self.driver.quit()

    def take_screenshot(self):
        if self.driver is not None:
            self.driver.save_screenshot("searchResult.png")
        else:
            print("take_screenshot: Failed: driver is None")

    def test_search(self):
        # keyin search keyword and submit
        element = WebDriverWait(self.driver, self.element_wait_time).until(
            EC.element_to_be_clickable((By.NAME, "q")))
        element.send_keys("123")
        element.submit()
        self.take_screenshot()
