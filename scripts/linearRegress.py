"""
Simple Script to Compute Best Fit Straight Line

"""

import json
import numpy as np

# Open required files
with open("../data/dailyLocalCases.json") as file:
    dailyLocalCases = json.load(file)

#define data
xValues = [x for x in range(1,31)]
yValues = list(map(lambda x: x[1] , list(dailyLocalCases.items())[::-1][-30:])) # Convert dictionary into list of tuples. Reverse the list. Slice last 30 days. Extract the numbers
x = np.array(xValues)
y = np.array(yValues)

#find line of best fit
a, b = np.polyfit(x, y, 1)

def y(x):
    return a*x + b

day = 30
while True:
    check = y(day)
    if check <= 0:
        print(day,":",check)
        break
    else:
        print(day,":",check)
        day+=1
