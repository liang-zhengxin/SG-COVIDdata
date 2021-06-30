"""
Singapore Ministry of Health RSS Feed Scrapper
Version 1.0 
"""
# Import Required Modules

import requests
import json
import xmltodict
import datetime
from bs4 import BeautifulSoup

# Getters and Setters

def get_MOH_feed():
    data = requests.get('https://www.moh.gov.sg/feeds/news-highlights')
    data = xmltodict.parse(data.content)
    data = data["rss"]['channel']['item']
    return data

def get_latest_local_cases(data):
    for news in data:
        title = news['title']
        if all(elem in title.lower().split()  for elem in 'Locally Transmitted COVID-19 Infection'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
            description = news["description"]
            
            if all(elem in description.lower().split() for elem in "further updates will be shared via the MOH press release that will be issued".lower().split()):
                continue
            soup = BeautifulSoup(description, "html.parser")
            description = soup.get_text()
            description = description[description.index("As"):]
            date = description[6:description.index("12pm")-2]
            date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            localCases = description[description.index("verified"):description.index("locally transmitted")]
            localCases = "".join(char for char in localCases if char in "1234567890")
            break
    return (date, int(localCases))


def get_previous_data(data):
    # Get Data as far as RSS feed contains
    for news in data:
        title = news['title']
        if all(elem in title.lower().split()  for elem in 'Locally Transmitted COVID-19 Infection'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
            description = news["description"]
            
            if all(elem in description.lower().split() for elem in "further updates will be shared via the MOH press release that will be issued".lower().split()):
                continue
            soup = BeautifulSoup(description, "html.parser")
            description = soup.get_text()
            description = description[description.index("As"):]
            date = description[6:description.index("12pm")-2]
            date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            localCases = description[description.index("verified"):description.index("locally transmitted")]
            localCases = "".join(char for char in localCases if char in "1234567890")
            dailyLocalCases[date] = int(localCases)

def load():
    with open("SG-COVIDdata/data/dailyLocalCases.json") as file:
        dailyLocalCases = json.load(file)
    return dailyLocalCases

def unload(dailyLocalCases):
    with open("SG-COVIDdata/data/dailyLocalCases.json", "w") as file:
        json.dump(dailyLocalCases, file, indent=4)


### RUN EVERYTIME ###
data = get_MOH_feed()
dailyLocalCases = load()

### RUN DAILY ###
date, localCases = get_latest_local_cases(data)
dailyLocalCases[date] = localCases

### RUN ONCE TO GET ALL DATA ###
#get_previous_data(data)

### RUN EVERYTIME ###
unload(dailyLocalCases)
