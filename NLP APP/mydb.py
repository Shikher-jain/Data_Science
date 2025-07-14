import json
from tkinter import messagebox
import os

class Database:
    def __init__(self):
        self.path = 'GUI/db.json'
        if not os.path.exists(self.path):
            with open(self.path, 'w') as wf:
                json.dump({}, wf)

    def add_data(self, name, email, password):
        with open(self.path, 'r') as rf:
            database = json.load(rf)

        if email in database:
            messagebox.showerror("Warning", "Email already registered.")
            return

        database[email] = [name, password]

        with open(self.path, 'w') as wf:
            json.dump(database, wf)
        messagebox.showinfo("Success", "Registration successful!")

    def search(self, email, password):
        with open(self.path, 'r') as rf:
            database = json.load(rf)

        if email in database and database[email][1] == password:
            return True
        return False
    
    def get_name(self, email):
        with open(self.path, 'r') as rf:
            database = json.load(rf)

        if email in database:
            return database[email][0]
        return None