"""
Singapore Ministry of Health RSS Feed Scrapper
Version 2.0 
"""
# Import Required Modules

import requests
import json
import xmltodict
import datetime
from bs4 import BeautifulSoup

# Getters and Setters

def get_MOH_website():
    data = requests.get('https://www.moh.gov.sg/')
    data = BeautifulSoup(data.content, "html.parser")
    return data

def get_COVID_data(data):
    mydivs = data.find_all("div", {"class": "stat-item"})
    mydivs = mydivs.find_all("div", {"class": "number"})
    print(mydivs)

print(list(get_MOH_website().children))