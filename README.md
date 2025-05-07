# 🦠 COVID-19 Data Analysis

This project focuses on analyzing and visualizing global COVID-19 data using Python and Jupyter Notebook. It allows users to explore case trends, filter by country and date range, and draw insights from visual patterns.

---

## 🎯 Project Objectives

- Analyze global and country-specific COVID-19 case trends.
- Create visualizations to show the spread and impact over time.
- Enable user input to select specific countries and timeframes.
- Identify peaks, declines, and anomalies in the data.
- Allow filtering by country and date range (in the Streamlit dashboard).

---

## 🛠️ Tools and Libraries Used

- **Python 3.13.2 **
- **Jupyter Notebook**
- **Pandas** – for data manipulation
- **Matplotlib / Seaborn / Plotly** – for visualizations
- **IPyWidgets** – for interactive controls
- **NumPy** – for numerical processing
- `streamlit` (for dashboard)
- `owid-covid-data.csv` (data source)

---

## ▶️ How to Run the Project

1. Open the Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Launch the notebook file `COVID19_Global_Data_Tracker.ipynb`.

3. Install required libraries if not already available:
   ```
   pip install pandas matplotlib seaborn plotly ipywidgets
   ```

4. Run all cells in order to explore data and interact with visualizations.

5. Ensure dashboard.py and owid-covid-data.csv are in the same folder.

6. From the terminal,ensure you navigate to the folder where the project is and run: streamlit run dashboard.py 

7. Your browser will open an interactive dashboard allowing you to:

   - Select a country

   - Choose a custom date range

   - Visualize new cases, deaths, hospitalizations, and ICU trends


---

## 📊 Insights and Reflections

- COVID-19 waves varied significantly between countries and over time.
- Visualization made it easier to understand the timing and scale of outbreaks.
- User interactivity helped focus on specific regions and time periods.
- The project demonstrated the power of Python for real-world data analysis.

---
