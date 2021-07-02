"""
Missing Data Checker

This script checks for missing dates between a given timeframe. It does not check if the data is accurate.
"""
# Import Required Modules
import json
import datetime

# Global Variables 
MAIN = {}

# Load Data Function
def load():
    with open("SG-COVIDdata/data/dailyLocalCases-pre1jun21.json") as file:
        dailyLocalCasespre1jun21 = json.load(file)
    
    with open("SG-COVIDdata/data/dailyLocalCases.json") as file:
        dailyLocalCases = json.load(file)
    
    with open("SG-COVIDdata/data/dailyVaxData.json") as file:
        dailyVaxData = json.load(file)

    return dailyLocalCasespre1jun21, dailyLocalCases, dailyVaxData

def unload(MAIN):
    with open("SG-COVIDdata/missing-data.json", "w") as file:
        json.dump(MAIN, file, indent=4)

dailyLocalCasespre1jun21, dailyLocalCases, dailyVaxData = load() # Initialisation

def check_dailyLocalCases(dailyLocalCasespre1jun21, dailyLocalCases):
    START_DATE = datetime.datetime(2020,10,5)
    END_DATE = datetime.datetime(2021,6,1)
    MAIN["dailyLocalCases"] = []
    while True:
        if START_DATE == END_DATE:
            break

        START_DATE_STR = START_DATE.strftime("%d-%m-%Y")
        if START_DATE_STR not in dailyLocalCasespre1jun21:
            print(START_DATE_STR)
            MAIN["dailyLocalCases"].append(START_DATE_STR)
        START_DATE += datetime.timedelta(days=1)

    START_DATE = datetime.datetime(2021,6,1).date()
    END_DATE = datetime.datetime.now().date()
    while True:
        if START_DATE == END_DATE:
            break

        START_DATE_STR = START_DATE.strftime("%d-%m-%Y")
        if START_DATE_STR not in dailyLocalCases:
            print(START_DATE_STR)
            MAIN["dailyLocalCases"].append(START_DATE_STR)
        START_DATE += datetime.timedelta(days=1)

def check_dailyVaxData(dailyVaxData):
    START_DATE = datetime.datetime(2021,6,28).date()
    END_DATE = datetime.datetime.now().date()
    MAIN["dailyVaxData"] = []
    while True:
        if START_DATE == END_DATE:
            break

        START_DATE_STR = START_DATE.strftime("%d-%m-%Y")
        if START_DATE_STR not in dailyVaxData:
            print(START_DATE_STR)
            MAIN["dailyVaxData"].append(START_DATE_STR)
        START_DATE += datetime.timedelta(days=1)



### RUN TO CHECK ###
check_dailyLocalCases(dailyLocalCasespre1jun21, dailyLocalCases)
check_dailyVaxData(dailyVaxData)

unload(MAIN)

# Main Function
"""
while True:
    if START_DATE == END_DATE:
        break

    START_DATE_STR = START_DATE.strftime("%d-%m-%Y")
    if START_DATE_STR not in data:
        print(START_DATE_STR)
    START_DATE += datetime.timedelta(days=1)
"""