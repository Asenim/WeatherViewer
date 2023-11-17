import bcrypt
from users_app.working_with_passwords.working_with_passwordABC import WorkingWithPasswordABC


class PasswordVerification(WorkingWithPasswordABC):
    def __init__(self, user_password, hashed_pass_from_db):
        """
        :param user_password: Принимает на вход python str
            и преобразует в byte строку
        :param hashed_pass_from_db: Принимает на вход python str
            и преобразует в byte строку
        """
        super().__init__(user_password)
        self.__hashed_pass_from_db = bytes(hashed_pass_from_db, 'utf-8')

    def password_verification(self):
        """
        Метод проверяет правильно ли введен пароль
        :return True/False:
        """
        __check_password = bcrypt.checkpw(
            password=self._user_password,
            hashed_password=self.__hashed_pass_from_db
        )

        return __check_password
