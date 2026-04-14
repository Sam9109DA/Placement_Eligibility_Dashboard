
import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="placement_eligibility_db"
            )
            self.cursor = self.conn.cursor()
            print("Database connection established.")
            return self.conn, self.cursor
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            return None, None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
