import uuid

#Może wykorzystać base64 dla password?
class User:
    def __init__(self, user_id, user_name, user_surname, password, borrowed_books):
        self.id = user_id or str(uuid.uuid4())
        self.name = user_name
        self.surname = user_surname
        self.password = password
        self.borrowed_books = borrowed_books or []
        
    def borrow_book():
        pass
    
    def return_book():
        pass

class UsersManager:
    def __init__(self, file_path = 'storage/users.json'):
        self.file_path = file_path
        self.users_list = self.load_users()

    def load_users(self):
        print("DUPA")
        
    def save_users(self):
        print("zapisano")
    def check_password(self): #Czy spełnia wymogi
        print("sprawdzamy hasło")

    def create_user(self):
        print("Dodano użytkownia")
        
    def delete_user(self):
        print("Usunięto użytkownika")
        
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
        
    