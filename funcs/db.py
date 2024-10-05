import sqlite3

class Database():
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    #будут запросы
    def register_user(self, user_id):
        with self.connection: 
            self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def is_register(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT user_id FROM users").fetchall()
            new_list = []

            for tuple in res:
                element = tuple[0]
                new_list.append(element)

            if user_id in new_list:
                return False
            else: 
                return True
            

    def add_name(self, user_id, name):
        with self.connection:
            self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id,))

    def add_old(self, user_id, years):
        with self.connection:
            self.cursor.execute("UPDATE users SET old = ? WHERE user_id = ?", (years, user_id,))

    def add_phone(self, user_id, numder):
        with self.connection:
            self.cursor.execute("UPDATE users SET phone = ? WHERE user_id = ?", (numder, user_id,))