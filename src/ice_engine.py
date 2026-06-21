"""
LunaMission AI

Ice Confidence Engine

Calculates probability of subsurface ice
using CPR, DOP and Slope.
"""

import pandas as pd


class IceEngine:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    def calculate(self):

        scores = []
        labels = []

        for _, row in self.df.iterrows():

            score = 0

            # CPR Score
            if row["CPR"] >= 1.2:
                score += 50

            elif row["CPR"] >= 1:
                score += 35

            else:
                score += 15

            # DOP Score
            if row["DOP"] <= 0.10:
                score += 30

            elif row["DOP"] <= 0.13:
                score += 20

            else:
                score += 5

            # Slope Score
            if row["Slope"] <= 5:
                score += 20

            elif row["Slope"] <= 10:
                score += 10

            else:
                score += 2

            scores.append(score)

            # Confidence Label
            if score >= 90:
                labels.append("High")

            elif score >= 70:
                labels.append("Medium")

            else:
                labels.append("Low")

        self.df["IceScore"] = scores
        self.df["Confidence"] = labels

        return self.df