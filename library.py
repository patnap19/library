import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BOOKS_FILE = 'books.json'

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
        'gatunek': category_of_new_book.title()
    }    
    library = load_books(BOOKS_FILE)
    library.append(new_book)
    with open(BOOKS_FILE, 'w',  encoding="utf-8") as file:
        json.dump(library, file, ensure_ascii=False, indent=4)
    
    print("Książka została dodana do biblioteki.")

def check_if_exist(phrase_to_check):
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
        
def print_book(book_to_print):
        print(f"\nTytuł: {book_to_print['tytuł']}")
        print(f"Autor: {book_to_print['autor']}")
        print(f"Rok wydania: {book_to_print['rok']}")
        print(f"Gatunek: {book_to_print['gatunek']}")
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

print("Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?")

while True:
    print("Wybierz opcję: ")
    print("1. Wyświetl wszystkie książki.")
    print("2. Wyszukaj książki.")
    print("3. Dodaj książkę.")
    print("0. Zakończ pracę.")
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
        if check_if_exist(title_of_new_book):
            print("Podana książka już istnieje w naszej bibliotece")
            print('-' * 30)
        else:
            add_book_to_library(title_of_new_book)

    elif user_choice == '0':
        clear_screen()
        print("Dziękujęmy, do zobaczenia")
        break
    else:
        clear_screen()
        print("Nie wybrano żadnej opcji, spróbuj ponownie")
        print('-' * 30)