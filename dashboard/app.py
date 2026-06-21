import streamlit as st
import pandas as pd
from src.ice_engine import IceEngine
st.caption(
    "Bharatiya Antariksh Hackathon • LunaMission AI v0.1"
)
st.set_page_config(
    page_title="LunaMission AI",
    layout="wide"
)

st.title("🌙 LunaMission AI")

st.subheader(
    "AI Assisted Lunar Mission Decision Support System"
)

df = pd.read_csv("data/sample/sample_lunar_data.csv")
engine = IceEngine(df)

df = engine.calculate()

st.markdown("🛰️ Candidate Lunar Regions")

st.dataframe(
    df,
    use_container_width=True
)

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

st.markdown("## 🧊 Ice Confidence Ranking")

ranking = df.sort_values(
    by="IceScore",
    ascending=False
)

st.dataframe(
    ranking,
    use_container_width=True
)