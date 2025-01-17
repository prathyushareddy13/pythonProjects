from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import pytest
import time

@allure.title("Positive Testcase1")
@allure.description("Clicking on the login button to check the functionality")
def test_espo_login_click():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    #<button type="submit" class="btn btn-primary btn-s-wide" id="btn-login">Login</button>
    login_button_webelement = driver.find_element(By.ID,"btn-login")
    #login_button_webelement = driver.find_element(By.XPATH,"//button[@id='btn-login']")
    login_button_webelement.click()
    time.sleep(3)

def test_click_advanced_pack():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    #<a href="https://www.espocrm.com/extensions/advanced-pack/" target="_blank">Advanced Pack</a>
    pack_webelement = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/advanced-pack/']")
    pack_webelement.click()
    time.sleep(3)

def test_click_sales_pack_():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    #<a href="https://www.espocrm.com/extensions/sales-pack/" target="_blank">Sales Pack</a>
    sales_webelement = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/sales-pack/']")
    sales_webelement.click()
    time.sleep(3)

def test_click_personal_demo():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    #<a href="https://www.espocrm.com/cloud-registration/?plan=demo">personal demo</a>
    personal_demo = driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")
    personal_demo.click()
    time.sleep(5)