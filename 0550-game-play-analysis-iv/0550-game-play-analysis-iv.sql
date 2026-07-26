SELECT ROUND(
   COUNT(a.player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM 
(
    SELECT player_id,MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)first_login 
JOIN Activity a
ON a.player_id=first_login.player_id
AND a.event_date = DATE_ADD(first_login.first_date, INTERVAL 1 DAY);