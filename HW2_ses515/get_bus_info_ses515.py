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

%pylab inline
pl.rc('font', size=15)

key = sys.argv[1]
line = sys.argv[2]
fout = open(sys.argv[3], "w")


if not len(sys.argv) == 3:
    print ("Invalid number of arguments.")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
   "a&VehicleMonitoringDetailLevel=calls&LineRef=" + line

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
   fout.write("{},{},{},{}".format(bus_list[i][1].values()[0], bus_list[i][1].values()[1], stop, status))   
            
