#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
Get some data from TLF feed
"""
import urllib
import xml.etree.ElementTree as ET

plan = urllib.urlopen(
    'http://jpapi.tfl.gov.uk/api/XML_TRIP_REQUEST2?language=en&sessionID=0&place_origin=London&type_origin=stop&name_origin=Amersham%20Undergroud%20Station&place_destination=London&type_destination=stop&name_destination=Chalfont%20%26%20Latimer%20Underground%20Station&itdDate=20130711&itdTime=0800')
f = open('journeyplannertest.xml', 'r+')
s = str(plan.read())
f.write(s)
f.close()

print(plan.info())
