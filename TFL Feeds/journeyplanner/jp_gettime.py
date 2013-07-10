#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
Read the data written to xml file by getfeed script and find the
average journey time of those given.
"""
import xml.etree.ElementTree as ET

journey_data  = ET.parse('journeyplannertest.xml')
journey_data_root = journey_data.getroot()

route_list = journey_data_root.find('itdTripRequest').find('itdItinerary').find('itdRouteList')

duration_list = []

for route in route_list.findall('itdRoute'):
    time_list = route.get('publicDuration').split(':')
    duration_list.append(60*float(time_list[0]) + float(time_list[1]))

duration_sum = 0

for element in duration_list:
    duration_sum = duration_sum + element

duration_avg = duration_sum / len(duration_list)

print "Average journey length is: ", duration_avg

