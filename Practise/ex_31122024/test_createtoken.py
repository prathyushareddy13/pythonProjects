import pytest
import allure
import requests

from Practise.ex_31122024.test_GETID_Request import base_url, header


def test_createtoken():
    base_path = "/auth"
    full_url = base_url+base_path

    json_token = {
       "username": "admin",
       "password": "password123"
    }

    response_data = requests.post(url = full_url, headers= header,json = json_token)
    response_json = response_data.json()
    token = response_json["token"]
    print(token)

    assert len(token) > 10
    assert response_data.status_code == 200
    assert type(token) == str