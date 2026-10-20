-- Churn breakdown by customer tenure cohorts and contract type
WITH customer_cohorts AS (
    SELECT 
        customerID,
        Contract,
        MonthlyCharges,
        Churn,
        CASE 
            WHEN tenure <= 12 THEN '0-12 Months'
            WHEN tenure <= 24 THEN '13-24 Months'
            WHEN tenure <= 48 THEN '25-48 Months'
            ELSE '49-72 Months'
        END AS tenure_cohort
    FROM telco_churn
)
SELECT 
    tenure_cohort,
    Contract,
    COUNT(customerID) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(customerID), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM customer_cohorts
GROUP BY tenure_cohort, Contract
ORDER BY 
    CASE tenure_cohort
        WHEN '0-12 Months' THEN 1
        WHEN '13-24 Months' THEN 2
        WHEN '25-48 Months' THEN 3
        ELSE 4
    END,
    churn_rate_pct DESC;