from math import sqrt, pi
from plotly import graph_objects as go
from shapely import LineString, intersection
import streamlit as st
from streamlit_option_menu import option_menu
from eng_module import seismic_analysis as sa

import pandas as pd

st.set_page_config(
    page_title='Bridge Analysis',
    layout='wide',
    initial_sidebar_state='expanded',
)

with st.sidebar:
    st.title('Bridge Analysis Tools')
    main_menu_selection = option_menu(None, ["Home", 'Seismic Analysis'], 
    icons=['house', 'activity'], menu_icon="cast", default_index=1,
        styles={'nav-link-selected': {'background-color': 'green'}}
    )
    
if main_menu_selection == 'Home':
    st.header('Tools for Bridge Analysis')

elif main_menu_selection == 'Seismic Analysis':
    sa_geometry_tab, sa_loads_tab, sa_results_tab = st.tabs(['Geometry', 'Loads', 'Results'])

    with sa_geometry_tab:
        st.subheader('Spans Defenition')
        spans = pd.DataFrame(
                [
                    {'Span Name': 'Span 1', 'Span Length [m]': 30.0},
                ]   
            )
        bridge_spans = st.data_editor(spans, num_rows='dynamic')

        if len(bridge_spans) > 1:
            st.subheader('Pier Geometry')
            pier_columns = ['Pier Name', 'Pier Height [m]', 'Pier Inertia [m4]']
            pier_index = [idx for idx in range(len(bridge_spans)-1)]
            pier_names = []
            for idx in range(len(bridge_spans)-1):
                pier_names.append([f'Pier {idx+1}', 0., 0.])
            piers = pd.DataFrame(pier_names, index=pier_index, columns=pier_columns)
            bridge_piers = st.data_editor(piers, disabled= ('Pier Name',), hide_index= True)
