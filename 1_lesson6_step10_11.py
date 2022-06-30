from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Делаю все через менеджер контекста, он удобнее, чем операторы try:, finally:
with webdriver.Chrome() as browser:
    # Этот тест упадет. Замените ссылку на первый сайт, чтобы прошло. 
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ищу поля по XPATH - должен быть атрибут required, который задает обязательность поля
    # и класс first, second или third, которые определяют очередность полей
    browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Test_name")
    browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Test_pass")
    browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("Test_email@dot.com")

    # Нажимаем кнопку "отправить"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # После запятой добавил сообщение об ошибке, если будет сгенерирована AssertionError
    assert welcome_text == "Congratulations! You have successfully registered!", "Simple registration failed"
    time.sleep(10)