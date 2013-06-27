#!/usr/bin/python
"""
Read csv station data and create an xml file from it
"""
from pylab import csv2rec
import xml.etree.ElementTree as ET

stationdata = csv2rec("London270.csv", delimiter=',', converterd={5:str})

tree = ET.parse('Tube.xml')
root = tree.getroot()

for i in range(1, stationdata.size):
    newstation = ET.Element('station', {'name': stationdata[i][0]})

    newrequired = ET.Element('required', {})
    newrequired.text = "true"
    newstation.append(newrequired)

    newline = ET.Element('line', {})
    newstation.append(newline)

    newosx = ET.Element('osx', {})
    newosx.text = str(stationdata[i][1])
    newstation.append(newosx)

    newosy = ET.Element('osy', {})
    newosy.text = str(stationdata[i][2])
    newstation.append(newosy)

    newlatitude = ET.Element('latitude', {})
    newlatitude.text = str(stationdata[i][3])
    newstation.append(newlatitude)

    newlongitude = ET.Element('longitude', {})
    newlongitude.text = str(stationdata[i][4])
    newstation.append(newlongitude)

    newzone = ET.Element('zone', {})
    newzone.text = str(stationdata[i][5])
    newstation.append(newzone)

    root.append(newstation)

tree.write('test1.xml')
