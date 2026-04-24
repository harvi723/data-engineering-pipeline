import sqlite3
from extract import extract_csv
from transform import transform
from config import DB_PATH

def load_sqlite():
    try:
        conn = sqlite3.connect(DB_PATH)
        df = transform(extract_csv())
        df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()
        print("Data loaded into SQLite successfully")
    except Exception as e:
        print("Error loading into SQLite:", e)
        raise

if __name__ == "__main__":
    load_sqlite()
