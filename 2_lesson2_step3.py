# --------dropdown selection challenge----------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(link)
    # find operands and calculate sum
    a = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    b = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    value = str(a + b)
    # initialize Select element and select answer from dropdown
    select = Select(browser.find_element(By.XPATH, '//select[@id="dropdown"]'))
    select.select_by_value(value)
    # find button and click it
    browser.find_element(By.CSS_SELECTOR, "button.btn[type='submit']").click()
    sleep(10)
