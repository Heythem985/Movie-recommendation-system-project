import streamlit as st
import pandas as pd 
from Over


movies = pd.read_csv(r"C:\Users\d\Documents\python_projects\movie_recommendation_system\data\movies.csv")
ratings = pd.read_csv(r"C:\Users\d\Documents\python_projects\movie_recommendation_system\data\ratings.csv") 

merged = pd.merge(movies, ratings, on='movieId')
avg_ratings = merged.groupby(['movieId', 'title', 'genres'])['rating'].mean().reset_index()
selected = avg_ratings[['title', 'genres', 'rating']]
st.write(selected.sort_values('rating', ascending=False).head(20))

st.markdown("### Filters")
min_rating =st.slider("Select minimum rating :", 0.0, 5.0, 0.0, 0.1)
if st.button("Filter"):
    filtered_movies = selected[selected['rating'] >= min_rating].sort_values('rating', ascending=False)
    st.write(filtered_movies)





 
