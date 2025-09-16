import streamlit as st
import pandas as pd 
import os 
   
st.title("Movie overview")
# Get the base directory (repo root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level if script is inside src/, else stay in root
DATA_PATH = os.path.join(BASE_DIR, "data")

# Read CSVs from the data folder
movies = pd.read_csv(os.path.join(DATA_PATH, "movies.csv"))
ratings = pd.read_csv(os.path.join(DATA_PATH, "ratings.csv"))

merged = pd.merge(movies, ratings, on='movieId')
avg_ratings = merged.groupby(['movieId', 'title', 'genres'])['rating'].mean().reset_index()
selected = avg_ratings[['title', 'genres', 'rating']]
st.write(selected.head(20))