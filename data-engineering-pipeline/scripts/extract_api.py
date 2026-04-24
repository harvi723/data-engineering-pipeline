import requests
import pandas as pd
from config import API_URL

def extract_api():
    try:
        res = requests.get(API_URL, timeout=10)
        res.raise_for_status()
        data = res.json()
        df = pd.DataFrame(data)
        # normalize nested city
        if 'address' in df.columns:
            df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
        return df[['id','name','email','city']]
    except Exception as e:
        print("API extraction error:", e)
        raise

if __name__ == "__main__":
    print(extract_api().head())
