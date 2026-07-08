# Databricks notebook source
import requests
import csv
import pandas as pd 
from bs4 import BeautifulSoup
from itertools import zip_longest
import re
from datetime import datetime


# !pip install lxml

# COMMAND ----------

job_title = []
company_name = []
location_name = []

employment_type = []
work_mode = []
experience_level = []
yrs_of_exp = []
categories = []
skills = []
ago=[]
links=[]
salaries=[]

# COMMAND ----------

scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pg_num=0
while True:
    url = f'https://wuzzuf.net/search/jobs?q=python&start={pg_num}'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    limit=int(soup.find('strong').text)
    # print(limit)
    if (pg_num > limit//15):
        print('pages ended ,terminate')
        break
    job_titles = soup.find_all('h2', class_='css-s5fwzh')
    company_names = soup.find_all('a', class_='css-ipsyv7')
    location_names = soup.find_all('span', class_='css-16x61xq')
    job_details = soup.find_all('div', class_='css-1rhj4yg')
    days_ago=soup.find_all('div',{'class':['css-eg55jf','css-1jldrig']})
    
    # print(link)
    pattern = r'^(Full Time|Part Time|Internship|Freelance)(Hybrid|Remote|On-site)(Experienced|Entry Level|Senior Management|Manager|Student|Fresh Graduate)'

    for i in range(len(job_titles)):

        job_title.append(job_titles[i].text.strip())
        company_name.append(company_names[i].text.strip().rstrip(' -'))
        location_name.append(location_names[i].text.strip())
        ago.append(days_ago[i].text)
        links.append(job_titles[i].find('a').attrs['href'])
        
        details = job_details[i].text.strip()
        details = details.replace("Full TimePart Time", "Full Time · Part Time")
        details = re.sub(pattern, r"\1 · \2 · \3", details)

        details = re.sub(
        pattern,
        r"\1 · \2 · \3",
        details
        )

        parts = [p.strip() for p in details.split('·')]

        employment_type.append(parts[0])
        work_mode.append(parts[1])
        experience_level.append(parts[2])
        yrs_of_exp.append(parts[3])

        categories.append(parts[4])

        skills.append(parts[5:])
    pg_num+=1


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS jobs;
# MAGIC CREATE SCHEMA IF NOT EXISTS jobs.bronze;

# COMMAND ----------

# for link in links:
#     result=requests.get('https://wuzzuf.net'+link, headers={"User-Agent": "Mozilla/5.0"})
#     src=result.content
#     soup = BeautifulSoup(src,'lxml')
#     salary = soup.find("span", {"data-testid": "details-label"}, string="Salary:")
#     salary = salary.find_next("span", {"data-testid": "details-text"}).text.strip()


#     print(salary)
#     print('https://wuzzuf.net/'+link)

# COMMAND ----------

df = pd.DataFrame({
    "Job_Title": job_title,
    "Company": company_name,
    "Location": location_name,
    "Employment_Type": employment_type,
    "Work_Mode": work_mode,
    "days": ago,
    "Experience_Level": experience_level,
    "Year_of_Experience": yrs_of_exp,
    "Category": categories,
    "Skills": skills,
    "Job_URL": ["https://wuzzuf.net" + link for link in links],
    "Scraped_At": scraped_at
})

display(df)

spark_df = spark.createDataFrame(df)
from delta.tables import DeltaTable

delta_table = DeltaTable.forName(spark, "python_jobs")

(delta_table.alias("old")
 .merge(
    spark_df.alias("new"),
    "old.Job_URL = new.Job_URL"
)
 .whenMatchedUpdateAll()
 .whenNotMatchedInsertAll()
 .execute())