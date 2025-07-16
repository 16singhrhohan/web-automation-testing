import pytest
from pages.login_page import LoginPage
from utils.browser_setup import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_pass")
    error = login_page.get_error_message()
    assert "Username and password do not match" in error
