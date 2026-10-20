
import pandas as pd

# Load the original dataset
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("Original shape:", df.shape)

# 1. Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# 2. Convert TotalCharges to numeric
# Invalid or blank values become NaN
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# 3. Check missing values after conversion
print("\nMissing values after conversion:")
print(df.isnull().sum())

# 4. Inspect rows with missing TotalCharges
missing_rows = df[df["TotalCharges"].isnull()]
print("\nRows with missing TotalCharges:")
print(missing_rows[["customerID", "tenure", "TotalCharges"]])

# 5. Remove duplicate records, if any
df = df.drop_duplicates()

# 6. Handle missing TotalCharges
# These customers have zero tenure, so their total charges
# can reasonably be represented as 0 for this dataset.
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# 7. Validate the cleaned data
print("\nCleaned shape:", df.shape)
print("\nData types:")
print(df.dtypes)

print("\nRemaining missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# 8. Save the cleaned dataset
df.to_csv(
    "data/processed/telco_churn_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
