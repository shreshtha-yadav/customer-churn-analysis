import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "telco_churn.db"
SQL_DIR = BASE_DIR / "sql"

def execute_query(filename):
    query_path = SQL_DIR / filename
    with open(query_path, "r") as f:
        query = f.read()

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()

    print(f"\n--- Output: {filename} ---")
    print(df.to_string(index=False))

if __name__ == "__main__":
    for file in sorted(SQL_DIR.glob("*.sql")):
        execute_query(file.name)