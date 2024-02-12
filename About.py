import streamlit as st
from elements import planck, ico, insert_css
from streamlit_extras.stylable_container import stylable_container

# ICONS
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">',unsafe_allow_html=True)

# css_paths = [
#     'src/styles/main-page.css',
#     'src/styles/interpage.css',
#     'src/styles/sidebar.css'
# ]
#
# css_content = [open(file).read() for file in css_paths]
#
# combined_css = '<style>' + '\n'.join(css_content) + '</style>'
#
# st.markdown(combined_css, unsafe_allow_html=True)

insert_css()

st.image(image='src/assets/main-title.png', width=900)

# COLUMNS
col1, col2 = st.columns([0.6, 0.4], gap='small')

with col1:
    st.markdown("""
        <p>
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

with stylable_container(
    key='board',
    css_styles="""
        #board {
            backgroud-color: black;
        }
    """
):
    with abilities[0]:
        planck('BACK-END')
        ico("C Lang", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg")
        ico("C++ Lang", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg")
        ico("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg")
        ico("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg")

        planck('PLATFORMS')
        ico('Jupyter', 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg')
        ico('Figma',  "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg")

    with abilities[1]:
        planck('FRONT-END')
        ico("HTML5", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg")
        ico("CSS3", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg")
        ico("Javascript", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg")

        planck('OTHER')
        ico('Git', 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg')
        ico("JSON", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg")
        ico("LaTeX", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tex/tex-original.svg")

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
            ico('Streamlit', 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg')
