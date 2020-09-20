#!/usr/bin/python
import sys
import json

prevRoute = None

months = ['01', '02', '03', '04', '05',
          '06', '07', '08', '09', '10', '11', '12']

routes = {}

count = 0

for m in months:
    routes[m] = {"topRoutes": ["", "", "", "", ""],
                 "topCounts": [0, 0, 0, 0, 0]}

lines = sys.stdin

for line in lines:
    line = line.strip()
    if not line:
        continue
    currentRoute, passengers = line.split('\t')
    if currentRoute != prevRoute:
        if prevRoute != None:
            month = prevRoute[0:2]
            minval = min(routes[month]["topCounts"])
            if(minval < count):
                ind = routes[month]["topCounts"].index(minval)
                routes[month]["topCounts"][ind] = count
                routes[month]["topRoutes"][ind] = prevRoute
        prevRoute = currentRoute
        count = int(passengers)
    else:
        count += int(passengers)

month = prevRoute[0:2]
minval = min(routes[month]["topCounts"])
if(minval < count):
    ind = routes[month]["topCounts"].index(minval)
    routes[month]["topCounts"] = count
    routes[month]["topRoutes"] = prevRoute

print routes
