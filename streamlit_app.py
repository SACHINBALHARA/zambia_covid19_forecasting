import streamlit as st 
import pandas as pd

from pages.eda_page import main as eda_page
from pages.home_page import main as home_page
from pages.model_page import main as model_page
from pages.overview_page import main as overview_page
from pages.team_page import main as team_page

st.balloons()
st.markdown("# COVID-19 Case Prediction App")

home, overview, eda, model, team = st.tabs(['Home', 'Overview', 'EDA', 'Model', 'Team'])

home_page(home)
overview_page(overview)
eda_page(eda)
model_page(model)
team_page(team)


