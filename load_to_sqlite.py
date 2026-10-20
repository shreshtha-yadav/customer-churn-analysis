import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "processed" / "telco_churn_cleaned.csv"
DB_PATH = BASE_DIR / "data" / "telco_churn.db"

# Read processed data
df = pd.read_csv(CSV_PATH)

# Write to SQLite
conn = sqlite3.connect(DB_PATH)
df.to_sql("telco_churn", conn, if_exists="replace", index=False)
conn.close()

print(f"Successfully loaded {len(df)} rows into {DB_PATH}")