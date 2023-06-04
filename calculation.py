import math, time, datetime
import numpy as np
#time module; time.time() structure gets unix time or Epoch time started in January 1, 1970 

# Add or subtract multiples of 360 to bring LST in range 0 to 360
def degree360(temp):
    if temp > 0:
        while(360 <= temp):
            temp = temp - 360 
        return temp
    elif temp < 0:
        while(temp < 0):
            temp = temp + 360
        return temp

# display GMT
def GMT():
    tm = time.gmtime()
    string = time.strftime('%Y/%m/%d/%H/%M/%S', tm)
    return string

# display Localtime
def Localtime():
    tm = time.localtime()
    string = time.strftime('%Y/%m/%d/%H/%M/%S', tm)
    return string

# input RA and DEC coordinates of celestial body
def input_RA_DEC():
    RA = input("Input RA (format: 00h00m00s): ")
    RA = 15*(float(RA[0:(RA.find('h' or 'H'))])+(float(RA[RA.find('h' or 'H')+1 : (RA.find('m' or 'M'))]))/60+(float(RA[RA.find('m' or 'M')+1 : RA.find('s' or 'S')]))/3600)
    RA = math.radians(RA)   
    
    DEC = input("Input DEC (format: 00d00'00): ")
    DEC = (float(DEC[0:(DEC.find('d' or 'D'))])+(float(DEC[DEC.find('d' or 'D')+1 : (DEC.find("'"))]))/60+(float(DEC[DEC.find("'")+1 : ]))/3600)
    DEC  = math.radians(DEC)
    return RA, DEC #radian

# Coordinate Transformation from Horizontal Coordinate system to Equatorial Coordinate system
def cal_AZ_ALT(RA, DEC, LAT, HA):
    #ALT
    sin_ALT = np.sin(DEC)*np.sin(LAT)+np.cos(DEC)*np.cos(LAT)*np.cos(HA)
    ALT = np.arcsin(sin_ALT)
    #AZ
    cos_AZ = (np.sin(DEC)-np.sin(ALT)*np.sin(LAT))/(np.cos(ALT)*np.cos(LAT))
    AZ = np.arccos(cos_AZ)
    return AZ, ALT  #radian



