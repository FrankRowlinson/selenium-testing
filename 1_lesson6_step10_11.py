from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# context managers are better than try:, finally: here
with webdriver.Chrome() as browser:
    # this link leads to the website where my test will fail miserably
    # try changing number 2 to 1 and it will work 
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # looking for required fields using XPATH
    browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Test_name")
    browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Test_pass")
    browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("Test_email@dot.com")

    # find and click that submit button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Assert nothing went wrong before, here it sure will :D
    assert welcome_text == "Congratulations! You have successfully registered!", "Simple registration failed"
    time.sleep(10)