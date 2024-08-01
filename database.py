# # import mysql.connector as mc 
# # conn = mc.connect(host='localhost' , user='root' , password='975919')

# import sqlite3

# def create_db():
#     conn = sqlite3.connect('customer_satisfaction.db')
#     c = conn.cursor()
    
#     c.execute('DROP TABLE IF EXISTS customer_satisfaction')
    
#     c.execute('''
#         CREATE TABLE customer_satisfaction (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             age INTEGER,
#             flight_distance INTEGER,
#             inflight_entertainment INTEGER,
#             baggage_handling INTEGER,
#             cleanliness INTEGER,
#             departure_delay INTEGER,
#             arrival_delay INTEGER,
#             gender INTEGER,
#             customer_type INTEGER,
#             class TEXT,
#             type_of_travel INTEGER,
#             Class_Eco INTEGER DEFAULT 0,
#             Class_Eco_Plus INTEGER DEFAULT 0
#         )
#     ''')
    
#     conn.commit()
#     conn.close()

# create_db()


import sqlite3

DATABASE = 'customer_satisfaction.db'

def recreate_table():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Drop the table if it exists
        c.execute('DROP TABLE IF EXISTS customer_satisfaction')
        # Create the table with the correct schema
        c.execute('''
            CREATE TABLE customer_satisfaction (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age INTEGER,
                flight_distance INTEGER,
                inflight_entertainment INTEGER,
                baggage_handling INTEGER,
                cleanliness INTEGER,
                departure_delay INTEGER,
                arrival_delay INTEGER,
                gender INTEGER,
                customer_type INTEGER,
                travel_type INTEGER,
                class_type TEXT,
                Class_Eco INTEGER,
                Class_Eco_Plus INTEGER
            )
        ''')
        conn.commit()
        conn.close()
        print("Table recreated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    recreate_table()
