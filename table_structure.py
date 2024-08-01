import sqlite3

DATABASE = 'customer_satisfaction.db'

def alter_table():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Add the missing column
        c.execute('ALTER TABLE customer_satisfaction ADD COLUMN travel_type INTEGER')
        conn.commit()
        conn.close()
        print("Table altered successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    alter_table()
