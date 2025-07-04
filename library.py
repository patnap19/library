import json

# with open('books.json', 'r', encoding="utf-8") as file:
#     data = json.load(file)

# print(data[0])

def print_all_books(file_to_open):
    with open(file_to_open, 'r', encoding="utf-8") as file:
        data = json.load(file)

    for book in data:
        print_book(book)
        
def print_book(book_to_print):
        print(f"Tytuł: {book_to_print['tytuł']}")
        print(f"Autor: {book_to_print['autor']}")
        print(f"Rok wydania: {book_to_print['rok']}")
        print(f"Gatunek: {book_to_print['gatunek']}")
        print('-' * 30)

print("Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?\n")
while True:
    print("1.Wyświetl wszystkie dostępne książki w naszej bibliotece.\n")
    print("2. Wyszukaj książki po autorze.\n")
    print("0. Zakończ pracę.\n")
    user_choice = input("Twój wybór: ")

    if user_choice == '1':
        print_all_books('books.json')
    elif user_choice == '2':
        author_to_find = input('Którego autora chcesz odnaleźć?: ').lower()
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
        found = False
        for book in data:
            if author_to_find in book['autor'].lower():
                found = True
                print_book(book)
        if not found:
            print("Niestety nie odnaleźliśmy żadnej książki podanego przez Ciebie autora.")
    elif user_choice == '0':
        print("Dziękujęmy, do zobaczenia")
        break
    else:
        print("Nie wybrano żadnej opcji, spróbuj ponownie")