-- Service and add-on driver analysis
SELECT 
    InternetService,
    TechSupport,
    OnlineSecurity,
    COUNT(customerID) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(customerID), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge
FROM telco_churn
GROUP BY InternetService, TechSupport, OnlineSecurity
ORDER BY total_customers DESC;