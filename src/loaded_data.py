import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "movies.csv")

data = pd.read_csv(DATA_PATH) 


# Handle missing values
data['genres'].fillna('', inplace=True)

# Drop duplicates
data = data.drop_duplicates()

# Convert genres to vector format
vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = vectorizer.fit_transform(data['genres'])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)


ratings = pd.read_csv(r"C:\Users\d\Documents\python_projects\movie_recommendation_system\data\ratings.csv") 
