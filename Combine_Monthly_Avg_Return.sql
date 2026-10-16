SELECT
    n.Month,
    ROUND(AVG(n.Daily_Return_Percent), 4) AS Nifty50_Avg_Return,
    ROUND(AVG(b.Daily_Return_Percent), 4) AS BankNifty_Avg_Return
FROM nifty50 n
JOIN banknifty b
    ON n.Date = b.Date
GROUP BY n.Month
ORDER BY MIN(n.Date);