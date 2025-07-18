import os

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