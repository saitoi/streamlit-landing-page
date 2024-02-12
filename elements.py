import streamlit as st

css_paths = [
    'src/styles/main-page.css',
    'src/styles/interpage.css',
    'src/styles/sidebar.css'
]

css_content = [open(file).read() for file in css_paths]
combined_css = '<style>' + '\n'.join(css_content) + '</style>'

with open("src/styles/main-page.css") as css:
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


def insert_css() -> None:
    st.markdown(combined_css, unsafe_allow_html=True)
