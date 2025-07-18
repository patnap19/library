import uuid
from utils import *

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