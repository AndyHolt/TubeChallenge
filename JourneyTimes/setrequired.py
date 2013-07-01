#!/usr/bin/python
"""
Set value of <required> sub-element for each station.
"""
import xml.etree.ElementTree as ET

allstations_tree = ET.parse('AllStations.xml')
allstations_root = allstations_tree.getroot()

required_tree = ET.parse('London270.xml')
required_root = required_tree.getroot()

for station in allstations_root:
    for reqstation in required_root:
        if station.attrib == reqstation.attrib:
            station.__getitem__(0).text = "true"

allstations_tree.write('AllStations.xml')
