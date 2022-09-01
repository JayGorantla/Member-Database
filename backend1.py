import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS member (id INTEGER PRIMARY KEY, name text, team text, exp integer, spec text)")
        self.conn.commit()
    
    def insert(self, name, team, exp, spec):
        self.cur.execute("INSERT INTO member VALUES (NULL, ?, ?, ?, ?)", (name, team, exp, spec))
        self.conn.commit()
    
    def view(self):
        self.cur.execute("SELECT * FROM member")
        rows = self.cur.fetchall()
        return rows
    
    def search(self, name = "", team = "", exp = "", spec = ""):
        self.cur.execute("SELECT * FROM member WHERE name = ? OR team = ? OR exp = ? OR spec = ?", (name, team, exp, spec))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM member WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, name, team, exp, spec):
        self.cur.execute("UPDATE member SET name = ?, team = ?, exp = ?, spec = ? WHERE id = ?", (name, team, exp, spec, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        
