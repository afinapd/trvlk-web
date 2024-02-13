Feature: Car Rental Booking

  Scenario: Book a Car Rental with Customized Options
    Given launch chrome browser
    When user access traveloka page
    And the user select the "Car Rental" product
    And choose the "Without Driver" radio button
    And set the pick-up location to "Jakarta"
    And set the pick-up date and time to today 2d 09:00
    And set the drop-off date and time to today 5d 11:00
    And click the Search Car button
    And select a car
    And select a car provider
    And click the Continue button in the product detail section
    And select the pick-up location as "Rental Office"
    And choose the drop-off location as "Jakarta"
    And input optional pick-up/drop-off notes "dekat klender"
    And clicks the Book Now button
    And fills in contact details name "Afina", no hp "85771610000", and email "fina@gmail.com"
    And provides driver details title "Mr.", name "fina driver", and nohp "85771610001"
    And clicks Continue
#    And adds an optional special request
#    And checks all rental requirements
#    And clicks "Continue"
#    And selects a payment method and proceeds to payment
#    Then the booking process should be successfully completed
#    And the user should receive a confirmation of the booked car rental.
