import os
from utils import *
from user import UsersManager

class AuthManager:
    def __init__(self):
        self.users = UsersManager()
        self.current_user = None

    def log_user(self):
        attempts = 3
        while attempts > 0:
            user_login = get_valid_text("Podaj login: ")
            user_password = get_valid_text("Podaj hasło: ")

            for user in self.users.users_list:
                if user_login == user.login and user_password == user.password:
                    self.current_user = user
                    return self.current_user

            if not self.current_user:
                attempts -= 1
                if attempts == 0:
                    return self.current_user
                clear_screen()
                print("Podane dane są niewłaściwe, spróbuj ponownie.")
                print(f"Pozostało {attempts} prób.")