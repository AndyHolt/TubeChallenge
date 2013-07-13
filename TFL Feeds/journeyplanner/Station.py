# ONLY TO BE RUN ON CUED SERVERS!
# python2 class file
"""
Class definition for a station and all required data of it.
"""

class Station(object):
    """
    Class describing a station
    """
    def __init__(self, name, line, zone, os_x, os_y, latitutde, longitude):
        """
        Set up required station attributes.
        """
        self.set_name(name)
        self.set_line(line)
        self.set_zone(zone)
        self.set_os(os_x, os_y)
        self.set_lat_long(latitutde, longitude)

    def set_name(self, name):
        """
        Set name of the station.
        """
        self.name = name

    def set_line(self, line):
        """
        Validate line and set.
        Argument "Line" is a list of lines. 
        """
        self.lines = []
        self.line_list_all = ["Bakerloo", "Central", "Circle", "District", \
                              "HammersmithAndCity", "Jubilee", "Metropolitan", \
                              "Northern", "Piccadilly", "Victoria", \
                              "WaterlooAndCity"]

        for aline in line:
            if aline in self.line_list_all:
                self.lines.append(aline)
            else:
                print "Line name:", aline,  "is invalid."

    def set_zone(self, zone):
        """
        Validate the zone and set.
        """
        if 0 < zone < 10:
            self.zone = zone
        else:
            print "Zone value:", zone, "is invalid"

    def set_os(self, os_x, os_y):
        """
        Set position in os coords.
        """
        self.os_x = os_x
        self.os_y = os_y

    def set_lat_long(self, latitude, longitude):
        """
        Set position in lat-long coords
        """
        self.latitude = latitude
        self.longitude = longitude

    def get_name(self):
        """
        Return station name.
        """
        return self.name

    def get_line(self):
        """
        Return line name.
        """
        return self.lines

    def get_zone(self):
        """
        Return int of zone number.
        """
        return self.zone

    def get_os(self):
        """
        Return list of [os_x, os_y] as strings.
        """
        return [self.os_x, self.os_y]

    def get_lat_long(self):
        """
        Return list of [latitude, longitude] as strings. 
        """
        return [self.latitude, self.longitude]

    def add_line(self, aline):
        """
        Add a single line to the list of lines the station is on.
        """
        if aline in self.lines:
            print "Line:", aline, "is already in list."
        else:
            self.lines.append(aline)

class StationList(object):
    """
    Class defining a list of station objects and unique id
    """
    def __init__(self):
        self.station_list = []

    def add(self, station):
        self.id = len(self.station_list)
        self.station_list.append([self.id, station])

    def get_id(self, station):
        """
        Find the id associated with a station.
        """
        for element in self.station_list:
            if element[1] == station:
                return element[0]
        print "station:", station, "not found."

    def get_station(self, idn):
        """
        Find the station at a given index
        """
        return self.station_list[idn]

    def get_list(self):
        """
        Return whole list of stations
        """
        return self.station_list
