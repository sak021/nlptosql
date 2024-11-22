import os
import time
import sqlite3
import pandas as pd


def connect_to_database(db_name: str):
    """
    Connects to an SQLite database. If the database does not exist, it creates one.
    
    Parameters:
        db_name (str): Name of the SQLite database file (e.g., 'weather.db').
    
    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    try:
        connection = sqlite3.connect(db_name)
        print(f"Connected to database '{db_name}'.")
        # Return the connection object
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database '{db_name}': {e}")
        return None


def get_data(query, db_name, create_db=False):
    if query:
        print(f"Database '{db_name}' found. Connecting...")

        # Read From DataBase
        s = time.time()
        conn = connect_to_database(db_name)
        df = pd.read_sql_query(query, conn)
        print(f"Data fetched in {time.time()-s} seconds")
        return df

    elif create_db:
        print(f"Database '{db_name}' does not exist. Creating a new one...")
        
        # Create DataBase
        s = time.time()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Weather_Data (
            id INTEGER PRIMARY KEY,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            weather TEXT NOT NULL,
            climate TEXT NOT NULL
        );
        """
        conn = connect_to_database(db_name)
        conn.execute(create_table_query)
        weather_data = pd.read_csv(os.environ['FILE_PATH'])
        weather_data.to_sql("Weather_Data", conn, if_exists="replace", index=False)
        print("Table 'Weather_Data' ensured.")
        print(f"Database created in {time.time()-s} seconds")
        return None



# if __name__ == "__main__":
#     data = get_data()
#     print(data)