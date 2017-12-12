"""Python web scraper."""

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup


job_page = ['https://stackoverflow.com/jobs']

for i in range(2, 10):
    job_page.append('https://stackoverflow.com/jobs?pg=' + str(i))

for url in job_page:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    job_posting = soup.find_all('h2', attrs={'class': 'g-col10'})
    print(job_posting)
    for text in job_posting:
        job_link = text.find_all('a')

"""
    date_posted = soup.find_all('p', attrs={'class': '-posted-date g-col'})
    date = date_posted.text
    print(date)
"""


with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([job_posting, datetime.now()])

"""
div class="-job-summary "
div class="-title g-row"
    h2 class="g-col10"
        a href="url" title="title" class="job-link"
    p class="-posted-date g-col"
"""
