import streamlit as st

with open("main-page.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


def divider_element() -> None:
    st.markdown("""
    <div class='stylized-divider-element'>
    </div>
    """, unsafe_allow_html=True)
