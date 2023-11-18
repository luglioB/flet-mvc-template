from models.User import User

class UserController():

    def __init__(self, model: User):
        super().__init__()
        self.model = model

    def update_credentials(self, username, password):
        self.model.username = username
        self.model.password = password 