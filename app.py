from library import Library
from utils import clear_screen

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
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
                print("Do zobaczenia!")
                break
            else:
                print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")

app = LibraryApp()
app.run()