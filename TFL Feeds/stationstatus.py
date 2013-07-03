#!/usr/bin/python3
"""
Fetch news from TFL and display in terminal
"""
import urllib.request

station_status = urllib.request.urlopen('http://cloud.tfl.gov.uk/TrackerNet/StationStatus')

output_file = open('stationstatus_out.xml',mode='wb')

#print(station_status.read())
output_file.write(station_status.read())
