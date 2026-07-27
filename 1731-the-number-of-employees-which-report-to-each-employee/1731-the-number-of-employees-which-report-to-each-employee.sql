SELECT
    e.employee_id,
    e.name,
    emp.reports_count,
    emp.average_age
FROM Employees e
JOIN (
    SELECT reports_to,
           COUNT(*) AS reports_count,
           ROUND(AVG(age),0) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)emp
ON e.employee_id=emp.reports_to
ORDER BY e.employee_id;