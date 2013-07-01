#!/usr/bin/python
"""
Read csv station data and create an xml file from it
"""
from pylab import csv2rec
import xml.etree.ElementTree as ET

lines = ["Bakerloo", "Central", "Circle", "District", "HamAndCity", "Jubilee",
         "Metropolitan", "Northern", "Piccadilly", "Victoria",
         "WaterlooAndCity"]

for line in lines:
    stationdata = csv2rec(line + ".csv", delimiter=',', converterd={5:str})
    tree = ET.parse('Tube.xml')
    root = tree.getroot()
    for i in range(0, stationdata.size):
        newstation = ET.Element('station', {'name': stationdata[i][0]})
        root.append(newstation)
        tree.write(line + ".xml")
