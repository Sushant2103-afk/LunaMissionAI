import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LunaMission AI",
    layout="wide"
)

st.title("🌙 LunaMission AI")

st.subheader(
    "AI Assisted Lunar Mission Decision Support System"
)

df = pd.read_csv("data/sample/sample_lunar_data.csv")

st.markdown("## Lunar Regions")

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