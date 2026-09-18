from pages.login_page import LoginPage
from utilities import config
from utilities.logger import get_logger
logger = get_logger(__name__)


def test_open_saucedemo(driver):
    logger.info("Starting test_url")
    driver.get(config.BASE_URL)
    print(driver.title)
    assert driver.title == "Swag Labs"
    logger.info("test_valid_url completed successfully")


def test_valid_login(driver):
    logger.info("Starting test_valid_login")
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)

    print("\n[DEBUG] Current URL after login:", driver.current_url)
    print("[DEBUG] Page title after login:", driver.title)

    assert "inventory" in driver.current_url
    logger.info("test_valid_login completed successfully")