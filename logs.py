import json
import uuid
from datetime import datetime
import os

class Log:
    def __init__(self, log_id, book_id, action_type, action_time, user_id):
        self.id = log_id or str(uuid.uuid4())
        self.book_id = book_id
        self.action_type = action_type
        self.action_time = action_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user_id = user_id

class LogsManager:
    def __init__(self, file_path = "storage/logs.json"):
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

    def add_new_log(self, book_id, action_type, user_id):
            new_log = Log(log_id=None, book_id=book_id, action_type=action_type, action_time=None, user_id=user_id)
            self.log_history.append(new_log)
            self.save_logs()