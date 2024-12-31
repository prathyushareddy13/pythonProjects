import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com/"
header =  {"Content-Type": "application/json"}
def get_booking_id():
    base_path = "booking/"
    full_url = base_url + base_path
    json = {
        "firstname": "Siddhant",
        "lastname": "Reddy",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2019-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=header, json = json)
    res_data_json = response_data.json()
    bookingid = res_data_json["bookingid"]
    return bookingid
    

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase is to check Booking and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    booking_id = get_booking_id()
    print(booking_id)

    assert booking_id is not None
    assert type(booking_id) == int
    assert booking_id > 0



