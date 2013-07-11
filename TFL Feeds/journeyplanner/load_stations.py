#!/usr/bin/python
# ONLY TO BE RUN ON CUED SERVERS!
# python 2 script
"""
Create objects for the 270 stations, loading into list.
"""
# import Station, StationList and Journey classes
from Station import *
from Journey import *
import xml.etree.elementtree as ET

London270 = ET.parse('London270.xml')
London270_root = London270.getroot()


