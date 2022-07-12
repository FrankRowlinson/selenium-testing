from selenium.webdriver.common.by import By


def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")