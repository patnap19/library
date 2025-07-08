import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BOOKS_FILE = 'books.json'

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
    library = load_books(BOOKS_FILE)
    library.append(new_book)
    save_books(library)
    
    print("Książka została dodana do biblioteki.")

def book_exists_by_title(phrase_to_check):
    data = load_books(BOOKS_FILE)
    for book in data:
        if phrase_to_check.lower() == book['tytuł'].lower():
            return True
    return False

def load_books(file_path=BOOKS_FILE):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def print_all_books():
    data = load_books(BOOKS_FILE)
    for i, book in enumerate(data, 1):
        print(f"{i}.")
        print_book(book)
        
def print_all_free_books():
    
    data = load_books(BOOKS_FILE)
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
    data = load_books(BOOKS_FILE)
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
    print("0. Zakończ pracę.")
    
def borrow_book(index_of_book):
    data = load_books(BOOKS_FILE)
    
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
    all_books = load_books(BOOKS_FILE)
    available_books = [book for book in all_books if not book['wypozyczona']]

    if not available_books:
        print("Brak dostępnych książek do wypożyczenia.")
        print('-' * 30)
        return  # ⬅ ważne: wyjście z funkcji

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

    # Ustalamy, który indeks ma książka w oryginalnej liście `all_books`
    selected_book = available_books[user_input - 1]
    original_index = all_books.index(selected_book)

    clear_screen()
    borrowed_book = borrow_book(original_index + 1)  # bo indeksy w `borrow_book` są 1-based
    if borrowed_book is None:
        print("Przenosimy Cię do Menu Głównego")
    else:
        print("Wypożyczona przez Ciebie książka to: ")
        print_book(borrowed_book)
                
def library():

    print("Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?")

    while True:
        show_menu()
        user_choice = input("Twój wybór: ")

        if user_choice == '1':
            clear_screen()
            print_all_books()
        elif user_choice == '2':
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
        elif user_choice == '3':
            clear_screen()
            print(30 * '-')
            title_of_new_book = input("Podaj tytuł książki: ")
            if book_exists_by_title(title_of_new_book):
                print("Podana książka już istnieje w naszej bibliotece")
                print('-' * 30)
            else:
                add_book_to_library(title_of_new_book)
                print('-' * 30)
                
        elif user_choice == '4':
            borrow_book_handler()          

        elif user_choice == '0':
            clear_screen()
            print("Dziękujęmy, do zobaczenia")
            print('-' * 30)
            break
        else:
            clear_screen()
            print("Nie wybrano żadnej opcji, spróbuj ponownie")
            print('-' * 30)
            
library()