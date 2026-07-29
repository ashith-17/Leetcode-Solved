# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM Insurance 
WHERE TIV_2015 IN (
        SELECT TIV_2015 
        FROM Insurance 
        GROUP BY TIV_2015 
        HAVING COUNT(*) > 1
    )
    AND CONCAT(LAT, LON) IN (
        SELECT CONCAT(LAT, LON) 
        FROM Insurance 
        GROUP BY LAT, LON 
        HAVING COUNT(*) = 1
    );   

 

