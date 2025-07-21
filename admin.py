import user

class Admin(user.User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_admin = True
        
class AdminPanel:
    def __init__(self):
        pass