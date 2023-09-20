import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import urllib.request

# Load movie data from a pickle file
movies = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)
movies.reset_index(inplace=True)
movies_list = movies['title'].values

# Load movie similarity data from a pickle file
sims = pickle.load(open('similarity.pkl', 'rb'))

# Set the title for the Streamlit web app
st.title('Movie Recommender System')

# Create a dropdown for selecting a movie
selected_movie = st.selectbox(
    'Select a movie you like:',
    movies_list)

# Function to fetch movie poster from The Movie Database API
def fetch_poster(movie_id):
    response = requests.get(url=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ac49bb24ce69e2b0d99466b4752af33b')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w200' + data['poster_path']

# Function to recommend movies based on similarity
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    recommended_movies = sorted(list(enumerate(sims[movie_idx])), reverse=True, key=lambda x: x[1])[1:6]
    posters = []
    for i in recommended_movies:
        idx = i[0]
        posters.append(fetch_poster(movies.iloc[idx]['movie_id']))
    return recommended_movies, posters

# Create a button to trigger movie recommendations
if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie)

    st.write('You selected:', selected_movie)

    # Display recommended movies with posters and titles
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(f"{posters[0]}")
        st.write(f"{movies.iloc[recommendations[0][0]]['title']}")
    with col2:
        st.image(f"{posters[1]}")
        st.write(f"{movies.iloc[recommendations[1][0]]['title']}")
    with col3:
        st.image(f"{posters[2]}")
        st.write(f"{movies.iloc[recommendations[2][0]]['title']}")
    with col4:
        st.image(f"{posters[3]}")
        st.write(f"{movies.iloc[recommendations[3][0]]['title']}")
    with col5:
        st.image(f"{posters[4]}")
        st.write(f"{movies.iloc[recommendations[4][0]]['title']}")
