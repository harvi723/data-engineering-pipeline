import pandas as pd

def add_grade(m):
    if m > 85:
        return 'A'
    elif m > 70:
        return 'B'
    else:
        return 'C'

def transform(df: pd.DataFrame):
    try:
        df = df.copy()
        df['grade'] = df['marks'].apply(add_grade)
        return df
    except Exception as e:
        print("Error transforming data:", e)
        raise
