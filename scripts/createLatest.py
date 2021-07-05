"""
SG-COVIDdata API formating script

"""
# Import Required Modules
import json

# Open required files
with open("../data/dailyLocalCases.json") as file:
    dailyLocalCases = json.load(file)

with open("../data/dailyVaxData.json") as file:
    dailyVaxData = json.load(file)

# Global Variable

LATEST = {}

# Load Latest Local Cases
last = list(dailyLocalCases.items())[0]
LATEST["dailyLocalCases"] = {last[0]: last[1]}

# Load Latest Vaccination Data
last = list(dailyVaxData.items())[0]
LATEST["dailyVaxData"] = {last[0]: last[1]}

# Unload Latest into API
with open("../api/latest.json", "w") as file:
    json.dump(LATEST, file, indent=4)

