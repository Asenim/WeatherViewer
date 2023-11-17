from users_app.working_with_passwords.working_with_passwordABC import WorkingWithPasswordABC
import bcrypt


class PasswordHashing(WorkingWithPasswordABC):
    def __int__(self, user_password):
        """
        :param user_password: Принимает на вход python str
            и преобразует в byte строку
        """
        super().__init__(user_password)

    def password_hashing(self):
        """
        Метод для хеширования пароля
        :return __decode_hash_password: Возвращаем захешированный пароль
        """
        __crypt_salt = bcrypt.gensalt()

        __hash_password = bcrypt.hashpw(
            password=self._user_password,
            salt=__crypt_salt
        )
        # Конвертируем байты в строку
        __decode_hash_password = str(__hash_password, 'utf-8')

        return __decode_hash_password
