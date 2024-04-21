import sqlite3

def create_db():
    try:
        conn = sqlite3.connect('chat.db')  # Creates or opens a file called chat.db
        print("Database opened successfully.")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS messages
                    (sender TEXT, recipient TEXT, message TEXT, timestamp REAL)''')
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        print("Database connection is closed.")

if __name__ == "__main__":
    create_db()
