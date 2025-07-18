import json
from utils import *
import prettytable
from collections import Counter
from book import Book
from logs import LogsManager


class Library:
    def __init__(self, file_path='storage/books.json'):
        self.file_path = file_path
        self.books = self.load_books()
        self.logs_manager = LogsManager()

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
        self.logs_manager.add_new_log(new_book.id, "Dodano")

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

    def book_action_handler(self, action_type):
        clear_screen()
        if action_type == 'borrow':
            books = [book for book in self.books if not book.borrowed]
            action = 'wypożyczyć'
        else:
            books = [book for book in self.books if book.borrowed]
            action = 'zwrócić'

        self.display_books(books)
        selected_book = self.select_book(books)
        if selected_book:
            confirm = input(f'Chcesz {action} książkę "{selected_book.title}"? (tak/nie): ').lower()
            if confirm == 'tak':
                for book in self.books:
                    if book.id == selected_book.id:
                        if action_type == 'borrow':
                            book.borrow_book()
                            print(f'Książka została wypożyczona.')
                            self.logs_manager.add_new_log(selected_book.id, "Wypożyczono")
                        else:
                            book.return_book()
                            print(f'Książka została zwrócona.')
                            self.logs_manager.add_new_log(selected_book.id, "Zwrócono")
                
                self.save_books()
    
    def edit_book_data(self):
        self.display_books(self.books)
        seletced_book = self.select_book(self.books)
        if seletced_book:
            for index, element in enumerate(FILTERS_FOR_BOOKS, start=1):
                print(f'{index}. {FILTERS_FOR_BOOKS[element].title()}')
            print(f'Wybrana książka to: "{seletced_book.title}"')
            while True:
                user_choice = input(f"Który z elementów książki ma być zmienony? (podaj numer od 1 do {len(self.books)})(wprowadzenie 0 spowoduje opuszczenie opcji): ")
                if user_choice == '0':
                    print("")
                    return
                elif user_choice == '1':
                    seletced_book.change_property('title')
                    self.save_books()
                    break
                elif user_choice == '2':
                    seletced_book.change_property('author')
                    self.save_books()
                    break
                elif user_choice == '3':
                    seletced_book.change_property('year')
                    self.save_books()
                    break
                elif user_choice == '4':
                    seletced_book.change_property('genre')
                    self.save_books()
                    break
                else:
                    print("Podano niewłaściwą wartość")
            self.logs_manager.add_new_log(seletced_book.id, "Edytowano")

    def delete_book_from_library(self):
        self.display_books(self.books)
        seletced_book = self.select_book(self.books)
        if seletced_book:
            while True:
                user_choice = input(f"Czy książka {seletced_book.title} ma zostać usunięta z biblioteki? (wpisz tak/nie): ").lower()
                if user_choice == 'tak':
                    self.books.remove(seletced_book)
                    self.save_books()
                    print("Książka została usunięta z biblioteki.")
                    self.logs_manager.add_new_log(seletced_book.id, "Usunięto")
                    break
                elif user_choice == 'nie':
                    print(f'Książka "{seletced_book.title}" pozostanie w bibliotece.')
                    break
                else:
                    print('Proszę podać słowo "tak" lub "nie".')
                    
    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def display_logs(self, filter = None, limit = 10):
        logs_table = prettytable.PrettyTable()
        logs_table.field_names = ['Nr', 'Rodzaj akcji', 'Książka', 'Data']
        for index, log in enumerate(self.logs_manager.log_history[-limit:], start=1):
            book_title = self.get_book_by_id(log.book_id).title if self.get_book_by_id(log.book_id) else "[Usunięta książka]"
            logs_table.add_row([
                index,
                log.action_type,
                book_title,
                log.action_time
            ])
        print(logs_table)

    def logs_history_display_handler(self):
        clear_screen()
        print("Ostatnie 10 aktywności.")
        self.display_logs()
        print('1. Wyszukaj w historii zmian.')
        print('0. Wyjście z programu')

