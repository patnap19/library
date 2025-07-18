import json
import os
import prettytable
from collections import Counter
import uuid
from datetime import datetime

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

class Log:
    def __init__(self, log_id, book_id, action_type, action_time):
        self.id = log_id or str(uuid.uuid4())
        self.book_id = book_id
        self.action_type = action_type
        self.action_time = action_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class LogsManager:
    def __init__(self, file_path = "logs.json"):
        self.file_path = file_path
        self.log_history = self.load_logs()

    def load_logs(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return [Log(
                    log_id=log['id'],
                    book_id = log['book_id'],
                    action_type= log['action_type'],
                    action_time= log['action_time']
                ) for log in data]
            except json.JSONDecodeError:
                print("❌ Błąd przy wczytywaniu pliku logów.")
                return []

    def save_logs(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([log.__dict__ for log in self.log_history], file, ensure_ascii=False, indent=4)

    def add_new_log(self, book_id, action_type):
            new_log = Log(log_id=None, book_id=book_id, action_type=action_type, action_time=None)
            print(new_log)
            self.log_history.append(new_log)
            self.save_logs()


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
        
    def change_property(self, property_to_change):
        if property_to_change == 'year':
            new_value = get_valid_number(f"Podaj nowy {FILTERS_FOR_BOOKS[property_to_change]}, aktualnie to {getattr(self, property_to_change)}: ")
        else:
            new_value = get_valid_text(f"Podaj nowy {FILTERS_FOR_BOOKS[property_to_change]}:, aktualnie to {getattr(self, property_to_change)}: ")

        setattr(self, property_to_change, new_value)
        print(f"✅ Zmieniono {FILTERS_FOR_BOOKS[property_to_change]} na: {new_value}")


class Library:
    def __init__(self, file_path='books.json'):
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
                    
    def display_logs_history(self):
        pass

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            clear_screen()
            print("1. Pokaż książki\n2. Dodaj książkę\n3. Filtruj książki\n4. Statystyki\n5. Wypożycz książkę\n6. Zwróć książkę\n7. Edytuj książkę\n8. Usuń książkę\n0. Wyjście")
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
                self.library.display_logs_history()
            elif choice == "0":
                print("Do zobaczenia!")
                break
            else:
                print("❌ Niepoprawny wybór.")

            input("\nNaciśnij Enter, aby kontynuować...")

app = LibraryApp()
app.run()