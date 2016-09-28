"""
This is a code for GPS postprocessing from RTKlib,
created from Victor for Svarmi.

Still under development
"""


import numpy

with open("gps_file.txt", 'r') as GPS, open("Final.txt", 'r+') as GPSo:
    gps = GPS.readlines()
    for line in gps:
        strip = line.strip()
        nocol = line[26:68]
        stripnocol = nocol.strip()
        if strip.startswith('%'):
            continue
        elif stripnocol.endswith(str(1)):
            GPSo.write(nocol+'\n')

data = numpy.loadtxt("Final.txt")
Latitude = numpy.average(data[:,0])
Longitude = numpy.average(data[:,1])
Height = numpy.average(data[:,2])
print "LAT", Latitude
print "LON", Longitude
print "Height", Height

