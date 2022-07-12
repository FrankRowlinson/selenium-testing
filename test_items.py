from selenium.webdriver.common.by import By
import time


def test_add_to_basket_button_is_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # sleep to see whether or not language options worked
    time.sleep(15)
    # if selector is not unique, find_elements will find more than 1 element.
    # if there is no element with such selector, NoSuchElementException WILL NOT BE RAISED, 
    # it just will return empty list
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(buttons) == 1, "button not found or selector is not unique"