import json
import streamlit as st
from elements import planck, ico, insert_css
from streamlit_extras.stylable_container import stylable_container


# ICONS
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">',unsafe_allow_html=True)

insert_css()

st.image(image='src/assets/main-title.png', width=900)

# COLUMNS
col1, col2 = st.columns([0.6, 0.4], gap='small')

with stylable_container(
    key='col1',
    css_styles="""
        {
            backgrond-color: white;
        }  
"""
):
    with col1:
        st.markdown("""
            <p id="first-txt">
                Hey, my name is Pedro Saito and I'm a Computer Science 
        Undergrad at the Federal University of Rio de Janeiro. Even though my 
        main interests are Datascience with <span>Python</span> and Back-End,
        I've got more experience working with Front-End and also Data.
            </p>
        """, unsafe_allow_html=True)

with col2:
    st.image(image='src/assets/playdough-nerd.png', use_column_width=True)
    st.markdown("""
        <p style="text-align:center;">
            This is what I look like.
        </p>
    """, unsafe_allow_html=True)

st.image(image='src/assets/tools.png', width=900)

# ABILITIES COLUMNS
abilities = st.columns(3, gap='small')

with abilities[0]:
    planck('BACK-END')
    ico('C Lang')
    ico('C++ Lang')
    ico('Java')
    ico('Python')

    planck('PLATFORMS')
    ico('Jupyter')
    ico('Figma')

with abilities[1]:
    planck('FRONT-END')
    ico("HTML5")
    ico("CSS3")
    ico("Javascript")

    planck('OTHER')
    ico('Git')
    ico("JSON")
    ico("LaTeX")

with abilities[2]:
    planck('DATA')
    with st.expander('SQL Lang'):
        ico("SQLite")
        ico("SQL Server")
        ico("Azure SQL")
    with st.expander('Python Libs'):
        ico('Pandas')
        ico('Matplot')
        ico('Plotly')
        ico('Streamlit')
