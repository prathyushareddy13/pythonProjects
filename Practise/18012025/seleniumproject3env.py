from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from dotenv import load_dotenv
import os

def test_fill_form():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL"))
    time.sleep(10)
    #<input type="text" name="firstname" value="" placeholder="First Name" id="input-firstname" class="form-control">
    firstname = driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    firstname.send_keys(os.getenv("Firstname"))
    lastname = driver.find_element(By.XPATH,"//input[@id='input-lastname']")
    lastname.send_keys(os.getenv("Lastname"))
    email_id = driver.find_element(By.NAME,"email")
    email_id.send_keys("prathyusha5.reddy13@gmail.com") #need to change the email id everytime before running
    telephone = driver.find_element(By.ID, "input-telephone")
    telephone.send_keys(os.getenv("Telephone"))
    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys(os.getenv("Password"))
    confirm_password = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    confirm_password.send_keys(os.getenv("ConfirmPassword"))
    checkbox = driver.find_element(By.NAME,"agree")
    checkbox.click()
    #<input type="submit" value="Continue" class="btn btn-primary">
    #continue_button = driver.find_element(By.CLASS_NAME,"btn btn-primary")
    continue_button = driver.find_element(By.XPATH, "//input[@class='btn btn-primary']")
    continue_button.click()
    creation = driver.find_element(By.XPATH,"//h1[contains(text(),'Your Account Has')]")
    assert creation.text == os.getenv("assertion_text")
    #print("Account has been created!")
    time.sleep(5)
    driver.quit()