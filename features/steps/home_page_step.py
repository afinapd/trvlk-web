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
    basePage.navigate("https://www.traveloka.com/en-id/car-rental/search?sd=15-2-2024&st=9-0&ed=17-2-2024&et=9-0&driverType=WITHOUT_DRIVER&city=Soekarno%20Hatta%20International%20Airport%20(CGK)&fromLocation=TVLK.100004409163.POI.AIRPORT.Airport.Soekarno%20Hatta%20International%20Airport%20(CGK).%27%27.-6x1255698%2B106x6559982")

@step('the user select the "{menu}" product')
def clickProductMenu(self, menu):
    homePage.click_menu_product(menu)
    carRentalPage.verify_car_rental_page_by_URL()
