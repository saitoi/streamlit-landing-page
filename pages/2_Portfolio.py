import streamlit as st
from elements import insert_css, project

st.set_page_config(
    page_title="Saito's Lair",
    page_icon='https://iili.io/JEJS2hQ.png',
    initial_sidebar_state='collapsed',
    layout='centered'
)

insert_css()

st.image(image='src/assets/port.png', width=800)

project(
    title='MEGA-SENA DASHBOARD',
    img='https://github.com/saitoi/mega-sena-dashboard/raw/main/assets/dashboard-mega-sena-screenshot.png',
    desc="""
        Este projeto é um dashboard para visualização de resultados da Mega-Sena, a loteria mais popular do Brasil. O dashboard permite aos usuários visualizar os últimos resultados, analisar frequências de números, entre outros insights estatísticos.
    """
)

project(
    title='SPOTIFY HOME PAGE',
    img='https://github.com/saitoi/spotify-homepage/raw/main/src/assets/screenshots/spotify-homepage-snapshot.png',
    desc="""
        O Spotify Alura é uma aplicação web que emula algumas funcionalidades do popular serviço de streaming de música, Spotify. É projetado como uma interface amigável onde os usuários podem navegar por diversas funcionalidades como início, busca, biblioteca e mais.
    """
)

project(
    title='Compilador GCC',
    img='https://github.com/novae1/estatisticaplusplus/raw/main/assets/screenshot.png',
    desc="""
        O projeto de extensão visa criar materiais educacionais sobre as linguagens de programação C e Fortran. Inicialmente, os materiais foram feitos em LaTeX, destacando os conceitos básicos de C e explorando o compilador GCC. Mais tarde, optamos por migrar para uma plataforma online usando HTML5 e CSS para oferecer conteúdo mais acessível e interativo aos usuários interessados. Essa transição permitirá uma melhor experiência de aprendizado para os estudantes e entusiastas das linguagens.
    """
)

# frame('MEGA-SENA DASHBOARD')
#
# st.markdown("""
#     <div class="st-emotion-cache-ocqkz7 portfolio">
#         <div class="st-emotion-cache-fplge5">
#             <p>So this is a test..</p>
#         </div>
#     </div>
# """, unsafe_allow_html=True)
