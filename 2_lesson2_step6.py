# ---------robo-captcha 3.0: JavaScript edition :^) ---------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


# same function as in previous steps. Calculate value of f(x)
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    # same as before. Calculate x and send it into answer field
    x = int(browser.find_element(By.CSS_SELECTOR, 'label>span#input_value').text)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    field.send_keys(calc(x))
    # hide huge footer on page because it makes all required elements unreachable
    footer = browser.find_element(By.TAG_NAME, 'footer')
    browser.execute_script('arguments[0].style.visibility = "hidden"', footer)
    # proceed with everything else...
    # trying to use different approaches with element search just for the sake of practice
    # kinda liking XPATH, was afraid of using it at first <3
    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(10)

