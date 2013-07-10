#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python2 script
"""
OO and full version of journey planner scripts
"""
import urllib
import subprocess
import xml.etree.ElementTree as ET

class Journey(object):
    """ Class describing a journey from one station to another """

    def __init__(self, origin, destination, journey_date, journey_time):
        """
        Set up required journey attributes.
        """
        self.origin = origin
        self.destination = destination
        self.journey_date = str(journey_date)
        self.journey_time = str(journey_time)
        self.xml_file_name = self.origin + "-" + self.destination + \
            self.journey_date + self.journey_time + ".xml"

    def set_origin(self, origin):
        """
        Set origin station for journey.
        """
        self.origin = origin

    def set_destination(self, destination):
        """
        Set destination station for journey.
        """
        self.destination = destination

    def set_date(self, journey_date):
        """
        Set date of journey departure.
        format: YYYYMMDD
        """
        self.journey_date = str(journey_date)

    def set_time(self, journey_time):
        """
        Set time of journey departure.
        format: HHMM (24-hour)
        """
        self.journey_time = str(journey_time)

    def get_origin(self):
        """
        Returns string with origin station name.
        """
        return self.origin

    def get_destination(self):
        """
        Returns string with destination station name.
        """
        return self.destination

    def get_date(self):
        """
        Returns string with journey departure date.
        """
        return self.journey_date

    def get_time(self):
        """
        Returns string with journey departure time.
        """
        return self.journey_time

    def read_api(self):
        """
        Calls api and writes data to xml file.
        xml file name is: origin - destination date time
        """
        self.url_base = "http://jpapi.tfl.gov.uk/api/XML_TRIP_REQUEST2?language=en&sessionID=0"
        self.url_jstart = "&place_origin=London&type_origin=stop&name_origin="
        self.url_jend ="&place_destination=London&type_destination=stop&name_destination="
        self.url_date = "&itdDate="
        self.url_time = "&itdTime="

        self.url = self.url_base + self.url_jstart + urllib.quote(self.origin) \
            + self.url_jend + urllib.quote(self.destination) + self.url_date \
            + self.journey_date + self.url_time + self.journey_time

        self.plan = urllib.urlopen(self.url)

        subprocess.call(['touch', self.xml_file_name])
        self.xml_file = open(self.xml_file_name, 'r+')
        self.s = str(self.plan.read())
        self.xml_file.write(self.s)
        self.xml_file.close()

        # format xml file using xmllint command line tool
        subprocess.call(['touch', 'tmp.xml'])
        self.f = open('tmp.xml', 'r+')
        subprocess.call(['xmllint', '--format', self.xml_file_name], stdout=self.f)
        self.f.close()
        subprocess.call(['mv', 'tmp.xml', self.xml_file_name])

    def print_routes(self):
        """
        Prints out the suggested routes.
        Shows start time, travel time and no of changes.
        """
        self.journey_data = ET.parse(self.xml_file_name)
        self.journey_data_root = self.journey_data.getroot()

        self.route_list = self.journey_data_root.find('itdTripRequest')\
            .find('itdItinerary').find('itdRouteList')

        for route in self.route_list.findall('itdRoute'):
            print "Start Time:", \
                route.find('itdPartialRouteList').find('itdPartialRoute')\
                .find('itdPoint').find('itdDateTime').find('itdTime').get('hour'),\
                ":",\
                route.find('itdPartialRouteList').find('itdPartialRoute')\
                .find('itdPoint').find('itdDateTime').find('itdTime').get('minute'),\
                " Duration", route.get('publicDuration'),\
                " Changes:", route.get('changes')

    def get_journey_time(self):
        """
        Returns int with journey time in minutes.
        """
        self.journey_data = ET.parse(self.xml_file_name)
        self.journey_data_root = self.journey_data.getroot()

        self.route_list = self.journey_data_root.find('itdTripRequest')\
            .find('itdItinerary').find('itdRouteList')
        
        self.duration_list = []

        for route in self.route_list.findall('itdRoute'):
            self.time_list = route.get('publicDuration').split(':')
            self.duration_list.append((60*float(self.time_list[0])) \
                                          + float(self.time_list[1]))

        self.duration_sum = 0

        for element in self.duration_list:
            self.duration_sum = self.duration_sum + element

        self.duration_avg = self.duration_sum / len(self.duration_list)

        return self.duration_avg
