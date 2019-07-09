from django.test import TestCase

# Create your tests here.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import time
import sqlite3

# Connecting to database
def jobs_parser(self):
    conn = sqlite3.connect('123.sqlite')
    cur = conn.cursor()

    # Database setup
    cur.executescript('''
    DROP TABLE IF EXISTS Jobs;

    CREATE TABLE Jobs (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Position   TEXT,
        Company   TEXT,
        Salary   TEXT,
        URL    TEXT UNIQUE,
        UNIQUE(Position, Company)
    )
    ''')

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Gathering user input
    job_input = request.POST['job_input']
    location_input = request.POST['location_input']
    #job_input = input('Whit kind of jobs you are looking for ').split()
    #location_input = input('Enter your location ').split()

    # Formating user input
    job_str = ('')
    location_str = ('')

    job_input.insert(1,'+')
    job_str = job_str.join(job_input)

    location_input.insert(1,'+')
    location_str = location_str.join(location_input)

    pages = [10, 20]

    # Parsing indeed
    for page in pages:
        source = requests.get('https://www.indeed.com/jobs?q='+job_str+'&l='+location_str+'&start{}'.format(page)).text
        soup = BeautifulSoup(source, 'lxml')

        for jobs in soup.find_all(class_='result'):
            try:
                job_title = jobs.a.text.strip()
            except:
                job_title = None
            print(job_title)

            try:
                company = jobs.span.text.strip()
            except:
                company = None
            print(company)
            try:
                salary = jobs.find('span', class_='salary no-wrap').text.strip()

            except:
                salary = None
            print(salary)
            try:
                partial_url = jobs.a.get('href')
                url = 'https://ca.indeed.com' + partial_url
            except:
                url = None
            print(url)

            cur.execute('''INSERT OR IGNORE INTO Jobs (Position, Company, Salary, URL)
                        VALUES ( ?, ?, ?, ? )''', ( job_title, company, salary, url,) )
            cur.execute('''DELETE FROM Jobs WHERE URL LIKE '%pagead%' ''')
            time.sleep(1)

    conn.commit()

    cur.execute("SELECT * FROM Jobs")
    print(cur.fetchall())

    conn.close()
    return render(request, 'index.html', {})
