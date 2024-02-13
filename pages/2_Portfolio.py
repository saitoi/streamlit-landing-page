import streamlit as st
from elements import insert_css, frame

insert_css()

st.image(image='src/assets/port.png', width=800)

frame('MEGA-SENA DASHBOARD')

st.markdown("""
    <div class="st-emotion-cache-ocqkz7 portfolio">
        <div class="st-emotion-cache-fplge5">
            <p>So this is a test..</p>
        </div>
    </div>
""", unsafe_allow_html=True)
