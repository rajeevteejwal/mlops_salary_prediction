import glassdoor_scraper as gs 
import pandas as pd 

# path = "C:/Users/Ken/Documents/ds_salary_proj/chromedriver"
# path = "../../chromedriver/chromedriver"
path = "C:/Users/rajee\Desktop/ai_workbench/mlops_salary_prediction/chromedriver/chromedriver"

df = gs.get_jobs('data scientist',10, False, path, 15)

df.to_csv('data/raw/glassdoor_jobs.csv', index = False)