import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="Driver/chromedriver_win32 (7)/chromedriver.exe")
        print("Launching Chrome browser .......")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="Driver/geckodriver/geckodriver.exe")
        print("Launching Firefox browser .......")
    else:
        driver = webdriver.Chrome(executable_path="Driver/chromedriver_win32 (7)/chromedriver.exe")
    return driver


def pytest_addoption(parser):               # This will get the value of the browser from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                       # This will return the browser value tot he setup method above
    return request.config.getoption("--browser")


####################### pytest HTML Report  ###########

def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce Automation framework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Victor'


##### It is hook for delete / Modify Environment info to HTMK Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

