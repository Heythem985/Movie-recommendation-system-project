from  loaded_data import data, similarity

def recommend(movie_title):
    # Check if movie exists
    if movie_title not in data['title'].values:
        return f"Movie '{movie_title}' not found in dataset."

    # Find index
    idx = data[data['title'] == movie_title].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(similarity[idx]))

    # Sort by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 similar movies
    top_indices = [i[0] for i in sim_scores[1:11]]

    return data.iloc[top_indices][['title', 'genres']]

    

