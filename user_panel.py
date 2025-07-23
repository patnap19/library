from library import Library
from auth_manager import AuthManager 
class UserPanel:
    def __init__(self, auth_manager):
        self.library = Library()
        self.auth_manager = AuthManager()
        
    def user_panel_menu_choice(self, user_choice):
        match user_choice:
            
            case "1": self.library.print_all_books()
            case "2": self.library.filter_books()
            case "3": self.library.book_action_handler('borrow', self.auth_manager.current_user)
            case "4": self.library.book_action_handler('return', self.auth_manager.current_user)
            case "5": self.library.logs_history_display_handler()
            case "0": print("Wylogowano."); return
            case _: print("❌ Niepoprawny wybór.")

        input("\nNaciśnij Enter, aby kontynuować...")