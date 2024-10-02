import sqlite3


connect = sqlite3.connect("Users.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30)
    )
""")

connect.commit()
connect.close()
    
class DataBaseManager:
    def __init__(self, name):
        self.name = name
        
    def open():
        connect.commit()
        
    def close():
        connect.close()
        
    
        
        
class User:
    def add_user(self, name):
        self.name = name
        name = input("Введите имя: ")
        cursor.execute("""INSERT INTO users
                       (name)""", (name))
        connect.commit()
     
        
    def check_user(self):
           cursor.execute("""SELECT * FROM users""")
           user = cursor.fetchall()
           connect.commit()
           print(user)
     
           
    def delete_user(self, name):
           cursor.execute("""DELETE FROM users WHERE id = ?""", (name))
           connect.commit()
           

class Admin(User):
    def __init__(self, admins):
        self.admins = admins
        
        
class Customer(User):
    def __init__(self, customers):
        self.customers = customers
        
        

"Не смогу сделать. Не хорошо готовился"