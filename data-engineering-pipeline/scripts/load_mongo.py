import pandas as pd
from pymongo import MongoClient
from config import DATA_PATH

def load_mongo():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["student_db"]
        col = db["students"]
        df = pd.read_csv(DATA_PATH)
        col.delete_many({})
        col.insert_many(df.to_dict(orient="records"))
        print("Data inserted into MongoDB")
    except Exception as e:
        print("Mongo load error:", e)
        raise

if __name__ == "__main__":
    load_mongo()
