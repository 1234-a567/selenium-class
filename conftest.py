import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def login_driver():
    login_driver = WebDriver()
    login_driver.maximize_window()
    login_driver.get("https://demowebshop.tricentis.com/login")
    yield login_driver
    login_driver.quit()


@pytest.fixture()
def register_driver():
    register_driver = WebDriver()
    register_driver.maximize_window()
    register_driver.get("https://demowebshop.tricentis.com/register")
    yield register_driver
    register_driver.quit()
