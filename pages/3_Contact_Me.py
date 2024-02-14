import streamlit as st
from elements import *

st.set_page_config(
    page_title="Saito's Lair",
    page_icon='https://iili.io/JEJS2hQ.png',
    initial_sidebar_state='collapsed',
    layout='centered'
)

insert_css()

st.markdown(f"""
        <img src="https://iili.io/JEdg3FI.md.png" class="continue" alt="Image"/>
    """, unsafe_allow_html=True)
