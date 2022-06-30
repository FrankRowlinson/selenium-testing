# --------upload files via Selenium---------

import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    # get current directory and filename in variables
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = "file_to_upload.txt"
    browser.get(link)
    # insert info into all required fields ignoring everything else
    fields = browser.find_elements(By.XPATH, "//input[@type='text' and @required]")
    for field in fields:
        field.send_keys('placeholder_info')
    # find input tag with type 'file' to upload file using .send_keys(path)
    file_input = browser.find_element(By.XPATH, "//input[@type='file' and @id='file']")
    file_input.send_keys(os.path.join(current_dir, filename))
    # and familiar button click to finish
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(10)

