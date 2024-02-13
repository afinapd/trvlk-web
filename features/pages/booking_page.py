from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorBookingPage

class BookingPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BookingPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def input_name(self, name):
        super().perform_action_on_element(LocatorBookingPage.NAME_FIELD, "type", name)

    def input_nohp(self, nohp):
        super().perform_action_on_element(LocatorBookingPage.NOHP_FIELD, "type", nohp)

    def input_email(self, email):
        super().perform_action_on_element(LocatorBookingPage.EMAIL_FIELD, "type", email)

    def input_title_driver(self, title):
        super().perform_action_on_element(LocatorBookingPage.TITLE_DRIVER_FIELD, "dropdown", title)

    def input_name_driver(self, name):
        super().perform_action_on_element(LocatorBookingPage.NOHP_DRIVER_FIELD, "type", name)

    def input_nohp_driver(self, nohp):
        super().perform_action_on_element(LocatorBookingPage.EMAIL_DRIVER_FIELD, "type", nohp)

    def click_continue_button(self):
        super().perform_action_on_element(LocatorBookingPage.CONTINUE_BOOKING_BUTTON, "click")

bookingPage = BookingPage.get_instance()
