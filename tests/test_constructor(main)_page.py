import pytest

import settings
from data import StellarBurgersTestData
from locators import ConstructorLocators, LoginLocators, ProfilePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorPage:
    # Успешный вход через кнопкки "Личный кабинет" и "Войти в аккаунт" на главной (конструктор) странице
    @pytest.mark.parametrize('button', [ConstructorLocators.BUTTON_PERSONAL_ACCOUNT,
                                        ConstructorLocators.BUTTON_LOG_IN_ACCOUNT])
    def test_log_in_by_click_on_buttons_in_constructor_page(self, driver, button):
        driver.find_element(*button).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_SUBMIT).click()
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(ProfilePage.LINK_PROFILE, "Профиль"))

        assert driver.current_url == settings.URL + "/account/profile"

    # Переход в личный кабинет
    def test_go_to_personal_account_page(self, driver, log_in):
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        assert driver.current_url == settings.URL + '/account/profile'

    # Переход к разделу Булки
    def test_go_to_section_rolls(self, driver):
        driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_SAUCES).click()
        driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_ROLLS).click()
        section_rolls = WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.visibility_of_element_located(
            ConstructorLocators.SECTION_ROLLS))
        assert section_rolls.is_displayed(), "Does not scrolling to the Section Rolls"

    # Переход к разделу Соусы
    def test_go_to_section_sauces(self, driver):
        driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_SAUCES).click()
        section_sauces = WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.visibility_of_element_located(
            ConstructorLocators.SECTION_SAUCES))
        assert section_sauces.is_displayed(), "Does not scrolling to the Section sauces"

    # Переход к разделу Начинки
    def test_go_to_section_fillings(self, driver):
        driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_FILLINGS).click()
        section_fillings = WebDriverWait(driver, settings.MAX_WAIT_TIME).until(EC.visibility_of_element_located(
            ConstructorLocators.SECTION_FILLINGS))
        assert section_fillings.is_displayed(), "Does not scrolling to the Section fillings"
