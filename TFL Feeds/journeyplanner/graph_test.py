#!/usr/bin/python
"""
Test file for building a small version of the network graph.

Take the first 6 stations from the 270 requried and build the network
for them. Scale up from here!
"""
# Author: Andy Holt
# Date: Sun 14 Jul 2013 01:17
# Usage: Only to be run on CUED servers.

from Station import Station, StationList
from Journey import Journey
from GraphBuilder import GraphBuilder

big_station_list = StationList()
big_station_list.load_270()

test_station_list = StationList()
test_station_list.add(big_station_list.get_list()[0][1])
test_station_list.add(big_station_list.get_list()[1][1])
test_station_list.add(big_station_list.get_list()[2][1])
test_station_list.add(big_station_list.get_list()[3][1])
test_station_list.add(big_station_list.get_list()[4][1])
test_station_list.add(big_station_list.get_list()[5][1])

my_graph_builder = GraphBuilder(test_station_list)
my_graph_builder.build_part_graph()

print my_graph_builder.journey_time_matrix

