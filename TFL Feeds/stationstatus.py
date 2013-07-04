#!/usr/bin/python3
"""
Fetch news from TFL and display in terminal
"""
import urllib.request
import xml.etree.ElementTree as ET

station_status = urllib.request.urlopen('http://cloud.tfl.gov.uk/TrackerNet/StationStatus')

print(station_status.info())

output_file = open('stationstatus_out.xml',mode='wb')

#print(station_status.read())
output_file.write(station_status.read())

station_data = ET.parse('stationstatus_out.xml')
station_data_root = station_data.getroot()

# setup namespace abbrev for default namespace.
dftns = '{http://webservices.lul.co.uk/}'

for station_status_id in station_data_root.findall(dftns+'StationStatus'):
    print(station_status_id.find(dftns+'Station').get('Name'))

