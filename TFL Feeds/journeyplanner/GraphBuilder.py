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

    def build_full_graph(self):
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

    def build_full_no_change_graph(self):
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

    def build_part_graph(self):
        """
        Start from what has already been put into xml file and
        continue, writing to the xml file after each journey.
        This allows getting the full graph (eventually) despite SSH
        timeout and broken pipes etc.
        """
        from Journey import Journey
        import xml.etree.ElementTree as ET

        self.my_tree = ET.parse('TubeJourneyTimesGraph.gexf')
        self.my_gexf = self.my_tree.getroot()
        self.my_meta = self.my_gexf.find('{https://www.gexf.net/1.2draft}meta')
        self.my_graph = self.my_gexf.find('{https://www.gexf.net/1.2draft}graph')
        self.my_nodes = self.my_graph.find('{https://www.gexf.net/1.2draft}nodes')
        self.my_edges = self.my_graph.find('{https://www.gexf.net/1.2draft}edges')

        self.id_list = []
        for edge in self.my_edges:
            self.id_list.append(int(edge.get('id')))

        if len(self.id_list) != 0:
            self.max_id = self.id_list.pop()
        else:
            self.max_id = 0
            self.journey_time_matrix.append([])
            self.add_xml_node(0)

        self.i_start = self.max_id / len(self.my_station_list.get_list())
        self.j_start = self.max_id % len(self.my_station_list.get_list())

        for cols in range(self.i_start+1):
            self.journey_time_matrix.append([])
            for rows in range(self.j_start+1):
                self.journey_time_matrix[cols].append([])

        # finish current origin:
        for j in range(self.j_start+1, len(self.my_station_list.get_list())):
            if (self.i_start != j)\
                    and not(self.i_start==94 and j==95) and not(self.i_start==95 and j==94)\
                    and not(self.i_start==102 and j==103) and not(self.i_start==103 and j==102)\
                    and not(self.i_start==102 and j==104) and not(self.i_start==104 and j==102)\
                    and not(self.i_start==103 and j==104) and not(self.i_start==104 and j==103)\
                    and not(self.i_start==171 and j==172) and not(self.i_start==172 and j==171)\
                    and not(self.i_start==198 and j==199) and not(self.i_start==199 and j==198)\
                print "Journey:",\
                    self.my_station_list.get_list()[self.i_start][1].get_name(), \
                    "to",\
                    self.my_station_list.get_list()[j][1].get_name()

                self.this_journey = Journey(self.my_station_list\
                                                .get_list()[self.i_start][1],\
                                                self.my_station_list\
                                                .get_list()[j][1],\
                                                "20130801",\
                                                "0800")
                self.this_journey.read_api()
                self.journey_time_matrix[self.i_start].append(\
                    self.this_journey.get_no_change_journey_time())
                self.this_journey.cleanup_files()

            else:
                self.journey_time_matrix[self.i_start].append(0)

            if self.journey_time_matrix[self.i_start][j] != 0:
                self.add_xml_edge(self.i_start,j)

        # then do the rest:
        for i in range(self.i_start + 1, len(self.my_station_list.get_list())):
            self.journey_time_matrix.append([])
            self.add_xml_node(i)
            for j in range(len(self.my_station_list.get_list())):
                if (i != j)\
                        and not(i==94 and j==95) and not(i==95 and j==94)\
                        and not(i==102 and j==103) and not(i==103 and j==102)\
                        and not(i==102 and j==104) and not(i==104 and j==103)\
                        and not(i==103 and j==104) and not(i==104 and j==103)\
                        and not(i==171 and j==172) and not(i==172 and j==171)\
                        and not(i==198 and j==199) and not(i==199 and j==198)\
                    print "Journey:",\
                        self.my_station_list.get_list()[i][1].get_name(), \
                        "to",\
                        self.my_station_list.get_list()[j][1].get_name()

                    self.this_journey = Journey(self.my_station_list\
                                                    .get_list()[i][1],\
                                                    self.my_station_list\
                                                    .get_list()[j][1],\
                                                    "20130801",\
                                                    "0800")
                    self.this_journey.read_api()
                    self.journey_time_matrix[i].append(\
                        self.this_journey.get_no_change_journey_time())
                    self.this_journey.cleanup_files()

                else:
                    self.journey_time_matrix[i].append(0)

                if self.journey_time_matrix[i][j] != 0:
                    self.add_xml_edge(i,j)


    def export_to_gexf(self):
        """
        Export the generated graph to GEXF format used by gephi.
        """
        import time
        import subprocess
        import xml.etree.ElementTree as ET

        self.begin_xml_file()

        for i in range(len(self.journey_time_matrix)):
            self.new_node = ET.Element('node', {'id': str(i),\
                                                    'label':\
                                                    self.my_station_list\
                                                    .get_station(i)})
            self.my_atts = ET.Element('attvalues')
            self.my_stn_lat = ET.Element('attvalue', {'for': 'latitude',\
                                                      'value':\
                                                      str(self.my_station_list\
                                                              .fetch_station_id(i)\
                                                              .get_lat_long()[0])})
            self.my_stn_long = ET.Element('attvalue', {'for': 'longitude',\
                                                           'value':\
                                                           str(self.my_station_list\
                                                                   .fetch_station_id(i)\
                                                                   .get_lat_long()[1])})
            self.my_atts.append(self.my_stn_lat)
            self.my_atts.append(self.my_stn_long)
            self.new_node.append(self.my_atts)
            self.my_nodes.append(self.new_node)
            for j in range(len(self.journey_time_matrix)):
                if self.journey_time_matrix[i][j] != 0:
                    self.edge_id = str((i * len(self.journey_time_matrix)) + j)
                    self.new_edge = ET.Element('edge', {'id': self.edge_id,\
                                                            'source': str(i),\
                                                            'target': str(j),\
                                                            'weight':\
                                                            str(round(self.journey_time_matrix[i][j],1))})
                    self.my_edges.append(self.new_edge)

        self.my_tree.write('TubeJourneyTimesGraph.gexf')


    def begin_xml_file(self):
        """
        Create a new xml file and the appropriate meta data.
        Does not need to be called every time the program is
        run - only if there is no starting tree.
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

        self.my_attributes = ET.Element('attributes', {'class': 'node'})
        self.my_lat = ET.Element('attribute',\
                                     {'id': 'latitutde', 'title': 'latitude', 'type':'double'})
        self.my_long = ET.Element('attribute',\
                                      {'id': 'longitude', 'title': 'longitude', 'type':'double'})
        self.my_attributes.append(self.my_lat)
        self.my_attributes.append(self.my_long)
        self.my_graph.append(self.my_attributes)

        self.my_nodes = ET.Element('nodes')
        self.my_graph.append(self.my_nodes)

        self.my_edges = ET.Element('edges')
        self.my_graph.append(self.my_edges)

        self.my_tree.write('TubeJourneyTimesGraph.gexf')


    def add_xml_node(self, i):
        """
        Add a new station to the xml file and store.
        """
        import xml.etree.ElementTree as ET
        self.new_node = ET.Element('node', {'id': str(i),\
                                                'label':\
                                                self.my_station_list.get_station(i)})
        self.my_atts = ET.Element('attvalues')
        self.my_stn_lat = ET.Element('attvalue', {'for': 'latitude',\
                                                      'value':\
                                                      str(self.my_station_list.fetch_station_id(i)\
                                                              .get_lat_long()[0])})
        self.my_stn_long = ET.Element('attvalue', {'for': 'longitude',\
                                                       'value':\
                                                       str(self.my_station_list.fetch_station_id(i)\
                                                               .get_lat_long()[1])})
        self.my_atts.append(self.my_stn_lat)
        self.my_atts.append(self.my_stn_long)
        self.new_node.append(self.my_atts)
        self.my_nodes.append(self.new_node)

        self.my_tree.write('TubeJourneyTimesGraph.gexf')

    def add_xml_edge(self, i, j):
        """
        Add a new journey to the xml file and store.
        """
        import xml.etree.ElementTree as ET

        self.edge_id = str((i * len(self.my_station_list.get_list())) + j)
        self.new_edge = ET.Element('edge', {'id': self.edge_id,\
                                                'source': str(i),\
                                                'target': str(j),\
                                                'weight': str(round(self.journey_time_matrix[i][j],1))})
        self.my_edges.append(self.new_edge)

        self.my_tree.write('TubeJourneyTimesGraph.gexf')
