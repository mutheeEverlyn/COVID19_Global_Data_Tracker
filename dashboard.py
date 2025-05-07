
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

st.title("🦠 COVID-19 Dashboard")
st.markdown("Visualize COVID-19 cases, deaths, hospitalizations, and ICU data by country and date range.")

@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv", parse_dates=["date"])
    df = df[df["location"].notna()]
    return df

data = load_data()

st.sidebar.header("🔧 Filter Options")
country = st.sidebar.selectbox("Select Country", sorted(data["location"].unique()), index=0)

min_date = data["date"].min().date()
max_date = data["date"].max().date()

start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

if start_date > end_date:
    st.error("🚫 Start date must be before end date.")
    st.stop()

filtered = data[
    (data["location"] == country) &
    (data["date"] >= pd.to_datetime(start_date)) &
    (data["date"] <= pd.to_datetime(end_date))
].copy()

for col in ["hosp_patients", "icu_patients"]:
    if col not in filtered.columns:
        filtered[col] = None

st.subheader(f"📈 COVID-19 Trends in {country}")
st.write(f"From **{start_date}** to **{end_date}**")

chart_data = filtered.set_index("date")[["new_cases", "new_deaths", "hosp_patients", "icu_patients"]]
chart_data = chart_data.fillna(0)

st.line_chart(chart_data, use_container_width=True)

with st.expander("📄 Show Raw Data"):
    st.dataframe(filtered.reset_index(drop=True))

st.markdown("---")
st.caption("Data source: Our World in Data (owid-covid-data.csv)")
