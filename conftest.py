import pytest
from selenium import webdriver
import settings
from data import StellarBurgersTestData
from locators import LoginLocators, ConstructorLocators, ProfilePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def log_in(driver):
    driver.get(settings.URL + settings.LOGIN_PAGE)
    driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(*StellarBurgersTestData.AUTH_EMAIL)
    driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
    driver.find_element(*LoginLocators.LOGIN_SUBMIT).click()
    driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
        EC.text_to_be_present_in_element(ProfilePage.LINK_PROFILE, "Профиль"))
