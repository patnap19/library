import json
import os
import prettytable
from collections import Counter
import uuid
# from datetime import datetime

# def log_action(action, book_title):
#     log_history = load_file(LOG_HISTORY_FILE)
#     new_log = {
#         'time': datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
#         'action': action,
#         'book_title': book_title
#     }
#     log_history.append(new_log)
#     with open(LOG_HISTORY_FILE, 'w', encoding="utf-8") as file:
#         json.dump(log_history, file, ensure_ascii=False, indent=4)


# # def return_book(index_of_book):
# #     data = load_file(BOOKS_FILE)

# #     if 1 <= index_of_book <= len(data):
# #         book = data[index_of_book - 1]
# #         if not book['wypozyczona']:
# #             print("Ta książka nie jest wypożyczona.")
# #             return None
# #         data[index_of_book - 1]['wypozyczona'] = False
# #         save_books(data)
# #         return book
# #     else:
# #         print("Niepoprawny indeks książki.")
# #         return None
            
# def return_book_handler():
#     clear_screen()
#     all_books = load_file(BOOKS_FILE)
#     borrowed_books = [book for book in all_books if book['wypozyczona']]
#     if not borrowed_books:
#         print("Brak wypożyczonyhch książek.")
#         print('-' * 30)
#         return
#     print("Lista książek, które musisz zwrócić: ")
#     for i, book in enumerate(borrowed_books, 1):
#         print(f"{i}.")
#         print_book(book)

#     try:
#         user_input = int(input("Twój wybór: "))
#         if user_input < 1 or user_input > len(borrowed_books):
#             raise ValueError
#     except ValueError:
#         clear_screen()
#         print("Nieprawidłowy wybór. Wprowadź poprawny numer z listy.")
#         print('-' * 30)
#         return

#     selected_book = borrowed_books[user_input - 1]
#     original_index = all_books.index(selected_book)

#     clear_screen()
#     returned_book = return_book(original_index + 1)
#     if returned_book is None:
#         print("Przenosimy Cię do Menu Głównego")
#     else:
#         print("Zwróciłeś książkę")
#         log_action("Zwrócono", returned_book['tytuł'])
#         print_book(returned_book)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
FILTERS_FOR_BOOKS = {'title': 'tytuł',
    'author': 'autor', 
    'year': 'rok', 
    'genre': 'gatunek',
    'borrowed': 'wypożyczona'
}
    
