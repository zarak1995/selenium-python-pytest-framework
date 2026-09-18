from utilities.logger import get_logger
logger = get_logger("CONFTEST")

import pytest
import os
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    logger.info("Initializing Chrome driver")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.implicitly_wait(10)
    logger.info("Chrome driver initialized and window maximized")

    yield driver

    logger.info("Quitting Chrome driver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        if report.passed:
            logger.info(f"TEST PASSED: {item.name}")
        elif report.failed:
            logger.error(f"TEST FAILED: {item.name}")

            driver = item.funcargs.get("driver")
            if driver:
                os.makedirs("reports/screenshots", exist_ok=True)
                screenshot_path = f"reports/screenshots/{item.name}.png"
                driver.save_screenshot(screenshot_path)
                extra.append(extras.image(screenshot_path))
                logger.info(f"Screenshot saved: {screenshot_path}")

    report.extra = extra
