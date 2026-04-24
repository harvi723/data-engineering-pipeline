import pandas as pd
from config import DATA_PATH

def extract_csv():
    try:
        df = pd.read_csv(DATA_PATH)
        print("CSV extracted successfully")
        return df
    except Exception as e:
        print("Error extracting CSV:", e)
        raise
