import os
import shutil
import time

from helper.config import config
import datetime
from selenium import webdriver

class BasePage(object):
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BasePage()
        return cls.instance

    def __init__(self):
        if config.browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(config.driver_timeout)
        else:
            raise BasePage.SeleniumDriverNotFound(
                {config.browser} +" is not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()

    def close_browser(self):
        self.driver.close()
        time.sleep(5)

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)
        time.sleep(15)


basePage = BasePage.get_instance()