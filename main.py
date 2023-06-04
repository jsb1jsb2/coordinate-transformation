import calculation as cal
import function
import os, math, time, datetime
#from turtle import home
import numpy as np

#location
LAT, LON = function.location()

#time
#time selection
print("GMT: ", cal.GMT())
print("Localtime: ", cal.Localtime())
date = str(input('Input GMT: YYYY/MM/DD/HH/MM/SS or now: '))

if date == 'now' or date =='Now':
    date = cal.GMT()
#timezone = int("Input Timezone: ")
date_split = date.split('/')
UT = int(date_split[3]) + int(date_split[4])/60 + int(date_split[5])/3600

# convert string to datetimeformat
date = datetime.datetime.strptime(date, "%Y/%m/%d/%H/%M/%S")

RA, DEC = cal.input_RA_DEC()

# convert datetime to timestamp
date = datetime.datetime.timestamp(date)
Days = ((date-946684800)/86400)
LST = cal.degree360(100.46 + 0.985647 * Days + LON + 15*UT)
HA = cal.degree360(LST - math.degrees(RA))
HA  = math.radians(HA)
LAT = math.radians(LAT)



AZ, ALT = cal.cal_AZ_ALT(RA, DEC, LAT, HA)

AZ = math.degrees(AZ)
ALT = math.degrees(ALT)
if math.sin(HA) > 0:
    AZ = 360 - AZ

print("AZ: %f, ALT: %f" %(AZ, ALT))