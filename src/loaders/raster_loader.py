"""
Generic Raster Loader

Reads GeoTIFF radar products.
"""

import rasterio


class RasterLoader:

    def __init__(self, raster_path):

        self.raster_path = raster_path

    def load(self):

        dataset = rasterio.open(self.raster_path)

        return dataset