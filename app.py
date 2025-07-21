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
                    print("Przekroczono ilość możliwości logowania. Spróbuj ponownie później")
                    return self.current_user
                clear_screen()
                print("Podane dane są niewłaściwe, spróbuj ponownie.")
                print(f"Pozostało {attempts} prób.")


class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.auth_manager = AuthManager()

    def run(self):
            user = self.auth_manager.log_user()
            if not user:
                print("NIE MA")
                return
            else:
                print("DZIAŁA")
            print("Witaj w bibliotece szkolnej. Zaloguj się, aby korzystać.")
            while True:
                clear_screen()
                print("1. Pokaż książki\n2. Dodaj książkę\n3. Filtruj książki\n4. Statystyki\n5. Wypożycz książkę\n6. Zwróć książkę\n7. Edytuj książkę\n8. Usuń książkę\n9. Historia logów\n0. Wyjście")
                choice = input("Wybierz opcję: ")

                if choice == "1":
                    self.library.print_all_books()
                elif choice == "2":
                    self.library.add_book_to_library()
                elif choice == "3":
                    self.library.filter_books()
                elif choice == '4':
                    self.library.show_stats()
                elif choice == '5':
                    self.library.book_action_handler('borrow')
                elif choice == '6':
                    self.library.book_action_handler('return')
                elif choice == '7':
                    self.library.edit_book_data()
                elif choice == '8':
                    self.library.delete_book_from_library()
                elif choice == '9':
                    self.library.logs_history_display_handler()
                elif choice == "0":
                    clear_screen()
                    print("Do zobaczenia!")
                    break
                else:
                    print("❌ Niepoprawny wybór.")

                input("\nNaciśnij Enter, aby kontynuować...")

app = LibraryApp()
app.run()

#TODO
# 1. Wyszukiwanie logów po akcji
# 2. Może zapisywać logi książki konretnej do innych plików. - opcjonalne na przyszłość
# 3. Wykonać użytkowników?