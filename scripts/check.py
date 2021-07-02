"""
Missing Data Checker

This script checks for missing dates between a given timeframe. It does not check if the data is accurate.
"""
# Import Required Modules
import json
import datetime

# Global Variables 
START_DATE = datetime.datetime(2020,10,1)
END_DATE = datetime.datetime(2021,6,1)

# Load Data Function
def load():
    with open("SG-COVIDdata/data/dailyLocalCases-pre1jun21.json") as file:
        dailyLocalCases = json.load(file)
    return dailyLocalCases

data = load() # Initialisation

# Main Function
while True:
    if START_DATE == END_DATE:
        break

    START_DATE_STR = START_DATE.strftime("%d-%m-%Y")
    if START_DATE_STR not in data:
        print(START_DATE_STR)
    START_DATE += datetime.timedelta(days=1)
