import pytest
import allure
import requests



@allure.title("#TC1 - This is a request to create a booking:")
@allure.description("Creating a booking by passing arguments")
@pytest.mark.smoke
def test_createbooking_positive():
    url_post = "https://restful-booker.herokuapp.com/"
    path_url = "booking"
    full_url = url_post+path_url
    post_header = {
        "Content-Type":"application/json"
    }
    json = {
        "firstname": "Prathyusha",
        "lastname": "Reddy",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url,headers=post_header,json=json)
    print(response_data.text)

    response_jsondata = response_data.json()
    bookingid = response_jsondata["bookingid"]
    print(bookingid)

    assert response_data.status_code == 200
    assert bookingid is not None
    assert bookingid is not str
    #assert type(bookingid) == int
    assert bookingid > 0

    #assert response_jsondata["booking"]["firstname"] == "Prathyusha"
    firstname = response_jsondata["booking"]["firstname"]
    assert firstname == "Prathyusha"
    assert type(firstname) == str
    assert firstname is not None

    lastname = response_jsondata["booking"]["lastname"]
    assert lastname == "Reddy"
    assert type(lastname) == str
    assert lastname is not None

    checkin = response_jsondata["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"

