"""
Singapore Ministry of Health RSS Feed Scrapper (Unlink Local Cases)
Version 1.0 

Updated Manually. Unlink cases are recorded as of press release date as unlink cases may become linked as the days goes by.
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

def get_previous_data(data):
    # Get Data as far as RSS feed contains
    for news in data:
        title = news['title']
        if  all(elem in title.lower().split()  for elem in 'Updates on Local COVID-19 Situation'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
            description = news["description"]
            
            if all(elem in description.lower().split() for elem in "further updates will be shared via the MOH press release that will be issued".lower().split()):
                continue
            soup = BeautifulSoup(description, "html.parser")
            description = soup.get_text()
            description = description[description.index("As"):]
            try:
                date = description[description.index("MINISTRY OF HEALTH")+18:]
                date = date[:date.index("National")]
                date = date[:date.index("2021")+4].strip()
                date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            except:
                break
            """
            date = description[6:description.index("12pm")-2]
            date = datetime.datetime.strptime(date, "%d %B %Y").strftime("%d-%m-%Y")
            """
            try:
                localunlink = description[:description.index("are currently unlinked.")][-5:]
            except:
                break # Temporary Fix to Get Latest Data. Also to alert when broken.
                try:
                    check = input(f"check {date} value: ")
                except KeyboardInterrupt:
                    break
                localunlink = check
            localunlink = "".join(char for char in localunlink if char in "1234567890")
            print(date, localunlink)

            if len(localunlink) == 0:
                localunlink = 0
            dailyLocalUnlinkCases[date] = int(localunlink)

def load():
    with open("../data/dailyLocalUnlinkCases.json") as file:
        dailyLocalUnlinkCases = json.load(file)

    return dailyLocalUnlinkCases

def unload(dailyLocalUnlinkCases):
    with open("../data/dailyLocalUnlinkCases.json", "w") as file:
        json.dump(dailyLocalUnlinkCases, file, indent=4)


### RUN EVERYTIME ###
data = get_MOH_feed()
dailyLocalUnlinkCases = load()

### RUN ONCE TO GET ALL DATA ###
get_previous_data(data)

### RUN EVERYTIME ###
# SORT DATA SUCH THAT LATEST ON TOP
# Not the best method when data size inceases as at least O(n^2)
dailyLocalUnlinkCases = sorted(list(dailyLocalUnlinkCases.items()), key=lambda x:datetime.datetime.strptime(x[0],"%d-%m-%Y"), reverse=True)
dailyLocalUnlinkCases = dict(dailyLocalUnlinkCases)

unload(dailyLocalUnlinkCases)
