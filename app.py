import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviwes
from login.page import show_login
from Home.page import show_home


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Genêros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
        )

        if menu_option == 'Início':
            show_home()

        if menu_option == 'Genêros':
            show_genres()

        if menu_option == 'Atores/Atrizes':
            show_actors()

        if menu_option == 'Filmes':
            show_movies()

        if menu_option == 'Avaliações':
            show_reviwes()


if __name__ == '__main__':
    main()
