#!/usr/bin/python3
"""
Test file for graph analysis class methods.
"""
# Author: Andy Holt
# Date: Mon 22 Jul 2013 19:28
# Usage: Run in python3


from graph_analysis import *

ga = GraphAnalysis('TubeJourneyTimesGraph_270.gexf')

ga.station_connectivity_hist()
