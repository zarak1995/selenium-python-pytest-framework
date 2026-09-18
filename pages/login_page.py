from selenium.webdriver.common.by import By
from utilities.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        logger.info(f"Entering username: {username}")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        logger.info("Entering password")
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        logger.info("Clicking login button")