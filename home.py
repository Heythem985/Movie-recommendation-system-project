import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from model import recommend

st.title("🎬 Movie Recommendation System")

movie_title = st.text_input("Enter a movie title:")

if st.button("Recommend"):
    recommendations = recommend(movie_title)
    recommendations.drop_duplicates()
    st.write(recommendations)