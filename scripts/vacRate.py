"""
Simple Prediction Model to calculate number of completed doses after x number of days based on past few days vaccination rates.
Not extremely accurate as completed vaccination doses are random everyday

Just another testing script.
"""

import json
import numpy as np

with open("data/dailyVaxData.json") as file:
    data = json.load(file)
DAYS = 5
OFFSET = 42

data = list(data.items())[:DAYS]
data = list(map(lambda x: x[1]['completed'],data))[::-1]
x = [ x for x in range(1,len(data)+1)]
m, b = np.polyfit(x,data,1)
m, b = m.item(), b.item()
def f(a):
    return (m*a) +b

print(f(DAYS+OFFSET))

print((f(DAYS+OFFSET)/5685800)*100)