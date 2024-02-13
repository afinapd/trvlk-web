from behave import *

from features.core.base_page import basePage
from features.pages.car_rental_page import carRentalPage
from features.pages.home_page import homePage


@given('launch chrome browser')
def lauchBrowser(self):
    basePage.get_driver()

@step('close browser')
def closeBrowser(self):
    basePage.close_browser()

@step('user access traveloka page')
def accessTravelokaPage(self):
    basePage.navigate("https://www.traveloka.com/en-id")

@step('the user select the "{menu}" product')
def clickProductMenu(self, menu):
    homePage.click_menu_product(menu)
    carRentalPage.verify_car_rental_page_by_URL()
