from Model import Model

class User(Model):

    def __init__(self):
        super().__init__()
        self._username = None
        self._password = None

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
    
    @username.setter
    def username(self, value):
        self._username = value
        self.notify_views(self.username)
    
    @password.setter
    def password(self, value):
        self._password = value
        self.notify_views(self.password)