def get_valid_text(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("❌ To pole nie może być puste. Spróbuj ponownie.")
        else:
            return user_input
        
def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("❌ To pole nie może być puste. Spróbuj ponownie.")
        elif not user_input.isdigit():
            print("❌ To pole powinno być liczbą. Spróbuj ponownie.")
        else:
            return int(user_input)

class Book:
    def __init__(self, title, author, year, genre, borrowed=False, book_id=None):
        self.id = book_id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.borrowed = borrowed

    def borrow_book(self):
        if self.borrowed:
            print("Książka jest już wypożyczona")
            return
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            print("Książka nie była wypożyczona")
            return
        self.borrowed = False

class Library:
    def __init__(self, file_path='books.json'):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return [Book(
                    title=book['title'],
                    author=book['author'],
                    year=book['year'],
                    genre=book['genre'],
                    borrowed=book['borrowed'],
                    book_id=book.get('id')
                ) for book in data]
            except json.JSONDecodeError:
                print("❌ Błąd przy wczytywaniu pliku książek.")
                return []

    def filter_by_field(self, books, field):
        prompt = f"Filtruj wg {FILTERS_FOR_BOOKS[field]} (pozostaw puste, aby pominąć): "
        value = input(prompt).strip()

        if not value:
            return books

        if field == 'borrowed':
            value = value.lower()
            if value not in ['tak', 'nie']:
                print("❌ Wpisz 'tak' lub 'nie'. Pominięto ten filtr.")
                return books
            expected = value == 'tak'
            return [book for book in books if book.borrowed == expected]

        if field == 'year':
            if not value.isdigit():
                print("❌ Rok musi być liczbą. Pominięto ten filtr.")
                return books
            return [book for book in books if book.year == int(value)]

        return [book for book in books if value.lower() in getattr(book, field).lower()]

    def save_books(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'genre': book.genre,
                    'borrowed': book.borrowed
                } for book in self.books
            ], file, ensure_ascii=False, indent=4)

    def display_books(self, books_to_display):
        table_with_books = prettytable.PrettyTable()
        table_with_books.field_names = ['Nr', 'Tytuł', 'Autor', 'Rok wydania', 'Gatunek', 'Wypożyczona']

        for index, book in enumerate(books_to_display, start=1):
            table_with_books.add_row([
                index,
                book.title,
                book.author,
                book.year,
                book.genre,
                'Tak' if book.borrowed else 'Nie'
            ])
            table_with_books.add_divider()

        print(table_with_books)

    def print_all_books(self):
        clear_screen()
        if self.books:
            self.display_books(self.books)
        else:
            print("Brak książek w bibliotece.")


    def add_book_to_library(self):
        clear_screen()
        title_of_new_book = get_valid_text("Podaj tytuł książki: ")
        author_of_new_book = get_valid_text("Podaj nazwisko autora: ")
        year_of_new_book = get_valid_number("Podaj rok wydania książki: ")
        genre_of_new_book = get_valid_text("Podaj gatunek książki: ")
        new_book = Book(title= title_of_new_book, author= author_of_new_book, year= year_of_new_book, genre= genre_of_new_book)
        self.books.append(new_book)
        self.save_books()
        print(f"Książka {title_of_new_book} została dodana do biblioteki")

    def show_stats(self):
        clear_screen()
        borrowed_books = sum(book.borrowed for book in self.books)
        all_books = len(self.books)
        available_books = all_books - borrowed_books
        the_most_books_author = Counter(book.author for book in self.books)

        print(f"📚 Łączna liczba książek: {all_books}")
        print(f"✅ Dostępnych: {available_books}")
        print(f"📕 Wypożyczonych: {borrowed_books}\n")

        if the_most_books_author:
            max_count = max(the_most_books_author.values())
            top_authors = [author for author, count in the_most_books_author.items() if count == max_count]

            print(f"Autorzy z największą liczbą książek ({max_count} książek):")
            for author in top_authors:
                print(f"- {author}")
        else:
            print("Brak danych o autorach.")

    def filter_books(self):
        books_to_filter = self.books
        for field in FILTERS_FOR_BOOKS:
            books_to_filter = self.filter_by_field(books_to_filter, field)

        clear_screen()
        if books_to_filter:
            print("📘 Wyniki filtrowania:")
            self.display_books(books_to_filter)
        else:
            print("❌ Nie znaleziono książek pasujących do wszystkich filtrów.")
            
    def select_book(self, books_list):
        while True:
            try:
                user_choice = int(input(f"Wybierz książkę wprowadzając numer książki od 1 do {len(books_list)} (wprowadzenie 0 spowoduje opuszczenie opcji): "))
                if 1 <= user_choice <= len(books_list):
                    return books_list[user_choice - 1]
                elif user_choice == 0:
                    return None
                else:
                    print("Podano niewłaściwy numer książki, spróbuj ponownie.")
            except ValueError:
                print('Nie podano numeru, pod którym znajduje się książka. Spróbuj ponownie')

    def borrow_book_handler(self):
        clear_screen()
        available_books = [book for book in self.books if not book.borrowed]
        self.display_books(available_books)
        selected_book = self.select_book(available_books)
        if selected_book:
            while True:
                user_decision = input(f'Chcesz wypożyczyć następującą książkę\n "{selected_book.title}", której autorem jest: {selected_book.author}. Jesteś pewien(wpisz tak/nie?): ').lower()
                if user_decision == 'tak':
                    for book in self.books:
                        if selected_book.id == book.id:
                            book.borrow_book()
                    print(f'Książka "{selected_book.title}" została wypożyczona')
                    self.save_books()
                    return
                elif user_decision == 'nie':
                    print("Nie wybrano książki")
                    break
                else:
                    print("Podano niewłaściwy wyraz, spróbuj ponownie.")
                    
    def return_book_handler(self):
        clear_screen()
        borrowed_books = [book for book in self.books if book.borrowed]
        self.display_books(borrowed_books)
        selected_book = self.select_book(borrowed_books)
        if selected_book:
            while True:
                user_decision = input(f'Chcesz zwrócić następującą książkę\n "{selected_book.title}", której autorem jest: {selected_book.author}. Jesteś pewien(wpisz tak/nie?): ').lower()
                if user_decision == 'tak':
                    for book in self.books:
                        if selected_book.id == book.id:
                            book.return_book()
                    print(f'Książka "{selected_book.title}" została zwrócona')
                    self.save_books()
                    return
                elif user_decision == 'nie':
                    print("Nie wybrano książki")
                    break
                else:
                    print("Podano niewłaściwy wyraz, spróbuj ponownie.")

class LibraryApp:
    def __init__(self):
        self.library = Library()
        
    def run(self):
        while True:
            clear_screen()
            print("1. Pokaż książki\n2. Dodaj książkę\n3. Filtruj książki\n4. Statystyki\n5. Wypożycz książkę\n6. Zwróć książkę\n0. Wyjście")
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
                self.library.borrow_book_handler()
            elif choice == '6':
                self.library.return_book_handler()
            elif choice == "0":
                print("Do zobaczenia!")
                break
            else:
                print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")

app = LibraryApp()
app.run()