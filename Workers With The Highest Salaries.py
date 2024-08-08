# Import your libraries
import pandas as pd

#Your output should include the highest-paid title or multiple titles with the same salary.

max_salary = worker.salary.max() # get max of salary column
workers_max_sal = worker[worker["salary"] == max_salary]
worker_id_corr = title[title["worker_ref_id"].isin(workers_max_sal["worker_id"])]
worker_titles = worker_id_corr["worker_title"]
Highest_Salaries = pd.DataFrame({"best_titles" : worker_titles.tolist()})
