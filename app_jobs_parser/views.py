from django.shortcuts import render, redirect
from app_jobs_parser.models import Results
from app_jobs_parser.forms import input_form

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlretrieve
from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
import time

def jobs_input(request):
    form = input_form()
    return render(request, 'jobs_input.html', {'form':form})

def jobs_parser(request):
    if request.method != 'POST':
        return None
    else:
        # Databas cleaning
        queryset = Results.objects.all().delete()

        # Gathering and validating user input through Forms
        form = input_form(request.POST)
        if form.is_valid():
            pass
        else:
            form = input_form()
        job_input = form['position'].value()
        location_input = form['location'].value()

        indeed_url = 'https://www.indeed.com/jobs'
        pages = [10, 20]

        # Parsing indeed
        for page in pages:
            # Constructing url
            input_dict = {'q': job_input, '&l': location_input, '&start': page }
            source = requests.get(indeed_url, params=input_dict).text
            #source = requests.get('https://www.indeed.com/jobs?q=' + job_input+'&l=' + location_input + '&start{}'.format(page)).text
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

                #Database insert and ads filtering
                if 'pagead' in url:
                    pass
                else:
                    queryset = Results(Position = job_title, Company = company, Salary = salary, URL = url)
                    queryset.save()

                #Antiban
                time.sleep(1)

        # Retrieve data from database
        queryset = Results.objects.all()
        context = {
            "object_list": queryset
        }

        return render(request, 'jobs_results.html', context)
