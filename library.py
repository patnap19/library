import json

BOOKS_FILE = 'books.json'

def load_books(file_path=BOOKS_FILE):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def print_all_books():
    data = load_books(BOOKS_FILE)

    for book in data:
        print_book(book)
        
def print_book(book_to_print):
        print(f"\nTytuł: {book_to_print['tytuł']}")
        print(f"Autor: {book_to_print['autor']}")
        print(f"Rok wydania: {book_to_print['rok']}")
        print(f"Gatunek: {book_to_print['gatunek']}")
        print('-' * 30)
        
def find_book(area_of_search):
    phrase_to_find = input('Podaj frazę do wyszukiwania: ').lower()
    data = load_books(BOOKS_FILE)
    found = False
    for book in data:
        if phrase_to_find in str(book[area_of_search]).lower():
            found = True
            print_book(book)
    if not found:
        print("Niestety nie odnaleźliśmy żadnej książki pasującej do podanej przez Ciebie frazy.")

print("Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?")

while True:
    print("1.Wyświetl wszystkie dostępne książki w naszej bibliotece.")
    print("2. Wyszukaj książki po autorze.")
    print("0. Zakończ pracę.")
    user_choice = input("Twój wybór: ")

    if user_choice == '1':
        print_all_books()
    elif user_choice == '2':
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
            
        

    elif user_choice == '0':
        print("Dziękujęmy, do zobaczenia")
        break
    else:
        print("Nie wybrano żadnej opcji, spróbuj ponownie")