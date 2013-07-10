#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
Read the data written to xml file by getfeed script and print the
important bits.
"""
import xml.etree.ElementTree as ET

journey_data  = ET.parse('journeyplannertest.xml')
journey_data_root = journey_data.getroot()

route_list = journey_data_root.find('itdTripRequest').find('itdItinerary').find('itdRouteList')

for route in route_list.findall('itdRoute'):
    print "Start Time:", route.find('itdPartialRouteList').find('itdPartialRoute').find('itdPoint').find('itdDateTime').find('itdTime').get('hour'),\
        ":", route.find('itdPartialRouteList').find('itdPartialRoute').find('itdPoint').find('itdDateTime').find('itdTime').get('minute'),\
        " Duration:", route.get('publicDuration'), " Changes:", route.get('changes') 

