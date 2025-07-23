from library import Library
from utils import *
from admin_panel import AdminPanel
from auth_manager import AuthManager
from user_panel import UserPanel
from library_ui import LibraryUI


class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.auth_manager = AuthManager()
        self.library_ui = LibraryUI()
        self.admin_panel = AdminPanel()
        self.user_panel = UserPanel(auth_manager=self.auth_manager)
        
    def admin_menu(self):
        is_log = True
        while is_log:
            self.library_ui.display_admin_menu()
            choice = input("Twój wybór: ")
            if not self.admin_panel.admin_panel_menu_choice(choice):
                is_log = False

    def user_menu(self):
        is_log = True
        while is_log:
            self.library_ui.display_user_menu()
            choice = input("Twój wybór: ")
            if not self.user_panel.user_panel_menu_choice(choice):
                is_log = False

    def run(self):

        print("Witaj w bibliotece szkolnej. Zaloguj się, aby korzystać.")
        user = self.auth_manager.log_user()

        if not user:
            print("Przekroczono ilość prób logowania.")
            return

        clear_screen()
        print(f"Zalogowano jako {user.name} {user.surname}.")

        if getattr(user, "is_admin", False):
            self.admin_menu()
        else:
            self.user_menu()
        print("Dziękujemy za skorzystanie z biblioteki. Do zobaczenia!")

app = LibraryApp()
app.run()