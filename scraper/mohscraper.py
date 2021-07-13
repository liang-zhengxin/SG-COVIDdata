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
        if all(elem in title.lower().split()  for elem in 'Locally Transmitted COVID-19 Infection'.lower().split()) or all(elem in title.lower().split()  for elem in 'Updates on Local COVID-19 Situation'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
            description = news["description"]
            
            if all(elem in description.lower().split() for elem in "further updates will be shared via the MOH press release that will be issued".lower().split()):
                continue
            soup = BeautifulSoup(description, "html.parser")
            description = soup.get_text()
            description = description[description.index("As"):]
            date = description[6:description.index("12pm")-2]
            date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            try:
                localCases = description[description.index("verified"):description.index("locally transmitted")]
                localCases = "".join(char for char in localCases if char in "1234567890")
            except:
                localCases = description[description.index("confirmed"):description.index("locally transmitted")]
                localCases = "".join(char for char in localCases if char in "1234567890")
            if len(localCases) == 0:
                localCases = 0
            break
    return (date, int(localCases))


def get_previous_data(data):
    # Get Data as far as RSS feed contains
    for news in data:
        title = news['title']
        if all(elem in title.lower().split()  for elem in 'Locally Transmitted COVID-19 Infection'.lower().split()) or all(elem in title.lower().split()  for elem in 'Updates on Local COVID-19 Situation'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
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
            if len(localCases) == 0:
                localCases = 0
            dailyLocalCases[date] = int(localCases)

def get_latest_vax(data):
    for news in data:
        title = news['title']
        if all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()) or all(elem in title.lower().split()  for elem in 'Updates on Local COVID-19 Situation'.lower().split()):
            description = news["description"]
            soup = BeautifulSoup(description, "html.parser")
            description = soup.get_text()
            try:
                vaccineData = description[description.index("Progress of national vaccination programme"):description.index("full vaccination regimen.")]
            except:
                vaccineData = description[description.index("of national vaccination"):description.index("full vaccination regimen")]
            date = vaccineData[vaccineData.index("As"):]
            date = date[6:date.index("we")-2]
            date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            total = vaccineData[vaccineData.index("total number of doses administered"):vaccineData.index("covering")]
            first = vaccineData[vaccineData.index("covering"):vaccineData.index("individuals")]
            try:
                completed = vaccineData[vaccineData.index("individuals"):vaccineData.index("second dose")]
            except:
                completed = vaccineData[vaccineData.index("individuals"):vaccineData.index("completed")]
            total = "".join(char for char in total if char in "1234567890")
            first = "".join(char for char in first if char in "1234567890")
            completed = "".join(char for char in completed if char in "1234567890")
            entry = {"total":int(total), "first":int(first), "completed":int(completed)}
            break
    return date , entry

def load():
    with open("../data/dailyLocalCases.json") as file:
        dailyLocalCases = json.load(file)

    with open("../data/dailyVaxData.json") as file:
        dailyVaxData = json.load(file)
    return dailyLocalCases , dailyVaxData

def unload(dailyLocalCases, dailyVaxData):
    with open("../data/dailyLocalCases.json", "w") as file:
        json.dump(dailyLocalCases, file, indent=4)
    
    with open("../data/dailyVaxData.json", "w") as file:
        json.dump(dailyVaxData, file, indent=4)


### RUN EVERYTIME ###
data = get_MOH_feed()
dailyLocalCases, dailyVaxData = load()

### RUN DAILY ###
date, localCases = get_latest_local_cases(data)
dailyLocalCases[date] = localCases

date , entry = get_latest_vax(data)
dailyVaxData[date] = entry

### RUN ONCE TO GET ALL DATA ###
#get_previous_data(data)

### RUN EVERYTIME ###
# SORT DATA SUCH THAT LATEST ON TOP
# Not the best method when data size inceases as at least O(n^2)
dailyLocalCases = sorted(list(dailyLocalCases.items()), key=lambda x:datetime.datetime.strptime(x[0],"%d-%m-%Y"), reverse=True)
dailyLocalCases = dict(dailyLocalCases)

dailyVaxData = sorted(list(dailyVaxData.items()), key=lambda x:datetime.datetime.strptime(x[0],"%d-%m-%Y"), reverse=True)
dailyVaxData = dict(dailyVaxData)

unload(dailyLocalCases, dailyVaxData)
