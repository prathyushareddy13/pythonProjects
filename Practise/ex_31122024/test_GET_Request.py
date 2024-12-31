import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase is to check Booking and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "booking/2"
    full_url = base_url+base_path

    response_data_get = requests.get(url=full_url)
    res_data_json = response_data_get.json()
    print(res_data_json)

    assert res_data_json["firstname"] == "Mark"
    assert res_data_json["lastname"] == "Wilson"
    assert res_data_json["totalprice"] == 537
    assert res_data_json["bookingdates"]["checkin"] == "2018-03-04"
    assert response_data_get.status_code ==200
    assert response_data_get.elapsed.total_seconds() < 3
