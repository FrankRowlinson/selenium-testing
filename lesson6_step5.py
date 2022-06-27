from selenium import webdriver
from selenium.webdriver.common.by import By
from math import ceil, pi, e, pow
from time import sleep


formula = str(ceil(pow(pi, e)*10000))
# context manager to safely work with webdriver
with webdriver.Chrome() as browser:
    url = "http://suninjuly.github.io/find_link_text"
    browser.get(url)
    link = browser.find_element(By.LINK_TEXT, formula)
    link.click()
    # code from previous step
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    sleep(30)