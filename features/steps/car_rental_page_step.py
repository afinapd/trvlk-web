from behave import *

from features.pages.car_rental_page import carRentalPage


@step('choose the "{radioButton}" radio button')
def chooseDriver(self, radioButton):
    carRentalPage.click_tab_driver(radioButton)

@step('set the pick-up location to "{location}"')
def setPickupLocation(self, location):
    carRentalPage.input_pickup_location(location)

@step('set the pick-up date and time to today 2d 09:00')
def setPickupLocation(self):
    carRentalPage.input_pickup_date()
    carRentalPage.input_pickup_time()

@step('set the drop-off date and time to today 5d 11:00')
def setDropoffLocation(self):
    carRentalPage.input_dropoff_date()
    carRentalPage.input_dropoff_time()

@step('click the Search Car button')
def clickSearchCarButton(self):
    carRentalPage.click_button_search_car()

@step('select a car')
def selectCar(self):
    carRentalPage.select_car()

@step('select a car provider')
def selectCarProvider(self):
    carRentalPage.select_car_provider()

@step('click the Continue button in the product detail section')
def clickContinueButton(self):
    carRentalPage.click_button_continue()

@step('select the pick-up location as "{location}"')
def selectPickupLocation(self, location):
    carRentalPage.input_pickup_car_location(location)

@step('choose the drop-off location as "{location}"')
def selectDropoffLocation(self, location):
    carRentalPage.input_dropoff_car_location(location)

@step('input optional pick-up/drop-off notes "{notes}"')
def inputNotes(self, notes):
    carRentalPage.input_notes(notes)

@step('clicks the Book Now button')
def clickBookNowButton(self):
    carRentalPage.click_button_book_now()
