from selenium.webdriver.common.by import By
class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class LocatorHomePage:
    CAR_RENTAL_MENU = Locator(By.XPATH, "//div[@id='navbar-offset']/div[2]/div/div[2]/div/div/a[6]/h4")
    WITHOUT_DRIVER_TAB = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-901oao:nth-child(2)")

class LocatorCarRentalPage:
    WITHOUT_DRIVER_RADIOBUTTON = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-901oao:nth-child(2)")
    WITH_DRIVER_RADIOBUTTON = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n:nth-child(2) > .css-1dbjc4n > .css-901oao:nth-child(2)")

    PICKUP_LOCATION_FIELD = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n > .css-11aywtz")
    PICKUP_TOP_RESULT = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n:nth-child(2) > .css-1dbjc4n:nth-child(1) > .css-4rbku5")
    PICKUP_TIME = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(4) > .css-1dbjc4n:nth-child(3) .css-11aywtz")
    PICKUP_TIME_HOURS = Locator(By.ID, "#")
    PICKUP_TIME_MINUTES = Locator(By.ID, "#")
    PICKUP_TIME_DONE = Locator(By.XPATH, "//div[@id='__next']/div[6]/div/div[2]/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div")

    SEARCH_CAR_BUTTON = Locator(By.CSS_SELECTOR, ".css-bfa6kz:nth-child(2)")
    CHANGE_SEARCH_CAR_BUTTON = Locator(By.CSS_SELECTOR, ".r-1o4mh9l:nth-child(2)")

    TOP_CONTINUE_CAR_BUTTON = Locator(By.XPATH, '//div[3]/div[3]/div/div[2]/div')
    TOP_CONTINUE_CAR_PROVIDER_BUTTON = Locator(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .css-1dbjc4n > .css-1dbjc4n:nth-child(3) > .css-4rbku5:nth-child(1)")
    CONTINUE_BUTTON = Locator(By.XPATH, "//div[@id='__next']/div/div[5]/div/div[4]/div/div[2]/div[2]/div/div[2]/div")

    PICKUP_RENTAL_OFFICE_RADIOBUTTON = Locator(By.XPATH, "//div[@id='RENTAL_PICKUP_LOCATION']/div/div/div[3]/div/div[2]/div/div/div[2]")
    PICKUP_RENTAL_OFFICE_FIELD = Locator(By.XPATH, "//div[@id='RENTAL_PICKUP_LOCATION']/div/div/div[3]/div[2]/div/div/div/div/div/div/div")
    PICKUP_RENTAL_OFFICE_TOP_RESULT = Locator(By.XPATH, "//div[@id='RENTAL_PICKUP_LOCATION']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[3]")
    PICKUP_OTHER_LOCATION_RADIOBUTTON = Locator(By.XPATH, "//div[@id='RENTAL_PICKUP_LOCATION']/div/div/div[5]/div/div[2]/div/div/div[2]")

    DROPOFF_RENTAL_OFFICE_RADIOBUTTON = Locator(By.XPATH, "//div[@id='RENTAL_DROPOFF_LOCATION']/div/div/div[3]/div/div[2]/div/div/div[2]")
    DROPOFF_OTHER_LOCATION_RADIOBUTTON = Locator(By.XPATH, "//div[@id='RENTAL_DROPOFF_LOCATION']/div/div/div[5]/div/div[2]/div/div/div[2]")
    DROPOFF_OTHER_LOCATION = Locator(By.XPATH, "")
    DROPOFF_OTHER_LOCATION_FIELD = Locator(By.XPATH, "//div[@id='RENTAL_DROPOFF_LOCATION']/div/div/div[5]/div[2]/div/div/div/div/div/input")
    DROPOFF_OTHER_LOCATION_TOP_RESULT = Locator(By.XPATH, "//div[@id='RENTAL_DROPOFF_LOCATION']/div/div/div[5]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div")

    NOTES_FIELD = Locator(By.CSS_SELECTOR, ".r-bcqeeo")
    BOOK_NOW_BUTTON = Locator(By.XPATH, "//div[@id='__next']/div/div[5]/div/div/div/div[5]/div[3]/div/div[2]/div")

class LocatorBookingPage:
    NAME_FIELD = Locator(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/input")
    NOHP_FIELD = Locator(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/input")
    EMAIL_FIELD = Locator(By.XPATH, "//div[@id='__next']/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/input")
    TITLE_DRIVER_FIELD = Locator(By.XPATH, "//div[3]/div/div/div/div/div/div/div[2]/div/div/div/select")
    NOHP_DRIVER_FIELD = Locator(By.XPATH, "//div[3]/div/div/div/div/div/div/div[2]/div[2]/div/div/input")
    EMAIL_DRIVER_FIELD = Locator(By.XPATH, "//div[3]/div/input")
    CONTINUE_BOOKING_BUTTON = Locator(By.XPATH, "//div[@id=\'__next\']/div[2]/div[2]/div/div[4]/div/div/div/div[2]")