from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure


def test_fill_form():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(10)
    #<input type="text" name="firstname" value="" placeholder="First Name" id="input-firstname" class="form-control">
    firstname = driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    firstname.send_keys("Prathyusha")
    lastname = driver.find_element(By.XPATH,"//input[@id='input-lastname']")
    lastname.send_keys("Reddy")
    email_id = driver.find_element(By.NAME,"email")
    email_id.send_keys("prathyusha3.reddy13@gmail.com")
    telephone = driver.find_element(By.ID, "input-telephone")
    telephone.send_keys("3787375845")
    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("awesomeqa")
    confirm_password = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    confirm_password.send_keys("awesomeqa")
    checkbox = driver.find_element(By.NAME,"agree")
    checkbox.click()
    #<input type="submit" value="Continue" class="btn btn-primary">
    #continue_button = driver.find_element(By.CLASS_NAME,"btn btn-primary")
    continue_button = driver.find_element(By.XPATH, "//input[@class='btn btn-primary']")
    continue_button.click()
    creation = driver.find_element(By.XPATH,"//h1[contains(text(),'Your Account Has')]")
    assert creation.text == "Your Account Has Been Created!"
    #print("Account has been created!")
    time.sleep(5)