import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações:')
        reviews_df = pd.json_normalize(reviews)
        reviews_df = reviews_df.drop(columns=['id'])

        AgGrid(
            data=pd.DataFrame(reviews_df),
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title('Cadastrar Nova Avaliação:')

    movie_service = MovieService()
    movies = movie_service.get_movie()
    movies_name = {movie['title']: movie['id'] for movie in movies}
    selected_movie_name = st.selectbox('Filme', list(movies_name.keys()))
    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1
    )
    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_reviews(
            movie=movies_name[selected_movie_name],
            stars=stars,
            comment=comment
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a avaliação. Verifique os campos')
