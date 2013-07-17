#!/usr/bin/python
"""
Build graph of 270 stations. Only produce an edge if there is a direct
connection between the stations.
"""
# Author: Andy Holt
# Date: Tue 16 Jul 2013 18:27
# Usage: Only to be run on CUED servers.

from Station import Station, StationList
from Journey import Journey
from GraphBuilder import GraphBuilder

full_station_list = StationList()
full_station_list.load_270()

my_graph_builder = GraphBuilder(full_station_list)
my_graph_builder.build_part_graph()

#print my_graph_builder.journey_time_matrix

