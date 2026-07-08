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

ضع الصور الموجودة داخل مجلد screenshots هنا.

## Future Improvements

- Azure Data Factory
- Power BI Dashboard
- Job Trends Analytics