import json
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BOOKS_FILE = 'books.json'
LOG_HISTORY_FILE = 'log_history.json'

def log_action(action, book_title):
    log_history = load_file(LOG_HISTORY_FILE)
    new_log = {
        'time': datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
        'action': action,
        'book_title': book_title
    }
    log_history.append(new_log)
    with open(LOG_HISTORY_FILE, 'w', encoding="utf-8") as file:
        json.dump(log_history, file, ensure_ascii=False, indent=4)

def save_books(data, file_path=BOOKS_FILE):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_book_to_library(title_of_new_book):
    author_of_new_book = input("Podaj autora: ")
    category_of_new_book = input("Podaj gatunek: ")
    while True:
        try:
            year_of_new_book = int(input("Podaj rok wydania: "))
            break
        except ValueError:
            print("Podano niepoprawny rok. Wprowadź liczbę całkowitą.")

    new_book = {
        'tytuł': title_of_new_book.title(),
        'autor': author_of_new_book.title(),
        'rok': year_of_new_book,
        'gatunek': category_of_new_book.title(),
        'wypozyczona': False
    }
    library = load_file(BOOKS_FILE)
    library.append(new_book)
    log_action("Dodano", new_book['tytuł'])
    save_books(library)

    print("Książka została dodana do biblioteki.")

def book_exists_by_title(phrase_to_check):
    data = load_file(BOOKS_FILE)
    for book in data:
        if phrase_to_check.lower() == book['tytuł'].lower():
            return True
    return False

def load_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def print_all_books():
    data = load_file(BOOKS_FILE)
    for i, book in enumerate(data, 1):
        print(f"{i}.")
        print_book(book)

def print_all_free_books():
    data = load_file(BOOKS_FILE)
    for i, book in enumerate(data, 1):
        if book['wypozyczona'] == False:
            print(f"{i}.")
            print_book(book)

def print_book(book_to_print):
        print(f"\nTytuł: {book_to_print['tytuł']}")
        print(f"Autor: {book_to_print['autor']}")
        print(f"Rok wydania: {book_to_print['rok']}")
        print(f"Gatunek: {book_to_print['gatunek']}")
        print(f"Wypożyczona: {'Tak' if book_to_print['wypozyczona'] else 'Nie'}")
        print('-' * 30)

def find_book(area_of_search):
    clear_screen()
    phrase_to_find = input('Podaj frazę do wyszukiwania: ').lower()
    data = load_file(BOOKS_FILE)
    found = False
    for book in data:
        if phrase_to_find in str(book[area_of_search]).lower():
            found = True
            print_book(book)
    if not found:
        print("Niestety nie odnaleźliśmy żadnej książki pasującej do podanej przez Ciebie frazy.")
        print('-' * 30)

def show_menu():
    print("Wybierz opcję: ")
    print("1. Wyświetl wszystkie książki.")
    print("2. Wyszukaj książki.")
    print("3. Dodaj książkę.")
    print("4. Wypożycz książkę.")
    print("5. Zwróć książkę.")
    print("6. Wyświetl statystyki.")
    print("0. Zakończ pracę.")

    
def show_library_stats():
    clear_screen()
    data = load_file(BOOKS_FILE)
    all_books_number = len(data)
    all_borrowed_books_number = 0
    for book in data:
        if book['wypozyczona'] == True:
            all_borrowed_books_number += 1
    print(f"Łączna liczba książek w bibliotece: {all_books_number}")
    print(f"Liczba wypożyczonych książek: {all_borrowed_books_number}")
    print("Działa")

def borrow_book(index_of_book):
    data = load_file(BOOKS_FILE)

    if 1 <= index_of_book <= len(data):
        book = data[index_of_book - 1]
        if book['wypozyczona']:
            print("Ta książka jest już wypożyczona.")
            return None
        data[index_of_book - 1]['wypozyczona'] = True
        save_books(data)
        return book
    else:
        print("Niepoprawny indeks książki.")
        return None

