import streamlit as st
from elements import planck, ico
from streamlit_extras.grid import grid

with open("main-page.css") as main, open("interpage.css") as interpage:
    st.markdown(f'<style>{main.read()}</style>', unsafe_allow_html=True)
    st.markdown(f'<style>{interpage.read()}</style>', unsafe_allow_html=True)

# ICONS
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">',unsafe_allow_html=True)

st.image(image='src/assets/main-title.png', width=900)

# COLUMNS
col1, col2 = st.columns([0.6, 0.4], gap='small')

with col1:
    st.write("""Hey, my name is Pedro Saito and I'm a Computer Science 
    Undergrad at the Federal University of Rio de Janeiro.appetere putent 
    imperdiet luctus menandri suscipiantur habeo constituto auctor 
    sententiae molestiae principes suavitate conclusionemque postea docendi
     instructior partiendo efficitur has
    """)

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
    ico("C Lang", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg")
    ico("C++ Lang", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg")
    ico("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg")
    ico("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg")

    planck('OTHER')
    ico("JSON", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg")
    ico("LaTeX", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tex/tex-original.svg")


with abilities[1]:
    planck('FRONT-END')
    ico("HTML5", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg")
    ico("CSS3", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg")
    ico("Javascript", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg")

with abilities[2]:
    planck('DATA')
    with st.expander('SQL Lang'):
        ico("SQLite", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg")
        ico("SQL Server", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/microsoftsqlserver/microsoftsqlserver-original.svg")
        ico("Azure SQL", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg")
    with st.expander('Python Libs'):
        ico('Pandas', "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg")
        ico('Matplot', "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg")
        ico('Plotly', "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original.svg")
