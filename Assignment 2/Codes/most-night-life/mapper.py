#!/usr/bin/python
import sys

yearUsed = "2011"

for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    year = row[2][:4]
    month = row[2][5:7]
    dlong = row[5]
    dlat = row[6]
    time = row[2][11:13]
    passengers = row[7]
    l = [22, 23, 0, 1, 2, 3]
    if dlong != "0":
        if year == yearUsed and int(time) in l:
            print "%s:%s:%s\t%s\n" % (month, dlong, dlat, passengers)
