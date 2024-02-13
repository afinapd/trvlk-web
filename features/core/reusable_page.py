import time
import re

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from helper.config import config
from features.core.base_page import basePage
from selenium.webdriver.support.select import Select

class ReusablePage:
    def __init__(self):
        self.driver = basePage.get_driver()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, config.driver_timeout).until(condition)

    def wait_for_element(self, locator):
        self._execute_with_wait(ec.element_to_be_clickable(locator.l_type, locator.selector))

    def wait_for_items_to_load(self):
        try:
            if (self.driver.find_element("xpath", "//span[text()='Loading menu items...']").is_displayed()) == True:
                time.sleep(30)
        except:
            print("All items loaded")

    def count_all_elements(self, locator):
        return len(self.driver.find_elements(locator.l_type, locator.selector))

    def element_exists(self, locator):
        try:
            time.sleep(1)
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def assert_element_text(self, locator, text):
        web_element = self.driver.find_element(locator.l_type, locator.selector)
        assert web_element.text == text

    def assert_element_contain_text(self, text):
        web_element = self.driver.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")

    def get_element(self, locator, text=""):
        if "ObjectToken" in locator.selector:
            locator.selector = locator.selector.replace("ObjectToken", RunTimeValue)
        if not self.element_exists(locator):
            print(locator)
            raise NoSuchElementException("Could not find ->" + locator.selector)
        return self.driver.find_element(locator.l_type, locator.selector)

    def get_element_text(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException("Could not find {locators.selector}")
        return self.driver.find_element(locator.l_type, locator.selector).text

    def get_dynamic_text_from_element(self, locator, text):
        global RunTimeValue
        RunTimeValue = text
        dynamic_text = self.get_element(locator, text).text
        locator.selector = re.sub(r"'[A-Z _/a-z]+'", "'ObjectToken'", locator.selector)
        return dynamic_text

    def wait_for_page_load(self):
        # print("Checking if {} page is loaded.".format(self.driver.current_url))
        time.sleep(5)
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def verify_url(self, url):
        time.sleep(5)
        get_current_url = self.driver.current_url
        assert get_current_url == url

    def enter_text_in_dynamic_field(self, locator, text_to_locate_element, text_to_enter):
        global RunTimeValue
        RunTimeValue = text_to_locate_element
        self.get_element(locator).send_keys(text_to_enter)
        locator.selector = re.sub(r"'[A-Z _/a-z]+'", "'ObjectToken'", locator.selector)

    def multi_select_for_dynamic_element(self, main_element, option_to_select):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[text()='"+main_element+"']/following-sibling::div//li//span[contains(text(),'"+option_to_select+"')]")).click().perform()

    def perform_action_on_element(self, locator: str, action: str, text=""):
        try:
            global RunTimeValue
            flag = False
            RunTimeValue = text
            action = action.lower()
            if "ObjectToken" in locator.selector:
                flag = True
            if action == "click":
                self.get_element(locator).click()
            elif action == "type":
                self.get_element(locator).send_keys(text)
            elif action == "select":
                select = Select(self.get_element(locator))
                select.select_by_visible_text(text)
            elif action == "clear":
                self.get_element(locator).clear()
            elif action == "enter":
                self.get_element(locator).send_keys(Keys.ENTER)
            elif action == "clickwithactionclass":
                ActionChains(self.driver).move_to_element(self.get_element(locator)).click().perform()
            elif action == "scroll":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", self.get_element(locator))
                time.sleep(5)
            elif action == "scroll_into_middle":
                view_port_height = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
                element_top = "var elementTop = arguments[0].getBoundingClientRect().top;"
                js_function = "window.scrollBy(0, elementTop-(viewPortHeight/2));"
                scroll_into_middle = view_port_height + element_top + js_function
                self.driver.execute_script(scroll_into_middle, self.get_element(locator))
            elif action == "present":
                time.sleep(5)
                try:
                    assert self.get_element(locator).is_displayed()
                except:
                    print(text + " -> Element is not displayed on the page")
                    assert False, text + " Element is not displayed on the page"
            elif action == "not_present":
                if self.count_all_elements(locator)==0:
                    assert True, "User does not has access"
            else:
                raise NoSuchActionExist(action)
            if flag:
                locator.selector = re.sub(r"'[A-Z _/a-z]+'", "'ObjectToken'", locator.selector)
        except:
            print(action + "on " +str(locator.selector) +" is not working")
            assert False, action +" on " +str(locator.s) +" is failing"


reusablePage = ReusablePage()