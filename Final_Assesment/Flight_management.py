from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure WebDriver (adjust the path to your WebDriver executable)
driver = webdriver.Chrome() 
# Open the Flight Management System page

driver.get("http://localhost:8000")


def test_flight_search_service():
    # Test Case 1.1: Valid Flight Search
    driver.find_element(By.ID, "departure").send_keys("New York")
    driver.find_element(By.ID, "arrival").send_keys("Los Angeles")
    driver.find_element(By.ID, "date").send_keys("2024-12-01")
    driver.find_element(By.ID, "searchForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Flight1, Flight2" in driver.find_element(By.ID, "searchResults").text

    # Test Case 1.2: Invalid Flight Search
    driver.find_element(By.ID, "departure").clear()
    driver.find_element(By.ID, "arrival").clear()
    driver.find_element(By.ID, "date").clear()
    driver.find_element(By.ID, "departure").send_keys("InvalidCity")
    driver.find_element(By.ID, "arrival").send_keys("InvalidCity")
    driver.find_element(By.ID, "date").send_keys("2024-12-01")
    driver.find_element(By.ID, "searchForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "No flights available" in driver.find_element(By.ID, "searchResults").text

    # Test Case 1.3: Empty Search Fields
    driver.find_element(By.ID, "departure").clear()
    driver.find_element(By.ID, "arrival").clear()
    driver.find_element(By.ID, "date").clear()
    driver.find_element(By.ID, "searchForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Please enter valid search criteria." in driver.find_element(By.ID, "searchResults").text

def test_flight_booking_service():
    # Test Case 2.1: Valid Flight Booking
    driver.find_element(By.ID, "flight").send_keys("Flight1")
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "passport").send_keys("A1234567")
    driver.find_element(By.ID, "card").send_keys("4111111111111111")
    driver.find_element(By.ID, "expiry").send_keys("2024-12")
    driver.find_element(By.ID, "cvv").send_keys("123")
    driver.find_element(By.ID, "bookingForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Booking confirmed" in driver.find_element(By.ID, "bookingResult").text

    # Test Case 2.2: Booking with Incomplete Passenger Details
    driver.find_element(By.ID, "flight").clear()
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "age").clear()
    driver.find_element(By.ID, "passport").clear()
    driver.find_element(By.ID, "card").clear()
    driver.find_element(By.ID, "expiry").clear()
    driver.find_element(By.ID, "cvv").clear()
    driver.find_element(By.ID, "flight").send_keys("Flight1")
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "bookingForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Please complete all required fields." in driver.find_element(By.ID, "bookingResult").text

    # Test Case 2.3: Invalid Payment Details
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "passport").send_keys("A1234567")
    driver.find_element(By.ID, "card").send_keys("0000000000000000")
    driver.find_element(By.ID, "expiry").send_keys("2024-12")
    driver.find_element(By.ID, "cvv").send_keys("123")
    driver.find_element(By.ID, "bookingForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Payment failed" in driver.find_element(By.ID, "bookingResult").text

def test_flight_schedule_service():
    # Test Case 3.1: View Flight Schedule
    driver.find_element(By.ID, "flightNumber").send_keys("Flight1")
    driver.find_element(By.ID, "scheduleForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "10:00 AM" in driver.find_element(By.ID, "scheduleResult").text

    # Test Case 3.2: View Non-existent Flight Schedule
    driver.find_element(By.ID, "flightNumber").clear()
    driver.find_element(By.ID, "flightNumber").send_keys("InvalidFlight")
    driver.find_element(By.ID, "scheduleForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Invalid flight number" in driver.find_element(By.ID, "scheduleResult").text

def test_flight_cancel_service():
    # Test Case 4.1: Valid Flight Cancellation
    driver.find_element(By.ID, "bookingReference").send_keys("ABC123")
    driver.find_element(By.ID, "cancelForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Flight canceled" in driver.find_element(By.ID, "cancelResult").text

    # Test Case 4.2: Cancel Flight with Invalid Booking Reference
    driver.find_element(By.ID, "bookingReference").clear()
    driver.find_element(By.ID, "bookingReference").send_keys("InvalidReference")
    driver.find_element(By.ID, "cancelForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Invalid booking reference" in driver.find_element(By.ID, "cancelResult").text

    # Test Case 4.3: Cancel Flight Close to Departure Time
    driver.find_element(By.ID, "bookingReference").clear()
    driver.find_element(By.ID, "bookingReference").send_keys("ABC123")
    driver.find_element(By.ID, "cancelForm").find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "Cannot cancel the flight as it is too close to the departure time." in driver.find_element(By.ID, "cancelResult").text

# Run the test cases
test_flight_search_service()
test_flight_booking_service()
test_flight_schedule_service()
test_flight_cancel_service()

# Close the browser
driver.quit()
