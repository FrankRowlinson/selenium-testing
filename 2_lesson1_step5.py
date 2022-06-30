# ---------robo-captcha challenge----------

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep


# function to solve math problem on page
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    # find value of x on page
    x = browser.find_element(By.XPATH, '//label/span[@id="input_value"]').text
    field = browser.find_element(By.XPATH, '//input[@id="answer" and @required]')
    # send answer calculated by calc function
    field.send_keys(calc(x))
    # find everything on page that needs to be clicked on
    checkbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    radiobtn = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    submitbtn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # and click on it
    checkbox.click()
    radiobtn.click()
    submitbtn.click()
    sleep(10)
