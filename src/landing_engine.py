"""
Landing Site Optimizer
"""

class LandingEngine:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    def calculate(self):

        scores = []

        for _, row in self.df.iterrows():

            score = (
                row["IceScore"] * 0.7
                + (20 - row["Slope"]) * 1.5
            )

            scores.append(round(score, 2))

        self.df["LandingScore"] = scores

        return self.df