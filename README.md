# Global Earthquake Tracker
An interactive Streamlit dashboard for exploring recent global seismic activity, built for my Data Collection and Analysis course. Pulls the last 30 days of earthquake data straight from the USGS Earthquakes API.
In short: a tool that shows where earthquakes have happened around the world in the last month, and lets you filter by how strong they were.

**[Live demo](https://earthquake-tracker-wt.streamlit.app/)**

## What it does

Split into two parts: a Jupyter notebook that grabs and cleans the data, a Streamlit app that reads the cleaned result and turns it into a dashboard.
The notebook pulls earthquake data (magnitude, location, time, coordinates) from the USGS API, fixes up the timestamps so they're actually readable, drops rows missing key values and adds a `risk_category` column based on magnitude:
Minor (under 3.0), Moderate (3.0–4.9), or Strong (5.0+). The cleaned data gets saved to a CSV, and the app loads that instead of calling the API directly. That way it opens instantly and the numbers don't shift around while someone's using it.

The dashboard has three sidebar filters (minimum magnitude, maximum depth, risk category), two summary metrics up top (total earthquakes and the highest magnitude currently showing), and a map where each earthquake shows up as a dot sized by how strong it was.

## What I found

Even with no filters on the earthquakes aren't spread out evenly at all, most of them cluster around the west coast of the US plus Japan and Indonesia. Most of what shows up is Minor earthquakes, only a small chunk end up Strong. Filtering down to just "Strong" cuts the map from thousands of dots to way fewer, but they're still clustered in the same spots just easier to actually see without all the minor stuff cluttering it up.

Since the app pulls live data every time it loads the exact numbers will look different depending on when you check it, but the pattern of where the earthquakes happen stays the same.

## Built with

Python, Streamlit, pandas, pydeck, requests
