#!/usr/bin/python
import sys
import json

prevRoute = None

months = ['01', '02', '03', '04', '05',
          '06', '07', '08', '09', '10', '11', '12']

routes = {}

maxCost = 0

for m in months:
    routes[m] = {"topRoutes": ["", "", "", "", ""],
                 "topCosts": [0, 0, 0, 0, 0]}

lines = sys.stdin

for line in lines:
    line = line.strip()
    if not line:
        continue
    currentRoute, cost = line.split('\t')
    cost = float(cost)
    if currentRoute != prevRoute:
        if prevRoute != None:
            month = prevRoute[0:2]
            minval = min(routes[month]["topCosts"])
            if(minval < maxCost):
                ind = routes[month]["topCosts"].index(minval)
                routes[month]["topCosts"][ind] = maxCost
                routes[month]["topRoutes"][ind] = prevRoute
        prevRoute = currentRoute
        maxCost = cost
    else:
        if(maxCost < cost):
            maxCost = cost

month = prevRoute[0:2]
minval = min(routes[month]["topCosts"])

if(minval < maxCost):
    ind = routes[month]["topCosts"].index(minval)
    routes[month]["topCosts"] = maxCost
    routes[month]["topRoutes"] = prevRoute

print routes
