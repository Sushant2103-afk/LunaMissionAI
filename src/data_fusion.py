import pandas as pd

class DataFusion:

    REQUIRED_COLUMNS = [
        "Region",
        "Latitude",
        "Longitude",
        "CPR",
        "DOP",
        "Slope",
        "Roughness",
        "BoulderDensity",
        "ShadowCoverage",
    ]

    @staticmethod
    def load():

        ice_df = pd.read_csv("data/sample/sample_lunar_data.csv")
        terrain_df = pd.read_csv("data/sample/sample_terrain_data.csv")

        df = pd.merge(ice_df, terrain_df, on="Region")

        missing = [
            col for col in DataFusion.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        return df