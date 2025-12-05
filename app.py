import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
df = pd.DataFrame(movie_dict)

SIM_FILE = "similarity.pkl"
FILE_ID = "15TvN-zapEvKcdJlalvkCv-7JX4sjRcWb"
GDRIVE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

if not os.path.exists(SIM_FILE):
    gdown.download(GDRIVE_URL, SIM_FILE, quiet=False)

similarity = pickle.load(open(SIM_FILE, "rb"))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3907a8114aab2034916079c868b5af45&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].id
        recommended_movies.append(df.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

st.title("CineAI")

selected_movie_name = st.selectbox(
    'Choose a Movie & Let the Recommendations Begin',
     df['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])        
        st.markdown(
                f"<p style='text-align:center; font-size:16px; font-weight:600;'>{names[0]}</p>",
                unsafe_allow_html=True
            )

    with col2:
        st.image(posters[1])
        st.markdown(
                f"<p style='text-align:center; font-size:16px; font-weight:600;'>{names[1]}</p>",
                unsafe_allow_html=True
            )
        

    with col3:
        st.image(posters[2])
        st.markdown(
                f"<p style='text-align:center; font-size:16px; font-weight:600;'>{names[2]}</p>",
                unsafe_allow_html=True
            )
        

    with col4:
        st.image(posters[3])
        st.markdown(
                f"<p style='text-align:center; font-size:16px; font-weight:600;'>{names[3]}</p>",
                unsafe_allow_html=True
            )
        

    with col5:
        st.image(posters[4])
        st.markdown(
                f"<p style='text-align:center; font-size:16px; font-weight:600;'>{names[4]}</p>",
                unsafe_allow_html=True
            )
        


       