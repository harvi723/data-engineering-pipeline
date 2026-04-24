import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "students.csv")
DB_PATH = os.path.join(BASE_DIR, "scripts", "students.db")
API_URL = "https://jsonplaceholder.typicode.com/users"
