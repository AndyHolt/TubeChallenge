#!/usr/bin/python
"""
Read csv station data and create an xml file from it
"""
from pylab import csv2rec
import xml.etree.ElementTree as ET

stationdata = csv2rec("London270.csv", delimiter=',')

tree = ET.parse('Tube.xml')
root = tree.getroot()

for i in range(1, stationdata.size):
    newstation = ET.Element('station', {'name': stationdata[i][0]})
    root.append(newstation)

tree.write('test1.xml')
