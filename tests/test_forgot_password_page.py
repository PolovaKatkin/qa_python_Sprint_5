from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import settings
from data import StellarBurgersTestData
from locators import LoginLocators, ConstructorLocators, ProfilePage, ForgotPasswordLocators


class TestForgotPasswordPage:
    # Вход через кнопку в форме восстановления пароля
    def test_log_in_by_click_on_link_in_forgot_password_page(self, driver):
        driver.get(settings.URL + settings.FORGOT_PASSWORD_PAGE)
        driver.find_element(*ForgotPasswordLocators.LINK_TO_LOGIN_PAGE).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_SUBMIT).click()
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(ProfilePage.LINK_PROFILE, "Профиль"))

        assert driver.current_url == settings.URL + settings.ACCOUNT_PROFILE_PAGE
