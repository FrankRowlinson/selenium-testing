# --------collect fail reports to pass a challenge :^) --------------

import time
from math import log
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


links = ["https://stepik.org/lesson/236896/step/1", 
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize("link", links)
def test_optional_feedback(browser, link):
    browser.get(link)
    # some elements on page load with a little 
    browser.implicitly_wait(10)
    field = browser.find_element(By.XPATH, "//textarea[@required]")
    # this is a specific formula to calculate an answer to these tests
    answer = log(int(time.time()))
    field.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    hint = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    print(hint)
    assert hint == "Correct!", f"{hint} - hint message doesn't match expected 'Correct!'"
