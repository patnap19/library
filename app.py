from library import Library
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


class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.auth_manager = AuthManager()
        
    def admin_menu(self):
        while True:
            print("📘 PANEL ADMINISTRATORA")
            print("1. Wyświetl wszystkie książki")
            print("2. Dodaj książkę")
            print("3. Edytuj książkę")
            print("4. Usuń książkę")
            print("5. Dodaj użytkownika")
            print("6. Historia logów")
            print("0. Wyloguj się")
            choice = input("Twój wybór: ")

            match choice:
                case "1": self.library.print_all_books()
                case "2": self.library.add_book_to_library()
                case "3": self.library.edit_book_data()
                case "4": self.library.delete_book_from_library()
                case "5": self.auth_manager.users.create_user()
                case "6": self.library.logs_history_display_handler()
                case "0": print("Wylogowano."); break
                case _: print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")
            clear_screen()

    def user_menu(self):
        while True:
            print("📖 PANEL UŻYTKOWNIKA")
            print("1. Wyświetl wszystkie książki")
            print("2. Filtruj książki")
            print("3. Wypożycz książkę")
            print("4. Zwróć książkę")
            print("5. Historia logów")
            print("0. Wyloguj się")
            choice = input("Twój wybór: ")

            match choice:
                case "1": self.library.print_all_books()
                case "2": self.library.filter_books()
                case "3": self.library.book_action_handler('borrow', self.auth_manager.current_user)
                case "4": self.library.book_action_handler('return', self.auth_manager.current_user)
                case "5": self.library.logs_history_display_handler()
                case "0": print("Wylogowano."); break
                case _: print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")
            clear_screen()

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


app = LibraryApp()
clear_screen()
app.run()

#TODO
# 1. Wyszukiwanie logów po akcji
# 2. Może zapisywać logi książki konretnej do innych plików. - opcjonalne na przyszłość
# 3. Wykonać użytkowników?