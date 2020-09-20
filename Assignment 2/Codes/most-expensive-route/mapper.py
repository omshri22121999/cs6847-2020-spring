#!/usr/bin/python
import sys

yearUsed = "2011"
for line in sys.stdin:
    line = line.strip()
    row = line.split(",")
    year = row[2][:4]
    month = row[2][5:7]
    plong = row[3]
    plat = row[4]
    dlong = row[5]
    dlat = row[6]
    fare = row[1]
    if plong != "0":
        if year == yearUsed:
            print "%s:%s:%s:%s:%s\t%s\n" % (month,
                                            plong, plat, dlong, dlat, fare)
