from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorHomePage

class HomePage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_menu_product(self, menu):
        if menu == "Car Rental":
            super().perform_action_on_element(LocatorHomePage.CAR_RENTAL_MENU, "click")
        super().wait_for_page_load()

homePage = HomePage.get_instance()
