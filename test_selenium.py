import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Constants
URL = "https://www.google.com/"
SEARCH_TERM = "nokia wikipedia"
EXPECTED_YEAR = "1865"
GOOGLE_SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='q']")
GOOGLE_SEARCH_BUTTON = (By.CSS_SELECTOR, "input[name='btnK']")
WIKIPEDIA_LINK = (By.PARTIAL_LINK_TEXT, "Wikipedia")
FOUNDING_YEAR_XPATH = (
    By.XPATH,
    "//th[contains(text(), 'Founded')]/following-sibling::td",
)
SCREENSHOT_FILENAME = "Nokia_Wikipedia_Screenshot.png"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def search_google(driver, search_term):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.presence_of_element_located(GOOGLE_SEARCH_INPUT))
    search_input.send_keys(search_term)
    search_button = wait.until(EC.element_to_be_clickable(GOOGLE_SEARCH_BUTTON))
    search_button.click()


def click_wikipedia_link(driver):
    wait = WebDriverWait(driver, 10)
    wikipedia_link = wait.until(EC.presence_of_element_located(WIKIPEDIA_LINK))
    wikipedia_link.click()


def verify_wikipedia_page(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(FOUNDING_YEAR_XPATH))
    driver.save_screenshot(SCREENSHOT_FILENAME)
    assert "Nokia" in driver.title, "Page title does not contain 'Nokia'"


def verify_founding_year(driver):
    founding_year = driver.find_element(*FOUNDING_YEAR_XPATH).text
    assert (
        founding_year == EXPECTED_YEAR
    ), f"Founding year does not match. Expected: {EXPECTED_YEAR}, Found: {founding_year}"


def search_nokia_on_wikipedia(driver):
    search_google(driver, SEARCH_TERM)
    click_wikipedia_link(driver)
    verify_wikipedia_page(driver)
    verify_founding_year(driver)


def test_search_nokia_on_wikipedia(driver):
    search_nokia_on_wikipedia(driver)
