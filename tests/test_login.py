from pages.login_page import LoginPage
from utilities import config


def test_open_saucedemo(driver):
    driver.get(config.BASE_URL)
    print(driver.title)
    assert driver.title == "Swag Labs"


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)
A
    print("\n[DEBUG] Current URL after login:", driver.current_url)
    print("[DEBUG] Page title after login:", driver.title)

    assert "inventory" in driver.current_url