import pytest
import allure


@allure.title("This is request to get the details")
@pytest.mark.positive
def test_create_booking():
 print("This is a test")
 assert 5==5

@allure.title("This is request to get the Booking details")
@pytest.mark.negative
def test_create_booking_neg():
 print("This is a negative test case")
 assert 6==8

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0
