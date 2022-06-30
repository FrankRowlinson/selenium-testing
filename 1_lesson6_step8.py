from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as browser:
    url = "http://suninjuly.github.io/find_xpath_form"
    browser.get(url)
    browser.find_element(By.TAG_NAME, "input").send_keys("Vlad")
    browser.find_element(By.NAME, "last_name").send_keys("Solomonov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Barnaul")
    browser.find_element(By.ID, "country").send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    sleep(30)