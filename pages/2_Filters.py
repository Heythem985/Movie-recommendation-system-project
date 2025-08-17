import streamlit as st
import pandas as pd 
import importlib
Overview = importlib.import_module("pages.3_Overview")
selected = overview.selected
from pages.Overview import selected

st.title("Movie Filters")

st.markdown("### Filter movies based on rating : ")
min_rating =st.slider("Select minimum rating :", 0.0, 5.0, 0.0, 0.1)
max_rating = st.slider("Select maximum rating :", 0.0, 5.0, 5.0, 0.1)
if st.button("Filter"):
    filtered_movies = selected[
        (selected['rating'] >= min_rating)  & 
        (selected['rating'] <= max_rating )].sort_values('rating', ascending=False)
    st.write(filtered_movies)


st.markdown("### Filter movies based on genre : ")
genres = selected['genres'].str.split('|').explode().unique()
selected_genre = st.selectbox("Select a genre:", genres)
st.write(f"Movies in the genre: {selected_genre}")
filtered_by_genre = selected[selected['genres'].str.contains(selected_genre, case=False)]
st.write(filtered_by_genre[['title', 'genres', 'rating']].sort_values('rating', ascending=False)) 






 
