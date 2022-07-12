# configuration file for all tests
# can contain frequently used fixtures
import pytest
from selenium import webdriver


supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

# now you can specify browser name in command line options by using --browser_name='browser-name'.
# supported variants: chrome, firefox
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name in supported_browsers:
        browser = supported_browsers.get(browser_name)()
        print(f"\nstart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()