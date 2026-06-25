"""
SRI Loader
"""

import pandas as pd


class SRILoader:

    def __init__(self, path):

        self.path = path

    def load(self):

        df = pd.DataFrame(

            columns=[

                "Region",

                "Latitude",

                "Longitude",

                "HH",

                "HV",

                "VH",

                "VV",

                "IncidenceAngle",

                "Mask"

            ]

        )

        return df