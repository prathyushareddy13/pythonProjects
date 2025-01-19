from numpy.ma.core import equal
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
    #<div class="s-item__info clearfix"><!--F#f_21--><div class="s-item__caption"></div><!--F#f_11--><a data-interactions="[{&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;interaction&quot;:&quot;wwFVrK2vRE0lhQQ0MDFKSFdIWDVFMkY0QjBZOTlFUDdTVlRFS0U0MDFKSFdIWDU5WFNROTFTR1BaNjBTNDNZMUsAAAg3NDAwDE5BVlNSQwA=&quot;}]" target="_blank" _sp="p2351460.m1686.l7400" data-s-szex436="{&quot;eventFamily&quot;:&quot;LST&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;NAVSRC&quot;,&quot;actionKinds&quot;:[&quot;NAVSRC&quot;],&quot;operationId&quot;:&quot;2351460&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;$l&quot;:&quot;420904986203242&quot;}}" class="s-item__link" href="https://www.ebay.com/itm/155930614304?_skw=macmini&amp;itmmeta=01JHWHX59XSQ91SGPZ60S43Y1K&amp;hash=item244e305a20:g:AYUAAOSw6shlgd6A&amp;itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKkXmeUILrDQqIbpCD%2B58nShoFyl5FpjFAGcffSgrLiTOm%2FPLHU1rgF7rrqOKvmwZ7MKF9J5gNHXAPPE3lk83OMNvtR0yKndeh%2FOTN8%2FH1L3vzK91TIa%2BJ4Art6Xf6cbMFxzmRBvbs2YB6O0B7NGXtJfqNuqB8X9iSvIg8Euqqy%2B3W6Y6cTdAU0HTu8R5sPk3FoAiGhYrdQXfcBiiTShQZTsrcWqFX9Vh1m5go2%2Fs%2FbhiJoae1q2%2BXyDiQ4TJqn3O5254CI8p8jXLiNOctHdht9r%7Ctkp%3ABk9SR4TW9JGPZQ"><div class="s-item__title"><span role="heading" aria-level="3"><!--F#f_0-->Apple Mac Mini M1 Chip 8CGPU Late 2020 512GB SSD 8GB RAM Silver - Very Good<!--F/--></span></div><span class="clipped">Opens in a new window or tab</span></a><!--F/--><div class="s-item__subtitle"><!--F#f_0--><span class="SECONDARY_INFO">Very Good - Refurbished</span><!--F/--></div><!--F/--><div class="s-item__details clearfix"><div class="s-item__details-section--primary"><div class="s-item__detail s-item__detail--primary"><span class="s-item__price"><!--F#f_0--><!--F#f_0-->$375.99<!--F/--><!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__dynamic s-item__formatBuyItNow"><!--F#f_0-->Buy It Now<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__shipping s-item__logisticsCost"><!--F#f_0-->+$65.03 delivery<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__location s-item__itemLocation"><!--F#f_0-->from United States<!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__hotness s-item__authorized-seller" aria-label="eBay Refurbished" role="text"><svg data-marko-key="@svg s0-62-0-13-8-4-3-0-3-0-4[9]-10-1-33[0[4[0]]]-1-8-1-0" class="icon icon--48-colored" focusable="false" aria-hidden="true"><use href="#icon-legacy-authenticity-guarantee-48-colored"></use></svg><!--F#f_0--><span class="BOLD">eBay Refurbished</span><!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span class="s-item__dynamic s-item__watchCountTotal"><!--F#f_0--><span class="BOLD">126 watchers</span><!--F/--></span></div><div class="s-item__detail s-item__detail--primary"><span><span aria-labelledby="s-sfmy432" data-w="Sporndeso" class="s-sfmy432_s-bftt630" role="text"><div aria-hidden="true">Sponsored</div></span></span><span class="s-item__space_bar"></span></div></div><div class="s-item__details-section--center"></div><div class="s-item__details-section--secondary"><span class="s-item__detail s-item__detail--secondary"><span class="s-item__etrs"><span class="s-item__etrs-badge clipped">Top Rated Seller</span><svg data-marko-key="@svg s0-62-0-13-8-4-3-0-3-0-4[9]-10-1-33[0[0[2]]]-1-23-2-0" class="icon icon--48-colored" focusable="false" aria-hidden="true"><use href="#icon-legacy-top-rated-seller-48-colored"></use></svg><span class="s-item__etrs-text"><!--F#f_0-->Top Rated Seller<!--F/--></span></span></span><span class="s-item__detail s-item__detail--secondary"><span class="s-item__seller-info"><span class="s-item__seller-info-text">cellularprofessor (18,554) 99%</span></span></span></div></div></div>
    webpage_info = driver.find_elements(By.CLASS_NAME, "s-item__info")
    elements = driver.find_elements_by_xpath("//div[@class='my-class']")
    webpage_info1 = driver.find_elements(By.CLASS_NAME, "s-item__info")
    text = [title.text for title in webpage_info]
    #string_text = str(text)
    #split_text = text.split("\n")
    for info in text:
        if info != '' :
            temp = info.split("\n")
            print(temp[0],",",temp[3])
    print("hello")




    time.sleep(10)

