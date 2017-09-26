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

if not len(sys.argv) == 3:
    print ("Invalid number of arguments.")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "&VehicleMonitoringDetailLevel=calls&LineRef=" + line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

allbuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

bus_list = []
for bus in range(len(allbuses)):
    name = allbuses[bus]['MonitoredVehicleJourney']['PublishedLineName']
    location = allbuses[bus]['MonitoredVehicleJourney']['VehicleLocation']
    bus_list.append((name, location))

    
for i in range(len(allbuses)):
     print ("Bus {} is at {} latitude and {} longitude".format(i, bus_list[i][1].values()[0], bus_list[i][1].values()[1]))   


                

