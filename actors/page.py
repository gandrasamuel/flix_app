import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actor()

    if actors:
        st.write('Lista de Atores/Atrizes:')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=pd.DataFrame(actors_df),
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Nenhum Actor/Atriz encontrado')

    st.title('Cadastrar novo(a) Ator/Atriz')

    name = st.text_input('Nome do(a) Ator/Atriz')
    birthday = st.date_input(
        label='Ano de nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')
