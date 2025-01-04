import pytest
import requests

from Practise.ex_02012025.conftest import create_bookingid


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
        "firstname": "Kranti",
        "lastname": "Kumar",
        "totalprice": 600,
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

#@pytest.fixture()
def test_delete_request():
    booking_id_deleted = create_booking()
    #print("Del request", booking_id_deleted)
    token = create_token()
    url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id_deleted)
    full_url_del = url + base_path
    cookie = "token=" + token
    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    response_delete = requests.delete(url = full_url_del, headers=header)
    print(response_delete.text)    #coming as Created instead of Forbidden
    assert response_delete.status_code == 201
    print(booking_id_deleted)
    return booking_id_deleted

def test_update_deleted_request():
    booking_id = create_booking()
    print(booking_id)
    token = create_token()
    url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" +str(booking_id)
    full_url_patch = url + base_path
    cookie = "token="+token
    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    json_payload = {
        "firstname": "Pavan",
        "lastname": "Kumar",
        "totalprice": 600,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=full_url_patch, headers=header, json=json_payload)
    print(response.text)
    assert response.status_code == 405    #403 Forbidden