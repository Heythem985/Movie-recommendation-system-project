import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.model import recommend
data = pd.read_csv("data/movies.csv")  # Update the path if needed


st.title("🎬 Movie Recommendation System")

movie_title = st.text_input("Enter a movie title:")

if st.button("Recommend"):
    if movie_title not in data['title'].values:
        f"Movie '{movie_title}' not found in dataset."
        st.stop()
    recommendations = recommend(movie_title)
    recommendations.drop_duplicates()
    st.write(recommendations)