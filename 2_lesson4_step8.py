# -------wait until price is right-challenge----------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import robo_captcha as rc


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    # wait until price is $100 and then book the hotel
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    # solve robo-captcha and submit result
    x = int(browser.find_element(By.ID, "input_value").text)
    field = browser.find_element(By.ID, "answer")
    field.send_keys(rc.calc(x))
    browser.find_element(By.ID, "solve").click()
    sleep(10)