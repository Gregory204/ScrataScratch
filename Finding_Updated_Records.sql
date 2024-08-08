WITH cte AS
(SELECT *, ROW_NUMBER() OVER(PARTITION BY id order BY salary DESC) AS ranks
FROM ms_employee_salary)

SELECT id, first_name, last_name, department_id, salary
FROM cte
WHERE ranks = 1
