from __future__ import print_function

import pylab as pl
import os
import json
import pandas as pd
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# %pylab inline
pl.rc('font', size=15)

key = sys.argv[1]
line = sys.argv[2]
newfile = open(sys.argv[3], "w")


if not len(sys.argv) == 4:
    print ("Invalid number of arguments.")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "&VehicleMonitoringDetailLevel=calls&LineRef=" + line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busloc = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

next_bus = []
for bus in range(len(busloc)):
    latlong = busloc[bus]['MonitoredVehicleJourney']['VehicleLocation']
    status = busloc[bus]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    stop = busloc[bus]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    next_bus.append((latlong, status, stop))

for i in range(len(busloc)):
#  print (next_bus[i][0])
#   print (next_bus[i][1].values()[1])
#  print ("======") 
    newfile.write("{},{},{},{}\n".format(next_bus[i][0]['Latitude'],next_bus[i][0]['Longitude'],next_bus[i][1],next_bus[i][2]))   
            
