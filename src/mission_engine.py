"""
LunaMission AI

Mission Decision Engine

Combines Ice Confidence,
Landing Suitability and
Rover Traverse Risk.
"""


class MissionEngine:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    def calculate(self):

        rover_score = []

        for risk in self.df["TraverseRisk"]:

            if risk == "Low":
                rover_score.append(100)

            elif risk == "Medium":
                rover_score.append(70)

            else:
                rover_score.append(40)

        self.df["RoverSafetyScore"] = rover_score

        mission_score = []

        for _, row in self.df.iterrows():

            score = (
                row["IceScore"] * 0.45
                + row["LandingScore"] * 0.35
                + row["RoverSafetyScore"] * 0.20
            )

            mission_score.append(round(score, 2))

        self.df["MissionScore"] = mission_score

        self.df = self.df.sort_values(
            by="MissionScore",
            ascending=False
        )

        return self.df