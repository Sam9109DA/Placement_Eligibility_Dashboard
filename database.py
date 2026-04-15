import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect("placement.db")
            self.cursor = self.conn.cursor()
            print("SQLite database connected.")
            return self.conn, self.cursor
        except Exception as err:
            print(f"Error connecting to database: {err}")
            return None, None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
