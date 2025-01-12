
from time import sleep

import pytest
import allure
from selenium import webdriver

@allure.title("Selenium Testcase")
@allure.description("Testcase to open the webpage and verify URL and Title")
def test_open_webpage():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    sleep(10)
    print(driver.title)
    assert driver.current_url == "https://demo.us.espocrm.com/"
    assert driver.title == "EspoCRM Demo"

def test_open_in_edge():
    driver = webdriver.Edge()
    driver.get("https://demo.us.espocrm.com/")
    sleep(10)
    print(driver.title)
    assert driver.current_url == "https://demo.us.espocrm.com/"
    assert driver.title == "EspoCRM Demo"