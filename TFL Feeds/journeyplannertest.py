#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
Get some data from TLF feed
"""
import urllib

plan = urllib.urlopen(
    'http://jpapi.tfl.gov.uk/api/XML_TRIP_REQUEST2?language=en&sessionID=0&place_origin=London&type_origin=stop&name_origin=Alexander%20Road&place_destination=London&type_destination=stop&name_destination=Price%20Of%20Wales%20Gate&itdDate=20130706&itdTime=0800')
f = open('journeyplannertest.xml', 'r+')
s = str(plan.read())
f.write(s)
f.close()
