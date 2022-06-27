from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Answer placeholder")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    sleep(30)