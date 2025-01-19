from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

def test_mac_mini():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(5)
    search_element = driver.find_element(By.ID,"gh-ac")
    search_element.send_keys("macmini")
    #<span class="gh-search-button__label">Search</span>
    search_button = driver.find_element(By.CLASS_NAME, "gh-search-button__label")
    search_button.click()
    titles = driver.find_elements(By.CLASS_NAME, "s-item__title")
    prices = driver.find_elements(By.CLASS_NAME,"s-item__price")
    title_texts = [title.text for title in titles]
    price_texts = [price.text for price in prices]  #to convert web element to list
    for text,price in zip(title_texts,price_texts): #to combine two lists
        #for price in price_texts:
        print(text,price)

    time.sleep(10)
    driver.quit()

