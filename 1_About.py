import streamlit as st
from elements import planck, ico, insert_css

st.set_page_config(
    page_title="Saito's Lair",
    page_icon='https://iili.io/JEJS2hQ.png',
    initial_sidebar_state='collapsed',
    layout='centered'
)

# CSS FROM 'src/styles/.'
insert_css()

# SAITOS LAIR TITLE
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

# CONTINUE WRITING
st.markdown("""
    <div class="st-emotion-cache-ocqkz7">
        <div class="st-emotion-cache-fplge5">
            <p>So this is a test..</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# TOOLS TITLE
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
    ico('Intellij')

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
        ico('NumPy')
        ico('Matplot')
        ico('Plotly')
        ico('Streamlit')
