import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, pet, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (pet, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, pet, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (pet, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# import sqlite3

# class Database:
#     def __init__(self, db):
#        self.conn = sqlite3.connect(db)
#        self.cur = self.conn.cursor()
#        self.cur.execute("CREATE TABLE IF NOT EXISTS supplies (id INTEGER PRIMARY KEY, pet text, customer text, retailer text, price text")
#        self.conn. commit()

#     def fetch(self):
#         self.cur.execute("SELECT * FROM pet")
#         rows = self.cur.fetchall()
#         return rows

#     def insert(self, pet, customer, retailer, price):
#         self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (pet, customer, retailer, price))
#         self.conn.commit()

#     def remove(self, id):
#         self.cur.execute("DELETE FROM pet WHERE id=?", (id,))
#         self.conn.commit()

#     def update(self, id, pet, customer, retailer, price):
#         self.cur.execute("UPDATE pet SET pet = ?, customer = ?, retailer = ?, price = ? WHERE id = ?", (pet, customer, retailer, price, id))
#         self.conn.commit()

#     def __del__(self):
#         self.conn.close()
        
# db = Database('store.db')
# db.insert("Rope Toy", "John Jake", "PetCo", "20")