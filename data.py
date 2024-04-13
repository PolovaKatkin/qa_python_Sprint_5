from random import randint, choice
from string import ascii_letters


class StellarBurgersTestData:
    AUTH_EMAIL = "ekaterina_polova_7_702@mail.ru"
    AUTH_PASSWORD = "Grut86"
    AUTH_PASSWORD_INCORRECT = "G45d"


class UserDataGenerator:
    @staticmethod
    def correct_user_data_generator():
        user_data = {'name': str(choice(ascii_letters) * 6),
                     'email': "ekaterina_polova_7" + str(randint(100, 999)) + '@email.com',
                     'password': str(randint(100000, 999999))}
        return user_data

