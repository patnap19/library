import uuid
import hashlib
import os
import json
from utils import *

class User:
    def __init__(self, user_id, login, password, user_name, user_surname, borrowed_books, is_admin):
        self.id = user_id or str(uuid.uuid4())
        self.login = login
        self.password = password
        self.name = user_name
        self.surname = user_surname
        self.borrowed_books = borrowed_books or []
        self.is_admin = is_admin
        
    def borrow_book(self, book_id):
        print('TU WCHODZIMY')
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            print(f"Książka została wypożyczona.")
        else:
            print("Książka jest już przez Ciebie wypożyczona.")
    
    def return_book():
        pass
    
    def change_data():
        pass

class UsersManager:
    def __init__(self, file_path = 'storage/users.json'):
        self.file_path = file_path
        self.users_list = self.load_users()

    def load_users(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return [User(
                    user_id=user['id'],
                    login = user['login'],
                    user_name=user['name'],
                    user_surname=user['surname'],
                    password=user['password'],
                    borrowed_books=user.get('borrowed_books', []),
                    is_admin = user['is_admin']
                ) for user in data]
            except json.JSONDecodeError:
                print("❌ Błąd przy wczytywaniu pliku użytkowników.")
                return []
        
    def save_users(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([
                {
                    'id': user.id,
                    'login': user.login,
                    'name': user.name,
                    'surname': user.surname,
                    'password': user.password,
                    'borrowed_books': user.borrowed_books,
                    'is_admin': user.is_admin
                } for user in self.users_list
            ], file, ensure_ascii=False, indent=4)

    def create_user(self):
        print("Witamy w oknie, umożliwiającym utworzenie nowego użytkownika.")
        new_user_login = get_valid_text("Podaj nazwę użytkownika: ")
        new_user_name = get_valid_text("Podaj imię użytkownika: ")
        new_user_surname = get_valid_text("Podaj nazwisko użytkownika: ")
        new_user_password = get_valid_text("Podaj hasło: ")
        new_user = User(user_id= None, login=new_user_login ,user_name= new_user_name, user_surname= new_user_surname, password= new_user_password, borrowed_books= [], is_admin= False)
        self.users_list.append(new_user)
        self.save_users()
        print(f"Użytkownik {new_user_name.title()} {new_user_surname.title()} został dodany.")
        
    def delete_user(self, user_to_delete):
        pass
        
    def find_user(self):
        print("Znaleziono użytkownika")
        
    def edit_user(self):
        print("Zmieniono dane")
        
    def log_user(self):
        pass
    
    def logout_user():
        pass
    
    def display_all_users():
        pass
    
    def change_permissons():
        pass
    
        #TODO Przy tworzeniu użytkownika przez admina hasło jest ustawiane losowe, które użytkownik może po pierwszym logowaniu zmienić. Jeżeli użytkownik sam się bedzie 
        #rejestrował, ustawia samodzielnie hasło
        # Sprawdzenie, czy użytkownik w bazie danych istnieje, zapytanie czy to ta sama osoba, jeżeli nie utwrozenie nowego konta.