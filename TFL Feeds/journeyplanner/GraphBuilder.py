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

    def __init__(self, station_list):
        """
        Intilise object.
        """
        self.journey_time_matrix = []
        self.my_station_list = station_list

    def build_graph(self):
        """
        For each pair of stations in the supplied list, create a
        Journey object and save the journey times in a list.
        Arguments:
        - `station_list`: the list of stations created by load_stations().
        """
        from Journey import Journey
        for i in range(len(self.my_station_list.get_list())):
            self.journey_time_matrix.append([])
            for j in range(len(self.my_station_list.get_list())):
                if i != j:
                    print "Journey:",\
                        self.my_station_list.get_list()[i][1].get_name(), \
                        "to",\
                        self.my_station_list.get_list()[j][1].get_name()

                    self.this_journey = Journey(self.my_station_list.get_list()[i][1],\
                                                    self.my_station_list.get_list()[j][1],\
                                                    "20130801",\
                                                    "0800")
                    self.this_journey.read_api()
                    self.journey_time_matrix[i].append(\
                        self.this_journey.get_journey_time())
                    self.this_journey.cleanup_files()
                else:
                    self.journey_time_matrix[i].append(0)

    def build_no_change_graph(self):
        """
        For each pair of stations in the supplied list, create a
        Journey object and save the journey times in a list.
        Arguments:
        - `station_list`: the list of stations created by load_stations().
        """
        from Journey import Journey
        for i in range(len(self.my_station_list.get_list())):
            self.journey_time_matrix.append([])
            for j in range(len(self.my_station_list.get_list())):
                if i != j:
                    print "Journey:",\
                        self.my_station_list.get_list()[i][1].get_name(), \
                        "to",\
                        self.my_station_list.get_list()[j][1].get_name()

                    self.this_journey = Journey(self.my_station_list.get_list()[i][1],\
                                                    self.my_station_list.get_list()[j][1],\
                                                    "20130801",\
                                                    "0800")
                    self.this_journey.read_api()
                    self.journey_time_matrix[i].append(\
                        self.this_journey.get_no_change_journey_time())
                    self.this_journey.cleanup_files()
                else:
                    self.journey_time_matrix[i].append(0)

    def export_to_gexf(self):
        """
        Export the generated graph to GEXF format used by gephi.
        """
        import time
        import subprocess
        import xml.etree.ElementTree as ET

        subprocess.call(['touch', 'TubeJourneyTimesGraph.gexf'])

        self.my_gexf = ET.Element('gexf',\
                                      {'xmlns': 'https://www.gexf.net/1.2draft',\
                                           'xmlns:xsi':\
                                           'http://www.w3.org/2001/XMLSchema-instance',\
                                           'xsi:schemaLocation': \
                                           'http://www.gexf.net/1.2draft \n \http://www.gexf.net/1.2draft/gexf.xsd',\
                                           'version': '1.2'})
        self.my_tree = ET.ElementTree(self.my_gexf)

        self.my_meta = ET.Element('meta', {'lastmodifieddate': time.strftime('%Y-%m-%d')})
        self.my_creator = ET.Element('creator')
        self.my_creator.text = "Andy Holt"
        self.my_description = ET.Element('description')
        self.my_description.text = "Graph of tube network"
        self.my_meta.append(self.my_creator)
        self.my_meta.append(self.my_description)
        self.my_gexf.append(self.my_meta)

        self.my_graph = ET.Element('graph', {'defaultedgetype': 'directed'})
        self.my_gexf.append(self.my_graph)

        self.my_nodes = ET.Element('nodes')
        self.my_graph.append(self.my_nodes)

        self.my_edges = ET.Element('edges')
        self.my_graph.append(self.my_edges)

        for i in range(len(self.journey_time_matrix)):
            self.new_node = ET.Element('node', {'id': str(i),\
                                                    'label': self.my_station_list.get_station(i)})
            self.my_nodes.append(self.new_node)
            for j in range(len(self.journey_time_matrix)):
                if self.journey_time_matrix[i][j] != 0:
                    self.edge_id = str((i * len(self.journey_time_matrix)) + j)
                    self.new_edge = ET.Element('edge', {'id': self.edge_id,\
                                                            'source': str(i),\
                                                            'target': str(j),\
                                                            'weight': str(round(self.journey_time_matrix[i][j],1))})
                    self.my_edges.append(self.new_edge)

        self.my_tree.write('TubeJourneyTimesGraph.gexf')