def borrow_book_handler():
    clear_screen()
    all_books = load_file(BOOKS_FILE)
    available_books = [book for book in all_books if not book['wypozyczona']]

    if not available_books:
        print("Brak dostępnych książek do wypożyczenia.")
        print('-' * 30)
        return

    print("Wybierz książkę, którą chcesz wypożyczyć:")

    for i, book in enumerate(available_books, 1):
        print(f"{i}.")
        print_book(book)

    try:
        user_input = int(input("Twój wybór: "))
        if user_input < 1 or user_input > len(available_books):
            raise ValueError
    except ValueError:
        print("Nieprawidłowy wybór. Wprowadź poprawny numer z listy.")
        print('-' * 30)
        return

    selected_book = available_books[user_input - 1]
    original_index = all_books.index(selected_book)

    clear_screen()
    borrowed_book = borrow_book(original_index + 1)
    log_action('Wypożyczono', borrowed_book['tytuł'])
    if borrowed_book is None:
        print("Przenosimy Cię do Menu Głównego")
    else:
        print("Wypożyczona przez Ciebie książka to: ")
        print_book(borrowed_book)

def add_book_handler():
    clear_screen()
    print(30 * '-')
    title_of_new_book = input("Podaj tytuł książki: ")
    if book_exists_by_title(title_of_new_book):
        print("Podana książka już istnieje w naszej bibliotece")
        print('-' * 30)
    else:
        add_book_to_library(title_of_new_book)
        print('-' * 30)

def search_handler():
    clear_screen()
    while True:
        which_area_search = input("W której kategorii chcesz poszukać książki?\n1.Autor\n2.Tytuł\n3.Gatunek\n4.Rok wydania\n0.Wyjście\nTwój wybór: ")
        if which_area_search == '1':
            find_book('autor')
        elif which_area_search == '2':
            find_book('tytuł')
        elif which_area_search == '3':
            find_book('gatunek')
        elif which_area_search == '4':
            find_book('rok')
        elif which_area_search == '0':
            break
        else:
            print("Nie wybrano żadnej opcji, spróbuj ponownie")
            
def return_book(index_of_book):
    data = load_file(BOOKS_FILE)

    if 1 <= index_of_book <= len(data):
        book = data[index_of_book - 1]
        if not book['wypozyczona']:
            print("Ta książka nie jest wypożyczona.")
            return None
        data[index_of_book - 1]['wypozyczona'] = False
        save_books(data)
        return book
    else:
        print("Niepoprawny indeks książki.")
        return None
            
def return_book_handler():
    clear_screen()
    all_books = load_file(BOOKS_FILE)
    borrowed_books = [book for book in all_books if book['wypozyczona']]
    if not borrowed_books:
        print("Brak wypożyczonyhch książek.")
        print('-' * 30)
        return
    print("Lista książek, które musisz zwrócić: ")
    for i, book in enumerate(borrowed_books, 1):
        print(f"{i}.")
        print_book(book)

    try:
        user_input = int(input("Twój wybór: "))
        if user_input < 1 or user_input > len(borrowed_books):
            raise ValueError
    except ValueError:
        clear_screen()
        print("Nieprawidłowy wybór. Wprowadź poprawny numer z listy.")
        print('-' * 30)
        return

    selected_book = borrowed_books[user_input - 1]
    original_index = all_books.index(selected_book)

    clear_screen()
    returned_book = return_book(original_index + 1)
    if returned_book is None:
        print("Przenosimy Cię do Menu Głównego")
    else:
        print("Zwróciłeś książkę")
        log_action("Zwrócono", returned_book['tytuł'])
        print_book(returned_book)
    

def library():

    print("Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?")

    while True:
        show_menu()
        user_choice = input("Twój wybór: ")

        if user_choice == '1':
            clear_screen()
            print_all_books()
        elif user_choice == '2':
            search_handler()
        elif user_choice == '3':
            add_book_handler()
        elif user_choice == '4':
            borrow_book_handler()
        elif user_choice == '5':
            return_book_handler()
        elif user_choice == '6':
            show_library_stats()
        elif user_choice == '0':
            clear_screen()
            print("Dziękujęmy, do zobaczenia")
            print('-' * 30)
            break
        else:
            clear_screen()
            print("Nie wybrano żadnej opcji, spróbuj ponownie")
            print('-' * 30)

if __name__ == "__main__":
    library()
    
# def update_book_status(index, wypozyczona):
#     data = load_file(BOOKS_FILE)
#     if 1 <= index <= len(data):
#         book = data[index - 1]
#         if book['wypozyczona'] == wypozyczona:
#             print("Nieprawidłowa operacja na książce.")
#             return None
#         data[index - 1]['wypozyczona'] = wypozyczona
#         save_books(data)
#         return book
#     print("Niepoprawny indeks książki.")


# TODO change two function to one function