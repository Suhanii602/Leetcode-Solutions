# Write your MySQL query statement below
WITH RECURSIVE level_cte AS (
    
    SELECT employee_id,
           employee_name,
           manager_id,
           salary,
           1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL
    SELECT e.employee_id,
           e.employee_name,
           e.manager_id,
           e.salary,
           l.level + 1
    FROM Employees e
    JOIN level_cte l
      ON e.manager_id = l.employee_id
),

hierarchy AS (

    SELECT employee_id AS manager,
           employee_id AS emp
    FROM Employees

    UNION ALL

    SELECT h.manager,
           e.employee_id
    FROM hierarchy h
    JOIN Employees e
      ON e.manager_id = h.emp
)

SELECT
    l.employee_id,
    l.employee_name,
    l.level,
    COUNT(h.emp) - 1 AS team_size,
    SUM(e.salary) AS budget
FROM level_cte l
JOIN hierarchy h
    ON l.employee_id = h.manager
JOIN Employees e
    ON h.emp = e.employee_id
GROUP BY
    l.employee_id,
    l.employee_name,
    l.level
ORDER BY
    l.level,
    budget DESC,
    l.employee_name;