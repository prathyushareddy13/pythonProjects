import pytest
import requests

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

def create_booking():
    full_url = "https://restful-booker.herokuapp.com/booking/"
    header = {"Content-Type": "application/json"}
    json = {
        "firstname": "Mohan",
        "lastname": "Kumar",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response_create = requests.post(url=full_url, headers=header, json=json)
    response_json = response_create.json()
    booking_id = response_json["bookingid"]
    firstname = response_json["booking"]["firstname"]
    lastname = response_json["booking"]["lastname"]
    print(booking_id)
    return booking_id

def test_delete_request():
    booking_id = create_booking()
    token = create_token()
    url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    full_url_del = url + base_path
    cookie = "token=" + token
    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    response_delete = requests.delete(url = full_url_del, headers=header)
    assert response_delete.status_code == 201