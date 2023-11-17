from users_app.models import Users


class InsertDataInUsers:
    def __init__(self, login, password):
        user_model_object = Users(Login=login, Password=password)
        user_model_object.save()
