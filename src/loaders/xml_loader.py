"""
DFSAR XML Metadata Loader
Reads NASA PDS4 XML metadata.
"""

import xml.etree.ElementTree as ET


class XMLLoader:

    def __init__(self, xml_path):

        self.xml_path = xml_path

    def load(self):

        tree = ET.parse(self.xml_path)

        root = tree.getroot()

        metadata = {}

        namespace = {
            "pds": "http://pds.nasa.gov/pds4/pds/v1"
        }

        identification = root.find(
            "pds:Identification_Area",
            namespace
        )

        if identification is not None:

            for child in identification:

                tag = child.tag.split("}")[-1]

                metadata[tag] = child.text

        return metadata