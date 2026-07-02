import glob
import os

from src.loaders.raster_loader import RasterLoader
from src.models.radar_cube import RadarCube


class RadarLoader:

    def __init__(self, dataset_folder):
        self.dataset_folder = dataset_folder

    def load(self):

        hh_path = glob.glob(
            os.path.join(self.dataset_folder, "*hh*.tif")
        )[0]

        hv_path = glob.glob(
            os.path.join(self.dataset_folder, "*hv*.tif")
        )[0]

        vh_path = glob.glob(
            os.path.join(self.dataset_folder, "*vh*.tif")
        )[0]

        vv_path = glob.glob(
            os.path.join(self.dataset_folder, "*vv*.tif")
        )[0]

        hh = RasterLoader(hh_path).load().read(1)
        hv = RasterLoader(hv_path).load().read(1)
        vh = RasterLoader(vh_path).load().read(1)
        vv = RasterLoader(vv_path).load().read(1)

        return RadarCube(
            hh=hh,
            hv=hv,
            vh=vh,
            vv=vv
        )