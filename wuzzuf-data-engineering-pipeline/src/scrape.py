import requests
from bs4 import BeautifulSoup
from config import url

def scrape(page):

    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.content, "lxml")

    job_titles = soup.find_all('h2', class_='css-s5fwzh')
    company_names = soup.find_all('a', class_='css-ipsyv7')
    location_names = soup.find_all('span', class_='css-16x61xq')
    job_details = soup.find_all('div', class_='css-1rhj4yg')
    days_ago = soup.find_all('div', {'class':['css-eg55jf','css-1jldrig']})

    limit = int(soup.find('strong').text)

    return job_titles, company_names, location_names, job_details, days_ago, limit