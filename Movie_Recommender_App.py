# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 21:18:45 2025

@author: Ekhlaque
"""

import streamlit as st
import pickle
import pandas as pd
import joblib


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies 


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = joblib.load('similarity.joblib')

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
 'Which Movie you like To Watch the Same',
    movies['title'].values)
if st.button('Recommend'):
    names = recommend(selected_movie_name)


    col1, = st.columns(1)

    with col1:
        st.text('- '+ names[0])

    with col1:
        st.text('- '+ names[1])

    with col1:
        st.text('- '+ names[2])

    with col1:
        st.text('- '+ names[3])

    with col1:
        st.text('- '+ names[4])
             
        
        
