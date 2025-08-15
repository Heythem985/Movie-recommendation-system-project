import streamlit as st
import pandas as pd 


st.title("Movie overview")

movies = pd.read_csv(r"C:\Users\d\Documents\python_projects\movie_recommendation_system\data\movies.csv")
ratings = pd.read_csv(r"C:\Users\d\Documents\python_projects\movie_recommendation_system\data\ratings.csv") 

merged = pd.merge(movies, ratings, on='movieId')
avg_ratings = merged.groupby(['movieId', 'title', 'genres'])['rating'].mean().reset_index()


st.write(avg_ratings.head(10)) 
 
