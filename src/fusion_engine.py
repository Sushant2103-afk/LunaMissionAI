"""
LunaMission AI

Terrain Analysis Engine

Uses OHRC terrain parameters
to estimate landing safety.
"""

import pandas as pd


class TerrainEngine:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def calculate(self):

        terrain_scores = []
        terrain_risks = []

        for _, row in self.df.iterrows():

            score = 100

            # Slope penalty
            score -= row["Slope"] * 2

            # Roughness penalty
            if row["Roughness"] == "Medium":
                score -= 10
            elif row["Roughness"] == "High":
                score -= 20

            # Boulder penalty
            if row["BoulderDensity"] == "Medium":
                score -= 10
            elif row["BoulderDensity"] == "High":
                score -= 20

            score = max(score, 0)

            terrain_scores.append(score)

            if score >= 80:
                terrain_risks.append("Low")
            elif score >= 60:
                terrain_risks.append("Medium")
            else:
                terrain_risks.append("High")

        self.df["TerrainScore"] = terrain_scores
        self.df["TerrainRisk"] = terrain_risks

        return self.df