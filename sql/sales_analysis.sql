SELECT 
    city,
    ROUND(SUM(revenue),2) AS total_revenue
FROM sales
GROUP BY city
ORDER BY total_revenue DESC;


SELECT
    product_category,
    ROUND(SUM(revenue),2) AS total_revenue
FROM sales
GROUP BY product_category
ORDER BY total_revenue DESC;


WITH customer_revenue AS (
    SELECT
        customer_id,
        customer_name,
        city,
        ROUND(SUM(revenue),2) AS client_revenue
    FROM sales
    GROUP BY customer_id, customer_name, city
),
total_revenue AS (
    SELECT 
        SUM(client_revenue) AS all_revenue
    FROM customer_revenue
),
revenue_share AS (
    SELECT
        cr.customer_id,
        cr.customer_name,
        cr.city,
        cr.client_revenue,
        ROUND(cr.client_revenue * 100.0 / tr.all_revenue, 2) AS revenue_share
    FROM customer_revenue cr, total_revenue tr
)
SELECT 
    customer_id,
    customer_name,
    city,
    client_revenue,
    revenue_share,
    CASE
        WHEN revenue_share >= 3 THEN 'VIP'
        WHEN revenue_share >=1 AND revenue_share < 3 THEN 'Regular'
        ELSE 'Low Value'
    END AS customer_segment
FROM revenue_share
ORDER BY revenue_share DESC;


SELECT
    month,
    ROUND(SUM(revenue),2) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

