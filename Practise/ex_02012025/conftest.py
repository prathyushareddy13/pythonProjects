import pytest
import requests

@pytest.fixture()
def create_token():
    base_url = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    json_token = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=base_url,headers=header,json=json_token)
    token = response_data.json()["token"]
    print(token)
    return token

@pytest.fixture()
def create_bookingid():
    full_url = "https://restful-booker.herokuapp.com/booking/"
    header = {"Content-Type": "application/json"}
    json = {
        "firstname": "Rakesh",
        "lastname": "Reddy",
        "totalprice": 723,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Lunch"
    }
    response_create = requests.post(url=full_url,headers=header,json=json)
    response_json = response_create.json()
    booking_id = response_json["bookingid"]
    firstname = response_json["booking"]["firstname"]
    lastname = response_json["booking"]["lastname"]
    print(booking_id)
    print(firstname)
    return booking_id


@pytest.fixture()
def patch_request(create_bookingid,create_token):
    url = "https://restful-booker.herokuapp.com/booking/"
    book_id = create_bookingid
    full_url = url + str(book_id)
    cookie = "token=" + create_token

    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Mehak",
        "lastname": "Reddy",
        "totalprice": 723,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(url=full_url, headers=header, json=json_payload)
    #response_json= response.json()
    #firstname = response_json["booking"]["firstname"]  it is not working in patch request
    firstname = response.json()["firstname"]
    print(firstname)
    return firstname

@pytest.fixture()
def delete_request(create_bookingid,create_token):
    url = "https://restful-booker.herokuapp.com/booking/"
    book_id = create_bookingid
    full_url = url + str(book_id)
    cookie = "token=" + create_token

    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    response_del = requests.delete(url = full_url,headers=header)
    status = response_del.status_code
    return status