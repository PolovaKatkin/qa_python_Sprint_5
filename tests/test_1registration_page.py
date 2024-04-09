from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import settings
from data import StellarBurgersTestData
from locators import RegistrationPageLocators, LoginLocators, ConstructorLocators, ProfilePage


class TestRegistration:
    # Успешная регистрация
    def test_successful_registration(self, driver):
        driver.get(settings.URL + "/register")
        name_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(*StellarBurgersTestData.AUTH_NAME)
        email_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        password_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
        submit_button = driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON)
        submit_button.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        assert driver.find_element(*LoginLocators.LOGIN_TITLE).is_displayed(), "Login Title does not exist"

    # Ошибка для некорректного пароля
    def test_error_text_appears_when_the_password_is_less_than_6_symbols(self, driver):
        driver.get(settings.URL + "/register")
        name_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_NAME_INPUT)
        name_input.send_keys(*StellarBurgersTestData.AUTH_NAME)
        email_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        password_input = driver.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(*StellarBurgersTestData.AUTH_PASSWORD_INCORRECT)
        submit_button = driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON)
        submit_button.click()

        assert driver.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD_INPUT_INCORRECT).is_displayed(), \
            "Error text does not exist"

    # Успешный вход через кнопку в форме регистрации
    def test_log_in_by_click_on_link_in_registration_page(self, driver):
        driver.get(settings.URL + "/register")
        driver.find_element(*RegistrationPageLocators.LINK_TO_LOGIN_PAGE).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_SUBMIT).click()
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(ProfilePage.LINK_PROFILE, "Профиль"))

        assert driver.current_url == settings.URL + "/account/profile"
