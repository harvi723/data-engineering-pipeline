import time, random, sqlite3
from config import DB_PATH

def stream():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    while True:
        marks = random.randint(60, 100)
        grade = 'A' if marks>85 else ('B' if marks>70 else 'C')
        cur.execute("INSERT INTO students (name, department, marks, grade) VALUES (?, ?, ?, ?)",
                    ("LiveUser", "IT", marks, grade))
        conn.commit()
        print("Inserted row:", marks, grade)
        time.sleep(3)

if __name__ == "__main__":
    stream()
