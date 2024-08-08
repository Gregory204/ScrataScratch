# Import your libraries
import pandas as pd

# Start writing code
df = employee.groupby(['department', 'first_name'])['salary'].max().reset_index()
idx_max = df.groupby('department')['salary'].idxmax()
df_highest_salary = df.loc[idx_max]
df_highest_salary.rename(columns={'salary' : 'highest_salary'})
