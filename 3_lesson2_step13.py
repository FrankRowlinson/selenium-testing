# the task here is to rewrite code from 1_lesson6_step10_11.py
# using unittest.py library

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_first_variation(self):
        # here I finally changed my naming to 'driver', cause it's shorter and clearer
        with webdriver.Chrome() as driver:
            link = "http://suninjuly.github.io/registration1.html"
            # tell my driver to wait if element is still not present or in some other cases
            driver.implicitly_wait(5)
            driver.get(link)
            # find, as before, all required fields using XPATH
            driver.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Test_name")
            driver.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Test_pass")
            driver.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("Test_email@dot.com")

            # find and click that submit button
            button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            
            welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            supposed_welcome_text = "Congratulations! You have successfully registered!"
            self.assertEqual(welcome_text, supposed_welcome_text, \
                "Registration failed. Text on screen doesn't look right")

    def test_second_variation(self):
        # here I finally changed my naming to 'driver', cause it's shorter and clearer
        with webdriver.Chrome() as driver:
            link = "http://suninjuly.github.io/registration2.html"
            # tell my driver to wait if element is still not present or in some other cases
            driver.implicitly_wait(5)
            driver.get(link)
            # find, as before, all required fields using XPATH
            driver.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Test_name")
            driver.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Test_pass")
            driver.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("Test_email@dot.com")

            # find and click that submit button
            button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            
            welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            supposed_welcome_text = "Congratulations! You have successfully registered!"
            self.assertEqual(welcome_text, supposed_welcome_text, \
                "Registration failed. Text on screen doesn't look right")

            
if __name__ == "__main__":
    unittest.main()

# Code looks terrible because of repetitive blocks. 
# Will fix it in the future when I'm comfortable with test libraries