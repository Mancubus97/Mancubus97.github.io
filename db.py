import sqlite3
from sqlite3 import Connection
import json
from Models.Customer import Customer

class Database:
    def __init__(self):
        self.db = sqlite3.connect("./Data/Customers.db", check_same_thread=False)
        self.cur = self.db.cursor()



    def GetAdmins(self):
        admins = []
        self.cur.execute("SELECT voornaam FROM customers")
        accounts = self.cur.fetchall()
        for account in accounts:
            admins.append(account)
        return admins
    
    def Count_Customers(self):
        self.cur.execute("SELECT voornaam FROM customers")
        results = self.cur.fetchall()
        print(len(results))
        return len(results)
    
    def Get_All_Customers(self):
        customers = []
        self.cur.execute("SELECT * FROM customers")
        results = self.cur.fetchall()
        for result in results:
            customers.append(Customer(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        return customers


    def setup_customers_table(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
        table_exists = self.cur.fetchone()
        
        if not table_exists:
            self.cur.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY AUTOINCREMENT,voornaam TEXT NOT NULL,achternaam TEXT NOT NULL,telefoon TEXT NOT NULL,email TEXT,opmerkingen TEXT,aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP)")
            self.db.commit()

        else:
            pass
        if (self.Count_Customers() == 0):
            self.cur.execute("""
                INSERT INTO customers (voornaam, achternaam, telefoon, email, opmerkingen)
                VALUES (?, ?, ?, ?, ?)
            """, ("Jan", "de Vries", "0612345678", "jan.devries@gmail.com", "Knipt altijd kort"))

            self.cur.execute("""
                INSERT INTO customers (voornaam, achternaam, telefoon, email, opmerkingen)
                VALUES (?, ?, ?, ?, ?)
            """, ("Sanne", "Jansen", "0687654321", "sanne.jansen@hotmail.com", "Gevoelige hoofdhuid"))

            self.cur.execute("""
                INSERT INTO customers (voornaam, achternaam, telefoon, email, opmerkingen)
                VALUES (?, ?, ?, ?, ?)
            """, ("Mehmet", "Kaya", "0622334455", "mehmet.kaya@gmail.com", "Baard + haar"))

            self.db.commit()