import streamlit as st
import json

# JSON
json_path = 'icons.json'
with open(json_path, 'r') as f:
    icons_dict = json.load(f)

# CSS
css_paths = [
    'src/styles/main-page.css',     # Main
    'src/styles/interpage.css',     # Interpage elements
    'src/styles/sidebar.css',       # Sidebar
    'src/styles/portfolio.css'      # Portfolio
]

css_content = [open(file).read() for file in css_paths]
combined_css = '<style>' + '\n'.join(css_content) + '</style>'


# FUNCTIONS
def insert_css() -> None:
    st.markdown(combined_css, unsafe_allow_html=True)


def planck(text: str) -> None:
    st.markdown(f"""
    <div class="planck">
        <span>{text}</span>
    </div>
    """, unsafe_allow_html=True)


def circus_frame(text: str) -> None:
    st.markdown(f"""
    <div class="circus">
        <span>{text}</span>
    </div>
    """, unsafe_allow_html=True)


def project(title: str, img: str, desc: str) -> None:
    circus_frame(f'{title}')
    st.markdown(f"""
    <div class="st-emotion-cache-ocqkz7 portfolio">
        <img src="{img}" alt="{title}" Image />
        <div class="st-emotion-cache-fplge5">
            <p>{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    pass


def ico(name: str) -> None:
    st.markdown(f"""
    <div class="icon-container">
        <img class="icons" src="{icons_dict[f'{name}']}" alt="{name} Icon"/>
        <p class="icon-text">{name}</p>
    </div>
    """, unsafe_allow_html=True)
