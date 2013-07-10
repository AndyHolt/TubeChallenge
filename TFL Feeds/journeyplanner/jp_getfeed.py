#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
Get some data from TLF feed
"""
import urllib
import xml.etree.ElementTree as ET

station_start = "Amersham Underground Station"
station_end = "Chalfont & Latimer Underground Station"
journey_date = "20130711"
journey_time = "0800"

url_base = "http://jpapi.tfl.gov.uk/api/XML_TRIP_REQUEST2?language=en&sessionID=0"
url_jstart = "&place_origin=London&type_origin=stop&name_origin="
url_jend ="&place_destination=London&type_destination=stop&name_destination="
url_date = "&itdDate="
url_time = "&itdTime="

url = url_base + url_jstart + urllib.quote(station_start) + url_jend + \
    urllib.quote(station_end) + url_date + journey_date + url_time + \
    journey_time

plan = urllib.urlopen(url)
f = open('journeyplannertest.xml', 'r+')
s = str(plan.read())
f.write(s)
f.close()

print(plan.info())
