#!/usr/bin/python
"""
Functions for analysis of data.
"""
import xml.etree.ElementTree as ET
import matplotlib.pyplot as pp

class GraphAnalysis(object):
    """
    Class of methods to analyse the graph.
    """

    def __init__(self, filename):
        """
        Import the tree, ready for some analysis.
        """
        self._filename = filename

        # default gexf namespace
        self.ns0 = "{https://www.gexf.net/1.2draft}"

        self.graph_tree = ET.parse(self._filename)
        self.graph_root = self.graph_tree.getroot()

        self.nodes_root = self.graph_root.find(self.ns0 + "graph")\
            .find(self.ns0 + "nodes")
        self.edges_root = self.graph_root.find(self.ns0 + "graph")\
            .find(self.ns0 + "edges")

    def journey_times_hist(self):
        self.journey_times = []
        for journey in self.edges_root:
            self.journey_times.append(float(journey.get('weight')))

        pp.hist(self.journey_times, 10)
        pp.xlabel('Journey Time (minutes)')
        pp.ylabel('Number of Journeys')
        pp.show()
