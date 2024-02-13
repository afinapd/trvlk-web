from behave import *

from features.pages.booking_page import bookingPage

@step('fills in contact details name "{name}", no hp "{nohp}", and email "{email}"')
def inputContactsDetails(self, name, nohp, email):
    bookingPage.input_name(name)
    bookingPage.input_nohp(nohp)
    bookingPage.input_email(email)

@step('provides driver details title "{title}", name "{name}", and nohp "{nohp}"')
def inputDriverDetails(self, title, name, nohp):
    bookingPage.input_title_driver(title)
    bookingPage.input_name_driver(name)
    bookingPage.input_nohp_driver(nohp)

@step('clicks Continue')
def clicContinueButton(self):
    bookingPage.click_continue_button()
