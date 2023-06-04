import numpy as np
import os, math, time, datetime

def location():
    f = open("info_locate.txt", 'a+')
    if os.stat("info_locate.txt").st_size == 0:
        input_name= str(input("Location Name:"))
        input_LAT = float(input("Latitude: "))
        input_LON = float(input("Longitude: "))
        for i in input_name, input_LAT, input_LON:
            f.write("%s\n" % i)
    f.close()

    f = open("info_locate.txt", 'r')
    lines = f.readlines()

    #delete \n
    lines = list(map(lambda s: s.strip(), lines))

    for i in range(0, int((len(lines)/3))):
        print(i+1, " Location name:", lines[3*i], "  Latitude: ", lines[3*i+1], "  Longitude: ", lines[3*i+2])
        
    temp = int(input("Select # of Location: "))
    LAT = float(lines[3*temp-2])
    LON = float(lines[3*temp-1])
    f.close()
    return LAT, LON
