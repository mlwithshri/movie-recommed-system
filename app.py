import pandas as pd
import streamlit as st
import pickle
import base64



def recommend(movie):
    # Get the index of the movie in the dataframe
    movie_index=movies[movies['title']==movie].index[0]

    # Get similarity scores for that movie with all others
    distance=similarity[movie_index]

    # Sort all movies based on similarity score (excluding the same movie)
    movies_list=sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]

    recommendmovies = []
    for i in movies_list:
        movie_id=i[0]
        # fetched poster through of recommed movies
        recommendmovies.append(movies.iloc[i[0]].title)
    return recommendmovies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('enter movie name', movies['title'].values)


if st.button("recommed"):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)

