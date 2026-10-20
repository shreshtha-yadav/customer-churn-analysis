
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Folder for saved charts
BASE_DIR = Path(__file__).resolve().parent
VISUALS_DIR = BASE_DIR / "visuals"
VISUALS_DIR.mkdir(exist_ok=True)

# Load cleaned data
df = pd.read_csv("data/processed/telco_churn_cleaned.csv")

# Count customers in each churn category
churn_counts = df["Churn"].value_counts()

print("Customer churn counts:")
print(churn_counts)

# Create a bar chart
plt.figure(figsize=(7, 5))

churn_counts.plot(
    kind="bar",
    color=["steelblue", "tomato"],
    edgecolor="black"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/ "churn_distribution.png", 
    dpi=300,
    bbox_inches="tight")
plt.show()


#################################


# Churn rate by contract type

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print("\nChurn rate by contract type:")
print(contract_churn.round(2))

# Plot churn percentages
contract_churn.plot(
    kind="bar",
    figsize=(9, 5),
    color=["steelblue", "tomato"],
    edgecolor="black"
)

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Percentage of Customers (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/ "churn_by_contract.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


###################################

# Churn rate by customer tenure group

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=[
        "0-12 months",
        "13-24 months",
        "25-48 months",
        "49-72 months"
    ]
)

tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

print("\nChurn rate by tenure group:")
print(tenure_churn.round(2))

tenure_churn.plot(
    kind="bar",
    figsize=(9, 5),
    color=["steelblue", "tomato"],
    edgecolor="black"
)

plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Percentage of Customers (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/ "churn_by_tenure.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#############################


# Monthly charges comparison by churn status

charges_summary = df.groupby("Churn")[
    "MonthlyCharges"
].agg(["mean", "median", "count"])

print("\nMonthly charges by churn status:")
print(charges_summary.round(2))

# Box plot comparison
df.boxplot(
    column="MonthlyCharges",
    by="Churn",
    figsize=(8, 5)
)

plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges ($)")
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/ "monthly_charges_by_churn.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

######################################

# Relationship between tenure and monthly charges

plt.figure(figsize=(9, 6))

for status, color in [("No", "steelblue"), ("Yes", "tomato")]:
    subset = df[df["Churn"] == status]

    plt.scatter(
        subset["tenure"],
        subset["MonthlyCharges"],
        label=f"Churn: {status}",
        alpha=0.4,
        s=18,
        color=color
    )

plt.title("Tenure vs Monthly Charges by Churn Status")
plt.xlabel("Tenure (months)")
plt.ylabel("Monthly Charges ($)")
plt.legend()
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/  "tenure_vs_monthly_charges.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

##########################################

# Churn rate by monthly charge group

df["ChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 35, 65, 90, float("inf")],
    labels=[
        "Low ($0–35)",
        "Medium ($35–65)",
        "High ($65–90)",
        "Very High ($90+)"
    ],
    include_lowest=True
)

charge_churn = pd.crosstab(
    df["ChargeGroup"],
    df["Churn"],
    normalize="index"
) * 100

print("\nChurn rate by monthly charge group:")
print(charge_churn.round(2))

# Visualize churn rates
charge_churn.plot(
    kind="bar",
    y="Yes",
    legend=False,
    figsize=(9, 5),
    color="tomato",
    edgecolor="black"
)

plt.title("Churn Rate by Monthly Charges")
plt.xlabel("Monthly Charge Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

plt.savefig(
    VISUALS_DIR/ "churn_by_monthly_charges.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#####################################

# Analyse churn by contract type and tenure together

contract_tenure_analysis = (
    df.groupby(["Contract", "TenureGroup"], observed=True)
    .agg(
        TotalCustomers=("Churn", "size"),
        ChurnedCustomers=("Churn", lambda x: (x == "Yes").sum()),
        ChurnRate=("Churn", lambda x: (x == "Yes").mean() * 100)
    )
    .reset_index()
)

print("\nChurn by Contract Type and Tenure:")
print(contract_tenure_analysis.round(2).to_string(index=False))

###########################################

# Churn rate by payment method
payment_churn = (
    df.groupby("PaymentMethod")
      .agg(
          TotalCustomers=("Churn", "size"),
          ChurnedCustomers=("Churn", lambda x: (x == "Yes").sum())
        )
)

payment_churn["ChurnRate"] = (
    payment_churn["ChurnedCustomers"]
    / payment_churn["TotalCustomers"] * 100
).round(2)

payment_churn = payment_churn.sort_values(
    "ChurnRate", ascending=False
)

print("Churn by Payment Method:")
print(payment_churn)

##################################################

payment_contract_churn = (
    df.groupby(["Contract", "PaymentMethod"])["Churn"]
      .agg(
          TotalCustomers="count",
          ChurnedCustomers=lambda x: (x == "Yes").sum()
      )
      .reset_index()
)

payment_contract_churn["ChurnRate"] = (
    payment_contract_churn["ChurnedCustomers"]
    / payment_contract_churn["TotalCustomers"] * 100
).round(2)

print(payment_contract_churn.to_string(index=False))

df[
    (df["Contract"] == "Two year") &
    (df["PaymentMethod"] == "Mailed check")
]["Churn"].value_counts()

#############################################

# Churn by customer tenure
tenure_churn = (
    df.groupby("TenureGroup")
      .agg(
          TotalCustomers=("Churn", "size"),
          ChurnedCustomers=("Churn", lambda x: (x == "Yes").sum())
      )
)

tenure_churn["ChurnRate"] = (
    tenure_churn["ChurnedCustomers"]
    / tenure_churn["TotalCustomers"] * 100
).round(2)

print("Churn by Tenure Group:")
print(tenure_churn)

internet_churn = (
    df.groupby("InternetService")
      .agg(
          TotalCustomers=("Churn", "size"),
          ChurnedCustomers=("Churn", lambda x: (x == "Yes").sum())
      )
)

internet_churn["ChurnRate"] = (
    internet_churn["ChurnedCustomers"]
    / internet_churn["TotalCustomers"] * 100
).round(2)

print("Churn by Internet Service:")
print(internet_churn)

######################################

internet_charges = (
    df.groupby("InternetService")
      .agg(
          TotalCustomers=("customerID", "count"),
          AverageMonthlyCharges=("MonthlyCharges", "mean"),
          MedianMonthlyCharges=("MonthlyCharges", "median")
      )
      .round(2)
)

print("Monthly Charges by Internet Service:")
print(internet_charges)

print(internet_charges.to_string())