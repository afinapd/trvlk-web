from selenium.webdriver.common.by import By

from features.core.reusable_page import ReusablePage
from features.locators.locator import LocatorCarRentalPage

class CarRentalPage(ReusablePage):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CarRentalPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def verify_car_rental_page_by_URL(self):
        super().verify_url("https://www.traveloka.com/en-id/car-rental")

    def click_tab_driver(self, radioButton):
        if radioButton == "Without Driver":
            super().perform_action_on_element(LocatorCarRentalPage.WITHOUT_DRIVER_RADIOBUTTON, "click")
        elif radioButton == "With Driver":
            super().perform_action_on_element(LocatorCarRentalPage.WITH_DRIVER_RADIOBUTTON, "click")
        super().wait_for_page_load()

    def input_pickup_location(self, location):
        super().perform_action_on_element(LocatorCarRentalPage.PICKUP_LOCATION_FIELD, "type", location)
        super().wait_for_page_load()
        super().perform_action_on_element(LocatorCarRentalPage.PICKUP_TOP_RESULT, "click")

    def input_pickup_date(self):
        print("==== TBD: input_pickup_date")

    def input_pickup_time(self):
        print("==== TBD: input_pickup_time")

    def input_dropoff_date(self):
        print("==== TBD: input_pickup_date")

    def input_dropoff_time(self):
        print("==== TBD: input_pickup_time")

    def click_button_search_car(self):
        super().perform_action_on_element(LocatorCarRentalPage.SEARCH_CAR_BUTTON, "click")
        super().perform_action_on_element(LocatorCarRentalPage.CHANGE_SEARCH_CAR_BUTTON, "present")

    def select_car(self):
        super().perform_action_on_element(LocatorCarRentalPage.TOP_CONTINUE_CAR_BUTTON, "click")

    def select_car_provider(self):
        super().perform_action_on_element(LocatorCarRentalPage.TOP_CONTINUE_CAR_PROVIDER_BUTTON, "click")

    def click_button_continue(self):
        super().perform_action_on_element(LocatorCarRentalPage.CONTINUE_BUTTON, "click")
        super().wait_for_page_load()

    def input_pickup_car_location(self, location):
        if location == "Rental Office":
            super().perform_action_on_element(LocatorCarRentalPage.PICKUP_RENTAL_OFFICE_RADIOBUTTON, "click")
            super().perform_action_on_element(LocatorCarRentalPage.PICKUP_RENTAL_OFFICE_FIELD, "click")
            super().perform_action_on_element(LocatorCarRentalPage.PICKUP_RENTAL_OFFICE_TOP_RESULT, "click")
        elif location == "Other Location":
            super().perform_action_on_element(LocatorCarRentalPage.PICKUP_OTHER_LOCATION_RADIOBUTTON, "click")
            print("==== TBD: Other Location")
        super().wait_for_page_load()

    def input_dropoff_car_location(self, location):
        if location == "Rental Office":
            super().perform_action_on_element(LocatorCarRentalPage.DROPOFF_RENTAL_OFFICE_RADIOBUTTON, "click")
            print("==== TBD: Rental Office")
        elif location == "Other Location":
            super().perform_action_on_element(LocatorCarRentalPage.DROPOFF_OTHER_LOCATION_RADIOBUTTON, "click")
            super().perform_action_on_element(LocatorCarRentalPage.DROPOFF_OTHER_LOCATION_FIELD, "type", location)
            super().wait_for_page_load()
            super().perform_action_on_element(LocatorCarRentalPage.DROPOFF_OTHER_LOCATION_TOP_RESULT, "click")
        super().wait_for_page_load()

carRentalPage = CarRentalPage.get_instance()
