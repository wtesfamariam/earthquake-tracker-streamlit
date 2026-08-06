import streamlit as st
import pandas as pd
import pydeck as pdk

#Wide layout
st.set_page_config(page_title="Global Earthquake Tracker", layout="wide")

#Read the csv
quake_df = pd.read_csv("quake_df.csv")

#Title
st.title("🌍 Global Earthquake Tracker")


#App Description
st.markdown("""
This dashboard displays **recent global earthquakes** from the past 30 days,
sources from the **USGS Earthquakes API**. Use the interactive filters in the
sidebar to explore seismic activity by magnitude, depth, and risk category.
            
**How to use the filters in the sidebar:**
- **Minimum Magnitude** Slide to set the smallest magnitude to display
- **Maximum Depth (km)** Slide to set the deepest earthquakes to include
- **Risk Category** Select which categories (Minor, Moderate, Strong) to include
            
The metrics, map, and data table will automatically update as you adjust the filters.
""")

st.sidebar.title("Navigation & Controls")

#Magnitute slider 
min_magnitude = st.sidebar.slider(
    "Minimum Magnitude", 
    min_value=float(quake_df['mag'].min()),
    max_value=float(quake_df['mag'].max()),
    value=float(quake_df['mag'].min())
)

#Depth slider maximum depth
max_depth = st.sidebar.slider(
    "Maximum depth (km)",
    min_value=float(quake_df['depth'].min()),
    max_value=float(quake_df['depth'].max()),
    value=float(quake_df['depth'].max())
)

#Risk category multiselect
risk_filter = st.sidebar.multiselect(
    "Select Risk Category",
    options=quake_df['risk_category'].unique(),
    default=list(quake_df['risk_category'].unique())
)

#Filters
filtered_df = quake_df[(quake_df['mag'] >= min_magnitude) & (quake_df['depth'] <= max_depth) & (quake_df['risk_category'].isin(risk_filter))]

#Display metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Earthquakes", len(filtered_df))
with col2:
    st.metric("Maximum Magnitude", f"{filtered_df['mag'].max():.2f}")

#Show how many earthquakes match
st.write(f"Showing {len(filtered_df)} earthquakes")

#Simple map
st.subheader("Earthquake Locations")
st.map(filtered_df, latitude='latitude', longitude='longitude')




