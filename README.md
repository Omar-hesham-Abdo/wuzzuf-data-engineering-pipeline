
# Wuzzuf Data Engineering Pipeline

## Overview

An end-to-end ETL pipeline that extracts Python job listings from Wuzzuf, transforms and cleans the data using Pandas, and incrementally loads the data into Delta Lake on Databricks.

## Architecture

```
Wuzzuf
   │
   ▼
Requests + BeautifulSoup
   │
   ▼
Pandas Transformations
   │
   ▼
Spark DataFrame
   │
   ▼
Delta Lake
   │
   ▼
MERGE (Incremental Loading)
```

## Features

- Scrape all search result pages
- Extract structured job information
- Clean and transform data
- Convert to Spark DataFrame
- Store data in Delta Lake
- Incremental loading using Delta MERGE
- Automated execution using Databricks Jobs

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- PySpark
- Delta Lake
- Databricks

## Dataset Columns

- Job Title
- Company
- Location
- Employment Type
- Work Mode
- Experience Level
- Years of Experience
- Category
- Skills
- Job URL
- Scraped At

## Screenshots
<img width="1886" height="932" alt="job" src="https://github.com/user-attachments/assets/8d7f5bd8-dc5e-4ce7-8002-cd21c84fa3af" />
<img width="1298" height="833" alt="delta_merge" src="https://github.com/user-attachments/assets/dcf42429-c8bb-40e9-835a-4a1e271de9e9" />
<img width="1885" height="896" alt="catalog_with_table" src="https://github.com/user-attachments/assets/e3313fd7-34de-451e-8f76-ecca785f7ed3" /> 

## Future Improvements

- Azure Data Factory
- Power BI Dashboard
- Job Trends Analytics
