import pytest
import allure
import requests

def test_get_all_bookings():
    url = "https://restful-booker.herokuapp.com/booking"
    response_all = requests.get(url=url)
    response_json = response_all.json()
    print(response_json)


def test_update_booking(create_token):
    url = "https://restful-booker.herokuapp.com/booking/"
    up_booking_id = str(500)
    full_url = url+up_booking_id
    print(full_url)
    cookie = "token=" + create_token
    header = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    up_payload = {
        "firstname": "Prat",
        "lastname": "Smith",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response_update = requests.put(url = full_url, headers=header,json=up_payload)
    firstname = response_update.json()["firstname"]
    #print(firstname)
    assert firstname == "Prat"

def test_get_request():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "booking/500"
    full_url = base_url+base_path

    response_data_get = requests.get(url=full_url)
    print(response_data_get.text)
    response_jsondata = response_data_get.json()
    
    firstname = response_jsondata["firstname"]
    assert firstname == "Prat"
    assert type(firstname) == str
    assert firstname is not None

    bookingdate = response_jsondata["bookingdates"]["checkin"]
    print(bookingdate)

    assert response_jsondata["lastname"] == "Smith"
    assert response_jsondata["totalprice"] == 111
    assert bookingdate == "2018-01-01"
    assert response_data_get.status_code == 200
    assert response_data_get.elapsed.total_seconds() < 5

