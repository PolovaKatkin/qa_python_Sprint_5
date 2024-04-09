from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTRATION_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  # поле Имя
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле Email
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  # поле Пароль
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # кнопка Зарегистрироваться
    REGISTRATION_PASSWORD_INPUT_INCORRECT = (By.XPATH, "//p[@class = 'input__error text_type_main-default']") \
        # Текст Некорректный пароль у поля Пароль
    LINK_TO_LOGIN_PAGE = (By.XPATH, "//a[@href = '/login']")  # Ссылка "Войти" на страницу авторизации


class LoginLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text() = 'Вход']")  # Текст "Вход" на странице авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name = 'name']")  # Поле Email
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  # Поле Пароль
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти"


class ConstructorLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет"
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    HEADING_IN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # Заголовок главной страницы "Соберите бургер"
    NAME_BUTTON_SECTION_ROLLS = (By.XPATH, "//span[text() = 'Булки']")  # Кнопка "Булки" для перехода к булкам
    NAME_BUTTON_SECTION_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")  # Кнопка "Соусы" для перехода к соусам
    NAME_BUTTON_SECTION_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")  # Кнопка "Начинки" для перехода к начинкам
    SECTION_ROLLS = (By.XPATH, "//h2[text() = 'Булки']")  # Текст раздела "Булки"
    SECTION_SAUCES = (By.XPATH, "//h2[text() = 'Соусы']")  # Текст раздела "Соусы"
    SECTION_FILLINGS = (By.XPATH, "//h2[text() = 'Начинки']")  # Текст раздела "Начинки"


class ForgotPasswordLocators:
    LINK_TO_LOGIN_PAGE = (By.XPATH, "//a[@href = '/login']")  # Ссылка "Войти" на страницу авторизации


class ProfilePage:
    LINK_PROFILE = (By.XPATH, "//a[@href='/account/profile']")  # Кнопка Профиль в личном кабинете
    LINK_CONSTRUCTOR = (By.XPATH, "//li/a[@href = '/']")  # Кнопка Конструктор
    LINK_LOGO = (By.XPATH, "//div/a[@href = '/']")  # Логотип сайта
    BUTTON_LOG_OUT = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка Выход
