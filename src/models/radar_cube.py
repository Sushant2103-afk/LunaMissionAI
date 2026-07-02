"""
Radar Cube

Represents one DFSAR acquisition.
"""


class RadarCube:

    def __init__(

        self,

        hh,

        hv,

        vh,

        vv,

        metadata=None

    ):

        self.HH = hh
        self.HV = hv
        self.VH = vh
        self.VV = vv

        self.metadata = metadata

    @property
    def shape(self):

        return self.HH.shape

    @property
    def width(self):

        return self.HH.shape[1]

    @property
    def height(self):

        return self.HH.shape[0]

    def channels(self):

        return {

            "HH": self.HH,

            "HV": self.HV,

            "VH": self.VH,

            "VV": self.VV

        }

    def statistics(self):

        stats = {}

        for name, img in self.channels().items():

            stats[name] = {

                "min": img.min(),

                "max": img.max(),

                "shape": img.shape,

                "dtype": img.dtype

            }

        return stats

    def __getitem__(self, channel):

        return self.channels()[channel]