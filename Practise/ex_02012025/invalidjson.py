import requests
import pytest

def test_createbooking_negative():
    url_post = "https://restful-booker.herokuapp.com/"
    path_url = "booking"
    full_url = url_post+path_url
    post_header = {
        "Content-Type":"application/json"
    }
    json = {
    }
    response_data = requests.post(url=full_url,headers=post_header,json=json)
    json_data = response_data.json()
    print(response_data.text)

    assert json_data is not None
    assert response_data.status_code == 500
    #assert response_data is not None

