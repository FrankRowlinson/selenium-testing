# -----------robo-capctha with alerts-------------

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import robo_captcha as rc


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    # click button and then accept alert
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.alert.accept()
    sleep(1)
    # solve robo-captcha and submit
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(rc.calc(x))
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(10)
    