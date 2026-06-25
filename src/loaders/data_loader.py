"""
Universal Data Loader

Every engine receives the same dataframe
regardless of the input dataset.
"""

from src.loaders.sri_loader import SRILoader
from src.loaders.gri_loader import GRILoader
from src.loaders.sli_loader import SLILoader


class DataLoader:

    @staticmethod
    def load(dataset_type, path):

        dataset_type = dataset_type.upper()

        if dataset_type == "SRI":
            return SRILoader(path).load()

        elif dataset_type == "GRI":
            return GRILoader(path).load()

        elif dataset_type == "SLI":
            return SLILoader(path).load()

        else:
            raise ValueError(
                f"Unsupported dataset: {dataset_type}"
            )