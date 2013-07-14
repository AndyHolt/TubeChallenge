# ONLY TO BE RUN ON CUED SERVERS!
# python2 class file
"""
Class definition for Journey between two stations at a particular date and time.
"""
import urllib
import subprocess
import xml.etree.ElementTree as ET

class Journey(object):
    """
    Class describing a journey from one station to another.
    """

    def __init__(self, origin, destination, journey_date, journey_time):
        """
        Set up required journey attributes.
        """
        self.origin = origin.get_name()
        self.destination = destination.get_name()
        self.journey_date = str(journey_date)
        self.journey_time = str(journey_time)
        self.xml_file_name = self.origin + "-" + self.destination + \
            self.journey_date + self.journey_time + ".xml"

    def set_origin(self, origin):
        """
        Set origin station for journey.
        """
        self.origin = origin.get_name()

    def set_destination(self, destination):
        """
        Set destination station for journey.
        """
        self.destination = destination.get_name()

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
        # ElementTree doesn't write to file properly if there is
        # already data in the file, so cleanup before writing new.
        self.cleanup_files()

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

    def cleanup_files(self):
        """
        read_api method creates an xml file for the journey. Creating
        many journeys produces LOTS of xml files cluttering up
        directory, this method can delete the file once we've got the
        neccessary information
        """
        subprocess.call(['rm', '-f', self.xml_file_name])

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

    def get_times_cross_section(self):
        """
        Get a selection of times for the journey.
        Find time on Mon, Thu and Sat at 0800, 1300 and 1800.
        """
        self.times_array = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
        for day in [ [0, "Mon", "15"], [1, "Thu", "18"], [2, "Sat", "20"] ]:
            self.set_date("201307" + day[2])
            for time in [[0, "0800"], [1, "1300"], [2, "1800"]]:
                self.set_time(time[1])
                self.times_array[day[0]][time[0]] = self.get_journey_time()

        self.org_file_name = self.origin + "-" + self.destination \
            + "_crosssection.org"
        subprocess.call(['touch', self.org_file_name])
        self.org_file = open(self.org_file_name, 'r+')
        self.org_file.write("|---+---+---+---|\n")
        self.org_file.write("| Day | 0800 | 1300 | 1800 |\n")
        self.org_file.write("|---+---+---+---|\n")
        self.org_file.write("| Mon | " + str(self.times_array[0][0]) + " | " \
                                       + str(self.times_array[0][1]) + " | " \
                                       + str(self.times_array[0][2]) + " |\n")
        self.org_file.write("| Thu | " + str(self.times_array[1][0]) + " | " \
                                       + str(self.times_array[1][1]) + " | " \
                                       + str(self.times_array[1][2]) + " |\n")
        self.org_file.write("| Fri | " + str(self.times_array[2][0]) + " | " \
                                       + str(self.times_array[2][1]) + " | " \
                                       + str(self.times_array[2][2]) + " |\n")
        self.org_file.write("|---+---+---+---|\n")
        self.org_file.close()
