
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/processed/telco_churn_cleaned.csv")

print("===== DATASET VALIDATION =====")

# 1. Dataset dimensions
print("\nDataset shape:", df.shape)

# 2. Missing values
print("\nTotal missing values:", df.isnull().sum().sum())

# 3. Duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# 4. Churn distribution
print("\nChurn distribution:")
print(df["Churn"].value_counts())

print("\nChurn percentage:")
print(
    (df["Churn"].value_counts(normalize=True) * 100).round(2)
)

# 5. Numeric summary
print("\nNumerical summary:")
print(df[["tenure", "MonthlyCharges", "TotalCharges"]].describe())

print("\nValidation complete!")
