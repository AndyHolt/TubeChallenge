#!/usr/bin/python
"""
Build graph of tube network.

Builds graph using Station, StationList and Journey classes.
Exports to GEXF format for use in Gephi.
May also add export to something for Matlab use.
"""
# Author: Andy Holt
# Date: Sat 13 Jul 2013 23:24
# Useage: Only to be run on CUED servers.

class GraphBuilder(object):
    """
    Build a graph of the tube network to export to GEXF format.
    """

    def __init__(self, ):
        """
        Intilise object.
        """
        self.journey_time_matrix = []

    def build_graph(self, station_list):
        """
        For each pair of stations in the supplied list, create a
        Journey object and save the journey times in a list.
        Arguments:
        - `station_list`: the list of stations created by load_stations().
        """
        from Journey import Journey
        for i in range(len(station_list.get_list())):
            self.journey_time_matrix.append([])
            for j in range(len(station_list.get_list())):
                if i != j:
                    self.this_journey = Journey(station_list.get_list()[i][1],\
                                                    station_list.get_list()[j][1],\
                                                    "20130801",\
                                                    "0800")
                    self.this_journey.read_api()
                    self.journey_time_matrix[i].append(\
                        self.this_journey.get_journey_time())
                else:
                    self.journey_time_matrix[i].append(0)
