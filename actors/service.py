import streamlit as st
from .repository import ActorRepository


class ActorService():

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actor(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actor()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
