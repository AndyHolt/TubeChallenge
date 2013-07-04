#!/usr/bin/python3
"""
Fetch train arrival news from TFL
"""
import urllib.request
import xml.etree.ElementTree as ET

# B = bakerloo line
train_prediction =urllib.request.urlopen(
    'http://cloud.tfl.gov.uk/TrackerNet/PredictionSummary/B')

print(train_prediction.info())

output_file = open('trainpredictionsummary_out.xml',mode='wb')
output_file.write(train_prediction.read())

train_prediction_tree = ET.parse('trainpredictionsummary_out.xml')
train_prediction_root = train_prediction_tree.getroot()

for station in train_prediction_root.findall('S'):
    print(station.get('N'))
    for platform in station.findall('P'):
        print(platform.get('N'))
        for train in platform.findall('T'):
            print("Train expected:", train.get('C'))
        print('\n')
