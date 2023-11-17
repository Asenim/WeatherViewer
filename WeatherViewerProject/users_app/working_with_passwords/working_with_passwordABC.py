from abc import ABC


class WorkingWithPasswordABC(ABC):
    def __init__(self, user_password):
        self._user_password = bytes(user_password, 'utf-8')
