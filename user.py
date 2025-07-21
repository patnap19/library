import uuid

class User:
    def __init__(self, user_id, user_name, user_surname, borrowed_books):
        self.id = user_id or str(uuid.uuid4())
        self.name = user_name
        self.surname = user_surname
        self.borrowed_books = borrowed_books or []
        
        
class UserBase:
    def __init__(self):
        pass