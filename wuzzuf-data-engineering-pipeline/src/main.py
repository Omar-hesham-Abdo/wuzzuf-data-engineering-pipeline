from scrape import scrape
from transform import transform
from load import load

page = 0

while True:

    (
        job_titles,
        company_names,
        location_names,
        job_details,
        days_ago,
        limit
    ) = scrape(page)

    df = transform(
        job_titles,
        company_names,
        location_names,
        job_details,
        days_ago
    )

    if not df.empty:
        load(df, spark)
    else:
        print(f"No data found on page {page}, skipping load")

    if page > limit // 15:
        print("Pages ended")
        break

    page += 1