# Telco Customer Churn & Retention Analysis

An end-to-end data analytics and business intelligence project evaluating subscriber retention patterns, revenue vulnerability, and risk cohorts using Python, SQL, and Tableau.

🔗 Interactive Tableau Dashboard: [View Live Executive Dashboard on Tableau Public](https://public.tableau.com/app/profile/shreshtha.yadav/viz/CustomerChurnRetentionAnalysis_17924450644480/Dashboard1)

---

## 📌 Executive Summary

Customer attrition directly threatens predictable Monthly Recurring Revenue (MRR). This analysis evaluates 7,043 subscriber records from the IBM Telco dataset to diagnose the core drivers of customer churn, quantify the financial impact of customer loss, and develop data-driven retention strategies for business stakeholders.

### Key Performance Indicators (KPIs)
* Total Customer Base: 7,043 subscribers
* Overall Churn Rate: 26.54% (1,869 churned customers)
* Monthly Revenue at Risk: $139,130.85 lost monthly (30.50% of total company MRR)
* Average Revenue Per User (ARPU): Overall ARPU is $64.76, whereas churned accounts average $74.44, proving attrition is heavily concentrated among higher-paying tiers.
* Highest-Risk Profile: Month-to-month subscribers with Fiber Optic service and no Tech Support/Online Security (churn rate: 55.01%).
* Strongest Retention Anchor: Two-year contract commitments reduce churn to **2.19%–3.33%** across all tenure bands.

---

## 🛠 Tech Stack & Tools

* Python & Pandas: Data ingestion, schema inspection, missing value handling, datatype casting, and exploratory analysis.
* Matplotlib & Seaborn: Statistical distribution plots and correlation visualizations.
* SQL (ANSI / SQLite): Modular analytical scripts utilizing Common Table Expressions (CTEs), `CASE WHEN` conditional aggregations, and window functions.
* Tableau Public: Production-grade interactive executive dashboard with dynamic KPI cards, cohort breakdowns, and cross-filtering.

---

## 📂 Project Architecture

```text
customer-churn-analysis/
├── data/
│   ├── processed/
│   │   └── telco_churn_cleaned.csv            # Cleaned, analysis-ready dataset
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv # Original raw dataset
│   └── telco_churn.db                         # Relational SQLite database
├── notebooks/
│   └── churn_analysis.ipynb                   # Jupyter notebook for deep-dive exploration
├── sql/
│   ├── 01_executive_kpis.sql                  # Overarching retention & MRR impact metrics
│   ├── 02_cohort_retention.sql                # Tenure cohorts cross-analyzed with contracts
│   ├── 03_service_churn_drivers.sql           # Internet service & tech support risk drivers
│   └── 04_customer_segmentation.sql           # Customer loyalty and risk tiering
├── tableau/                                   # Tableau workbook assets
├── visuals/                                   # Exported charts from EDA pipeline
│   ├── churn_by_contract.png
│   ├── churn_by_monthly_charges.png
│   ├── churn_by_tenure.png
│   ├── churn_distribution.png
│   ├── monthly_charges_by_churn.png
│   └── tenure_vs_monthly_charges.png
├── clean_data.py                              # Data transformation & type handling script
├── eda.py                                     # Exploratory data analysis & figure generator
├── inspect_data.py                            # Initial schema & null value diagnostic
├── load_to_sqlite.py                          # Ingestion script from CSV into SQLite DB
├── run_sql.py                                 # Automated SQL query execution runner
├── validate_data.py                           # Post-cleaning data integrity verification
├── requirements.txt                           # Python dependencies
└── README.md
```

---

## 🔄 End-to-End Pipeline & Methodology

| Stage | Script/Asset | Purpose |
| :--- | :--- | :--- |
| 1. Ingestion & Diagnostic | `inspect_data.py` | Audited schema datatypes and detected 11 whitespace strings in `TotalCharges` causing improper object classification. |
| 2. Cleaning & Transformation | `clean_data.py` | Imputed `TotalCharges` with 0 for new customers (`tenure = 0`), cast numerical types, and standardized categoricals. |
| 3. Quality Assurance | `validate_data.py` | Enforced strict schema constraints and confirmed zero null or unmapped values remained. |
| 4. Exploratory Data Analysis | `eda.py` | Conducted bivariate and correlation analyses, generating distribution visuals exported to `/visuals`. |
| 5. Relational Database Modeling | `load_to_sqlite.py` | Automated schema creation and batch ingested processed records into `telco_churn.db`. |
| 6. SQL Analytical Engine | `run_sql.py` & `/sql` | Executed modular queries evaluating tenure cohorts, support driver dependencies, and RFM-style segmentation. |
| 7. BI Dashboarding | Tableau Public | Built an executive dashboard linking high-level revenue KPIs directly to operational retention levers. |

---

## 📊 Key Analytical Findings

### 1. Contract & Tenure Cohorts (`02_cohort_retention.sql`)
* First-Year Vulnerability: Month-to-month subscribers in their first 12 months exhibit a **51.35%** churn rate.
* Tenure Buffer: Retention steadily improves over time; customers beyond 48 months drop to 26.02% churn on month-to-month agreements, while 2-year contracts drop churn to **3.33%**.

### 2. Service & Add-On Friction (`03_service_churn_drivers.sql`)
* Subscribers with **Fiber Optic** internet who lack **Tech Support** and **Online Security** churn at **55.01%**, with high monthly bills averaging $86.10.
* Adding Tech Support and Online Security reduces churn to **14.17%**, confirming that post-sales technical support directly drives product retention.

### 3. Customer Loyalty & Risk Segmentation (`04_customer_segmentation.sql`)
| Customer Segment | Criteria                                       | Customer Count  | Churn Rate (%)     | Avg Monthly Charges |
|  :---            | :---                                           | :---            | :---               | :---                |
| High-Risk New    | Tenure < 24 mos, Month-to-month, Charges ≥ $70 | 1,256           | **62.90%**         | $84.40              |
| Standard         | Balanced tenure & usage profiles               | 1,860           | **27.85%**         | $39.61              |
| Champion         | Tenure ≥ 24 mos, Charges ≥ $70                 | 2,274           | **20.80%**         | $93.53              |
| Loyal            | Tenure ≥ 24 mos, Charges < $70                 | 1,653           | **5.32%**          | $38.56              |

---

## 💡 Strategic Business Recommendations

1. **Onboarding Tech Support Bundling:** Bundle 6 months of complimentary Tech Support and Online Security with every new Fiber Optic activation to protect accounts during the highest-risk window.
2. **First-Year Contract Incentive Program:** Trigger automated discount or upgrade campaigns at Month 3 and Month 6 targeting month-to-month subscribers to transition them into 1-year agreements.
3. **Autopay Migration:** Incentivize Electronic Check customers (who experience high churn) to migrate to automated bank drafts or credit card payments with a small monthly billing credit.

---

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/customer-churn-analysis.git
cd customer-churn-analysis
```

### 2. Set Up the Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Data Pipeline
```bash
# Data quality & cleaning
python inspect_data.py
python clean_data.py
python validate_data.py

# Exploratory visualizations
python eda.py
```

### 4. Run the SQL Analytics Engine
```bash
# Load data into SQLite
python load_to_sqlite.py

# Execute all business queries
python run_sql.py
```