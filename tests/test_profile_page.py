import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import LoginLocators, ProfilePage


class TestProfilePage:
    # Переход из личного кабинета в конструктор по клику на "Конструктор" и логотип Stellar Burgers
    @pytest.mark.parametrize('link', [ProfilePage.LINK_CONSTRUCTOR, ProfilePage.LINK_LOGO])
    def test_go_to_constructor_page_click_on_the_button_constructor(self, driver, log_in, link):
        driver.find_element(*link).click()

        assert driver.current_url == settings.URL + settings.MAIN_PAGE

    # Выход из аккаунта по клику на "Выход" в личном кабинете
    def test_log_out_of_the_profile(self, driver, log_in):
        driver.find_element(*ProfilePage.BUTTON_LOG_OUT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        log_in_exist = driver.find_element(*LoginLocators.LOGIN_TITLE).text

        assert log_in_exist == 'Вход', "Login Title does not exist"
