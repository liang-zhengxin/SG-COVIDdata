"""
SG-COVIDdata 7 Days Rolling Average Rate Compute Script


"""
# Import Required Modules
import json

# Open required files
with open("../data/dailyLocalCases.json") as file:
    dailyLocalCases = json.load(file)

# Global Variables & Main Code
dailyLocalCases = list(map(lambda x: x[1] , list(dailyLocalCases.items())[::-1][-14:])) # Convert dictionary into list of tuples. Reverse the list. Slice last 14 days. Extract the numbers
last7days = sum(dailyLocalCases[-7:])/len(dailyLocalCases[-7:]) # Average of last 7 days
last14to8days = sum(dailyLocalCases[:-7])/len(dailyLocalCases[:-7]) # Average of last 14 to 8 days
weekRate = round(last7days/last14to8days, 5) # Weekly rate. Last 7 divided by last 14 to 8 days
print(weekRate)
