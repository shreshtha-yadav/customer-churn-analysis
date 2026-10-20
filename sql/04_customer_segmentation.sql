-- Customer loyalty and risk segmentation using CTEs and CASE WHEN
WITH customer_scoring AS (
    SELECT 
        customerID,
        tenure,
        MonthlyCharges,
        Contract,
        Churn,
        CASE 
            WHEN tenure >= 24 AND MonthlyCharges >= 70 THEN 'Champion'
            WHEN tenure >= 24 AND MonthlyCharges < 70 THEN 'Loyal'
            WHEN tenure < 24 AND Contract = 'Month-to-month' AND MonthlyCharges >= 70 THEN 'High-Risk New'
            ELSE 'Standard'
        END AS customer_segment
    FROM telco_churn
)
SELECT 
    customer_segment,
    COUNT(customerID) AS customer_count,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(customerID), 2) AS segment_churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS segment_avg_monthly_charges
FROM customer_scoring
GROUP BY customer_segment
ORDER BY segment_churn_rate_pct DESC;