"""
Scrape Singapore MOH Press Releases that were stored in alphamodel/COVID-19-SG GitHub repository
(SRC: github.com/alphamodel/COVID-19-SG)

Not to be used in automated scraping. Start and End Date variables are to be changed manually.
"""
# Import Required Modules
import json
import time
import requests
import datetime
from bs4 import BeautifulSoup

# Global Variables
PATH = "https://raw.githubusercontent.com/alphamodel/COVID-19-SG/2b3a30fcd086159caa9289593bb50a2d86c84393/moh/"
START_DATE = datetime.datetime(2020,10,1)
DATA = {}

# Getters and Setters
def load():
    with open("SG-COVIDdata/data/pre1jun21.json") as file:
        dailyLocalCases = json.load(file)
    return dailyLocalCases

def unload(dailyLocalCases):
    with open("SG-COVIDdata/data/pre1jun21.json", "w") as file:
        json.dump(dailyLocalCases, file, indent=4)

def get_press_release(date):
    date = datetime.datetime.strftime(date, "%Y%m%d")
    file = f"{date}.json"
    data = requests.get(PATH + file)
    data = data.json()
    return data["pressItemDictionary"]["Press Releases"]

def main(START_DATE):

    while True:

        if START_DATE == datetime.datetime(2020,11,1):
            break
        
        data = get_press_release(START_DATE)
        for news in data:
            title = news["Title"]
            if all(elem in title.lower().split()  for elem in 'Locally Transmitted COVID-19 Infection'.lower().split()) or all(elem in title.lower().split()  for elem in 'Update on Local COVID-19 Situation'.lower().split()):
                description  = news["MainContent"]
                
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
                DATA[date] = int(localCases)
                unload(DATA)
                print(date,": ",localCases)

        START_DATE += datetime.timedelta(days=1)
        time.sleep(0.5)


DATA = load() # Initialisation

main(START_DATE) # Run Main Function

### SORT DATA SUCH THAT LATEST ON TOP ###
# Not the best method when data size inceases as at least O(n^2)
DATA = sorted(list(DATA.items()), key=lambda x:datetime.datetime.strptime(x[0],"%d-%m-%Y"), reverse=True)
DATA = dict(DATA)
unload(DATA)

                