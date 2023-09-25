WITH flaten AS (
    SELECT
    s.country_key,
    c.country_name,
    DATE_PART(MONTH FROM sale_time) AS month_sales,
    DATE_PART(MONTH FROM sale_time) AS year_sales,
    sales_amount
FROM Sales_stg AS s
INNER JOIN Countries AS c
    ON s.country_key = c.country_key
)
SELECT 
    fl.country_key,
    fl.country_name,
    concat(year_sales,"-", month_sales) as month_year, 
    sum(sales_amount)
FROM flaten AS fl


