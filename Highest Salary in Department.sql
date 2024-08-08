WITH cte AS
(SELECT *, MAX(salary) OVER(PARTITION BY department) AS highest_salary
FROM employee)

SELECT department, first_name, salary AS highest_salary
FROM cte
WHERE salary = highest_salary;
