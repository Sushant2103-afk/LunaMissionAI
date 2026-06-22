"""
LunaMission AI

Rover Traverse Planner
"""

import pandas as pd


class RoverEngine:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    def calculate(self):

        distance = []
        energy = []
        risk = []

        for _, row in self.df.iterrows():

            # Synthetic demo values

            d = round(100 + row["Slope"] * 25, 2)

            e = round(d * 0.12, 2)

            if row["Slope"] <= 5:
                r = "Low"

            elif row["Slope"] <= 10:
                r = "Medium"

            else:
                r = "High"

            distance.append(d)
            energy.append(e)
            risk.append(r)

        self.df["TraverseDistance"] = distance
        self.df["EnergyCost"] = energy
        self.df["TraverseRisk"] = risk

        return self.df