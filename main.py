"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from pages import home, data, predict, visualise, about

# Configure the app
st.set_page_config(
    page_title = 'Kidney Disease Prediction',
    page_icon = 'drop_of_blood',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
pages = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise,
    "About me": about
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    pages[page].app(df, X, y)
elif (page == "Data Info"):
    pages[page].app(df)
else:
    pages[page].app()
