# -----------multiple window robo-captcha------------

from selenium import webdriver
from selenium.webdriver.common.by import By

import robo_captcha as rc
from time import sleep


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    # click on floating button and switch to a new window
    browser.find_element(By.CLASS_NAME, "trollface").click()
    new_window = browser.window_handles[1]
    browser._switch_to.window(new_window)
    # solve robo-captcha and submit
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(rc.calc(x))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(10)