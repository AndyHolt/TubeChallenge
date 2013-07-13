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
        self.zone = []
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
        Argument "line" is a list of lines. 
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
        Validate each zone in list and set.
        """
        for i in range(len(zone)):
            if 0 < zone[i] < 10:
                self.zone.append(zone[i])
            else:
                print "Zone value:", zone, "is invalid"

    def add_zone(self, zone):
        """
        Validate and add to list of zones.
        """
        if (0 < zone < 10) & (zone not in self.zone):
            self.zone.append(zone)
        else:
            print "Zone value:", zone, "is invalid or already set"

    def remove_zone(self, zone):
        """
        Remove zone from \one list, if set.
        """
        if zone in self.zone:
            self.zone.remove(zone)

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
        Return list of line names.
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
    Class defining a list of station objects, unique id and station
    name.
    """
    def __init__(self):
        self.station_list = []

    def add(self, station):
        self.id = len(self.station_list)
        self.station_list.append([self.id, station])

    def add_new(self, name, line, zone, os_x, os_y, latitude, longitude):
        self.my_station = Station(name, line, zone, os_x, os_y,\
                                      latitude, longitude)
        self.add(self.my_station)

    def get_id(self, station_name):
        """
        Find the id associated with a station.
        """
        for element in self.station_list:
            if element[1].get_name() == station_name:
                return element[0]
        print "station:", station_name, "not found."

    def get_station(self, idn):
        """
        Find the name of the station at a given index
        """
        if -1 <idn < len(self.station_list):
            return self.station_list[idn][1].get_name()
        else:
            print "ID:", idn, "isn't a valid station ID."

    def fetch_station(self, station_name):
        """
        Return the object describing a station with a given name
        """
        for element in self.station_list:
            if element[1].get_name() == station_name:
                return element[1]
        print "Station:", station_name, "not found."

    def get_list(self):
        """
        Return whole list of stations
        """
        return self.station_list
