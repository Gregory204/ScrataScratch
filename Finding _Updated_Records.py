# Import your libraries
import pandas as pd

idx = ms_employee_salary.groupby('id')['salary'].idxmax()
curr_employee_salary = ms_employee_salary.loc[idx]
curr_employee_salary.rename(columns={'salary': 'current_salary'}, inplace=True)
curr_employee_salary
