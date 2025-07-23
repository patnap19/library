from library import *
from auth_manager import AuthManager

class AdminPanel():
    def __init__(self):
        self.library = Library()
        self.auth_manager = AuthManager()
    
    def admin_panel_menu_choice(self, admin_choice):

            match admin_choice:
                case "1": self.library.print_all_books()
                case "2": self.library.add_book_to_library()
                case "3": self.library.edit_book_data()
                case "4": self.library.delete_book_from_library()
                case "5": self.auth_manager.users.create_user()
                case "6": self.library.logs_history_display_handler()
                case "0": print("Wylogowano."); return
                case _: print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")