import streamlit as st
import streamlit_elements as st_elements

with open("main-page.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.write('This is not right')

# TITLE IMAGE
st.image(image='assets/saitos-lair-shrek.png', width=750)

st_elements.divider_element()

# COLUMNS
col1, col2 = st.columns([0.6, 0.4], gap='small')

with col1:
    st.markdown("""
    <p>
        Hey, my name is Pedro Saito and I'm a Computer Science Undergrad
    at the Federal University of Rio de Janeiro.appetere putent imperdiet
     luctus menandri suscipiantur habeo constituto auctor sententiae molestiae
      principes suavitate conclusionemque postea docendi instructior  
      partiendo efficitur has
    </p>
    """, unsafe_allow_html=True)

with col2:
    # st.markdown("""
    # <style>
    # .circle-image {
    #     width: 250px;
    #     height: 250px;
    #     border-radius: 50%;
    #     overflow: hidden;
    #     box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    #     background: linear-gradient(to top, white, gray, black);
    #     background-clip: padding-box; /* Ensures the background (gradient) is only visible in the padding area */
    #     border: 5px solid transparent;
    #     transition: transform 0.5s ease;
    # }
    #
    # .circle-image img {
    #     width: 100%;
    #     height: 100%;
    #     object-fit: cover;
    # }
    #
    # .circle-image:hover {
    #     transform: rotate(180deg);
    #     cursor: pointer;
    # }
    # </style>
    #
    # <div class="circle-image">
    #     <img src="https://iili.io/J1M8Mog.png" alt="My Rectangular Image">
    # </div>
    # """, unsafe_allow_html=True)
    st.image(image='assets/playdough-nerd.png', use_column_width=True)
    st.caption("""
    <style>
        center {
            color: black;
        }
    </style>
    <center>This is what I look like</center>
    """, unsafe_allow_html=True)

st.subheader('Tools')
st.divider()
