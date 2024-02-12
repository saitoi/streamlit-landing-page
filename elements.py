import streamlit as st

with open("main-page.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


def planck(text: str) -> None:
    st.markdown(f"""
    <div class="planck">
        <span>{text}</span>
    </div>
    """, unsafe_allow_html=True)


def ico(name: str, url: str) -> None:
    st.markdown(f"""
    <div class="icon-container">
        <img class="icons" src="{url}" alt="{name} Icon"/>
        <span class="icon-text">{name}</span>
    </div>
    """, unsafe_allow_html=True)
