import re
import pandas as pd
from datetime import datetime
from config import pattern

def transform(job_titles,
              company_names,
              location_names,
              job_details,
              days_ago):

    job_title = []
    company_name = []
    location_name = []

    employment_type = []
    work_mode = []
    experience_level = []
    yrs_of_exp = []
    categories = []
    skills = []
    ago = []
    links = []

    scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i in range(len(job_titles)):

        job_title.append(job_titles[i].text.strip())
        company_name.append(company_names[i].text.strip().rstrip(" -"))
        location_name.append(location_names[i].text.strip())
        ago.append(days_ago[i].text)
        links.append("https://wuzzuf.net" + job_titles[i].find("a")["href"])

        details = job_details[i].text.strip()
        details = details.replace("Full TimePart Time", "Full Time · Part Time")
        details = re.sub(pattern, r"\1 · \2 · \3", details)

        parts = [p.strip() for p in details.split("·")]

        employment_type.append(parts[0])
        work_mode.append(parts[1])
        experience_level.append(parts[2])
        yrs_of_exp.append(parts[3])
        categories.append(parts[4])
        skills.append(parts[5:])

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
        "Job_URL": links,
        "Scraped_At": scraped_at
    })

    return df