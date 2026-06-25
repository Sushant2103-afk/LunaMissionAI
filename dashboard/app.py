import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_fusion import DataFusion
from src.ice_engine import IceEngine
from src.landing_engine import LandingEngine
from src.rover_engine import RoverEngine
from src.mission_engine import MissionEngine
from src.terrain_engine import TerrainEngine
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="LunaMission AI",
    layout="wide"
)

st.title("🌙 LunaMission AI")
st.subheader("AI Assisted Lunar Mission Decision Support System")
st.caption("Bharatiya Antariksh Hackathon • LunaMission AI v0.1")

from pathlib import Path

print(Path("data/sample/sample_lunar_data.csv").resolve())
print(Path("data/sample/sample_terrain_data.csv").resolve())
# -----------------------------
# Load Data
# -----------------------------

df = DataFusion.load()
print(df.columns.tolist())
print(df.head())

# -----------------------------
# Ice Confidence Engine
# -----------------------------

engine = IceEngine(df)
df = engine.calculate()

terrain = TerrainEngine(df)
df = terrain.calculate()

landing = LandingEngine(df)
df = landing.calculate()

rover = RoverEngine(df)

df = rover.calculate()
# -----------------------------
# Mission Decision Engine
# -----------------------------

mission = MissionEngine(df)

df = mission.calculate()
best = df.iloc[0]

st.success(
    f"""
# 🛰 Mission Status : READY

## Recommended Landing Site

### {best["Region"]}

Mission Score : {best["MissionScore"]}

Ice Confidence : {best["Confidence"]}

Landing Score : {best["LandingScore"]}

Traverse Risk : {best["TraverseRisk"]}

"""
)
st.markdown("## 📊 Mission Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🏆 Best Site",
    best["Region"]
)

c2.metric(
    "🧊 Ice Score",
    best["IceScore"]
)

c3.metric(
    "🚀 Landing",
    round(best["LandingScore"], 1)
)

c4.metric(
    "🎯 Mission",
    round(best["MissionScore"], 1)
)
st.markdown("---")

st.markdown("## 🛰 Final Mission Ranking")

st.dataframe(

    df[
        [
            "Region",
            "MissionScore",
            "IceScore",
            "LandingScore",
            "TraverseRisk"
        ]
    ],

    width="stretch"

)
# -----------------------------
# Sort Regions by Ice Score
# -----------------------------

ranking = df.sort_values(
    by="IceScore",
    ascending=False
)


# -----------------------------
# Metrics
# -----------------------------

st.markdown("---")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Regions",
    len(df)
)

c2.metric(
    "Highest CPR",
    df["CPR"].max()
)

c3.metric(
    "Lowest DOP",
    df["DOP"].min()
)

# -----------------------------
# Ice Confidence Ranking
# -----------------------------

st.markdown("---")
st.markdown("## 🧊 Ice Confidence Ranking")

st.dataframe(
    ranking,
    width="stretch"
)

# -----------------------------
# Bar Chart
# -----------------------------

st.markdown("---")
st.markdown("## 📊 Ice Confidence Visualization")

fig = px.bar(
    ranking,
    x="Region",
    y="IceScore",
    color="Confidence",
    text="IceScore",
    title="Ice Confidence by Region"
)

fig.update_layout(
    xaxis_title="Region",
    yaxis_title="Ice Score"
)

st.plotly_chart(
    fig,
    width="stretch"
)


st.markdown("---")

st.markdown("## 🚀 Landing Site Ranking")

landing_rank = df.sort_values(
    by="LandingScore",
    ascending=False
)

st.dataframe(
    landing_rank[
        [
            "Region",
            "IceScore",
            "LandingScore",
            "Slope"
        ]
    ],
    width="stretch"
)

landing_fig = px.scatter(

    landing_rank,

    x="Slope",

    y="LandingScore",

    size="IceScore",

    color="LandingScore",

    hover_name="Region",

    title="Landing Site Analysis"

)

st.plotly_chart(

    landing_fig,

    width="stretch"

)
st.markdown("---")
st.markdown("## 🤖 Rover Traverse Planning")

rover_rank = df.sort_values(
    by="LandingScore",
    ascending=False
)

st.dataframe(
    rover_rank[
        [
            "Region",
            "TraverseDistance",
            "EnergyCost",
            "TraverseRisk"
        ]
    ],
    width="stretch"
)

rover_fig = px.scatter(

    rover_rank,

    x="TraverseDistance",

    y="EnergyCost",

    color="TraverseRisk",

    size="LandingScore",

    hover_name="Region",

    title="Rover Traverse Analysis"

)

st.plotly_chart(

    rover_fig,

    width="stretch"

)
# -----------------------------
# Best Candidate
# -----------------------------

st.markdown("---")
st.markdown("## ⭐ Best Candidate Region")

best = ranking.iloc[0]

col1, col2 = st.columns(2)

col1.metric(
    "Region",
    best["Region"]
)

col2.metric(
    "Ice Score",
    best["IceScore"]
)

st.success(
    f"""
### Recommended Target

**Confidence:** {best["Confidence"]}

**CPR:** {best["CPR"]}

**DOP:** {best["DOP"]}

**Slope:** {best["Slope"]}°
"""
)

# -----------------------------
# Display Dataset
# -----------------------------

st.markdown("## 🛰️ Candidate Lunar Regions")

st.dataframe(
    df,
    width="stretch"
)
