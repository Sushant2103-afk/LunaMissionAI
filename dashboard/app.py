import streamlit as st
import pandas as pd
import plotly.express as px

from src.ice_engine import IceEngine
from src.landing_engine import LandingEngine
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

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("data/sample/sample_lunar_data.csv")

# -----------------------------
# Ice Confidence Engine
# -----------------------------

engine = IceEngine(df)
df = engine.calculate()

landing = LandingEngine(df)
df = landing.calculate()
# -----------------------------
# Sort Regions by Ice Score
# -----------------------------

ranking = df.sort_values(
    by="IceScore",
    ascending=False
)

# -----------------------------
# Display Dataset
# -----------------------------

st.markdown("## 🛰️ Candidate Lunar Regions")

st.dataframe(
    df,
    use_container_width=True
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
    use_container_width=True
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
    use_container_width=True
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
    use_container_width=True
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

    use_container_width=True

)