#!/usr/bin/python
# TODO: use an append method to add stations
# TODO: use a more robust method to select line sub-element than __getitem__(1)
"""
Add the line data for each station
"""
import xml.etree.ElementTree as ET

allstations_tree = ET.parse('AllStations.xml')
allstations_root = allstations_tree.getroot()

Bakerloo_tree = ET.parse('Bakerloo.xml')
Bakerloo_root = Bakerloo_tree.getroot()
Central_tree = ET.parse('Central.xml')
Central_root = Central_tree.getroot()
Circle_tree = ET.parse('Circle.xml')
Circle_root = Circle_tree.getroot()
District_tree = ET.parse('District.xml')
District_root = District_tree.getroot()
HamAndCity_tree = ET.parse('HamAndCity.xml')
HamAndCity_root = HamAndCity_tree.getroot()
Jubilee_tree = ET.parse('Jubilee.xml')
Jubilee_root = Jubilee_tree.getroot()
Metropolitan_tree = ET.parse('Metropolitan.xml')
Metropolitan_root = Metropolitan_tree.getroot()
Northern_tree = ET.parse('Northern.xml')
Northern_root = Northern_tree.getroot()
Piccadilly_tree = ET.parse('Piccadilly.xml')
Piccadilly_root = Piccadilly_tree.getroot()
Victoria_tree = ET.parse('Victoria.xml')
Victoria_root = Victoria_tree.getroot()
WaterlooAndCity_tree = ET.parse('WaterlooAndCity.xml')
WaterlooAndCity_root = WaterlooAndCity_tree.getroot()

for station in allstations_root:
    for BakerlooStation in Bakerloo_root:
        if station.attrib == BakerlooStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Bakerloo'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Bakerloo'

    for CentralStation in Central_root:
        if station.attrib == CentralStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Central'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Central'

    for CircleStation in Circle_root:
        if station.attrib == CircleStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Circle'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Circle'

    for DistrictStation in District_root:
        if station.attrib == DistrictStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'District'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' District'

    for HamAndCityStation in HamAndCity_root:
        if station.attrib == HamAndCityStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'HamAndCity'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' HamAndCity'

    for JubileeStation in Jubilee_root:
        if station.attrib == JubileeStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Jubilee'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Jubilee'

    for MetropolitanStation in Metropolitan_root:
        if station.attrib == MetropolitanStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Metropolitan'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Metropolitan'

    for NorthernStation in Northern_root:
        if station.attrib == NorthernStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Northern'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Northern'

    for PiccadillyStation in Piccadilly_root:
        if station.attrib == PiccadillyStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Piccadilly'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Piccadilly'

    for VictoriaStation in Victoria_root:
        if station.attrib == VictoriaStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'Victoria'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' Victoria'

    for WaterlooAndCityStation in WaterlooAndCity_root:
        if station.attrib == WaterlooAndCityStation.attrib:
            if str(station.__getitem__(1).text) == "None":
                station.__getitem__(1).text = 'WaterlooAndCity'
            else:
                station.__getitem__(1).text = str(station.__getitem__(1).text) + ' WaterlooAndCity'

allstations_tree.write('Test1.xml')
