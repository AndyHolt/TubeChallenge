#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python 2 script
"""
Create objects for the 270 stations, loading into list.
"""
# import Station, StationList and Journey classes
from Station import *
from Journey import *
import xml.etree.ElementTree as ET

London270 = ET.parse('London270.xml')
London270_root = London270.getroot()

Bakerloo = ET.parse('Bakerloo.xml')
Bakerloo_root = Bakerloo.getroot()
Central = ET.parse('Central.xml')
Central_root = Central.getroot()
Circle = ET.parse('Circle.xml')
Circle_root = Circle.getroot()
District = ET.parse('District.xml')
District_root = District.getroot()
HamAndCity = ET.parse('HamAndCity.xml')
HamAndCity_root = HamAndCity.getroot()
Jubilee = ET.parse('Jubilee.xml')
Jubilee_root = Jubilee.getroot()
Metropolitan = ET.parse('Metropolitan.xml')
Metropolitan_root = Metropolitan.getroot()
Northern = ET.parse('Northern.xml')
Northern_root = Northern.getroot()
Piccadilly = ET.parse('Piccadilly.xml')
Piccadilly_root = Piccadilly.getroot()
Victoria = ET.parse('Victoria.xml')
Victoria_root = Victoria.getroot()
WaterlooAndCity = ET.parse('WaterlooAndCity.xml')
WaterlooAndCity_root = WaterlooAndCity.getroot()

line_list = [ ["Bakerloo", Bakerloo_root],
              ["Central", Central_root],
              ["Circle", Circle_root],
              ["District", District_root],
              ["HammersmithAndCity", HamAndCity_root],
              ["Jubilee", Jubilee_root],
              ["Metropolitan", Metropolitan_root],
              ["Northern", Northern_root],
              ["Piccadilly", Piccadilly_root],
              ["Victoria", Victoria_root],
              ["WaterlooAndCity", WaterlooAndCity_root] ]

my_station_list = StationList()

for station in London270.findall('station'):
    station_name = station.get('name')
    station_osx = station.find('osx').text
    station_osy = station.find('osy').text
    station_latitude = station.find('latitude').text
    station_longitude = station.find('longitude').text
    station_zone = [int(station.find('zone').text.replace("/","")[i]) \
                        for i in range(len(station.find('zone').text\
                                               .replace("/","")))]
    station_lines = []
    for i in range(len(line_list)):
        line_stations = []
        for a_station in line_list[i][1].findall('station'):
            if a_station.get('name') == station_name:
                station_lines.append(line_list[i][0])
    my_station_list.add_new(station_name,\
                            station_lines, \
                            station_zone,
                            station_osx,
                            station_osy,
                            station_latitude,
                            station_longitude)

for i in range(len(my_station_list.get_list())):
    print my_station_list.get_station(i), "\n"
