import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommendation System')
movies_dict = pickle.load(open('movies_dic.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
    'please select any movie or type it',
    movies['title'].values
)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=124ce641403f1df8749e9dbaec0c5748&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)  # Call the function and store results

if 'recommendation' in locals():  # Check if recommendation variable is defined
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header(recommendation[0][0])
        st.image(recommendation[1][0])

    with col2:
        st.header(recommendation[0][1])
        st.image(recommendation[1][1])

    with col3:
        st.header(recommendation[0][2])
        st.image(recommendation[1][2])

    with col4:
        st.header(recommendation[0][3])
        st.image(recommendation[1][3])

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.header(recommendation[0][4])
        st.image(recommendation[1][4])

    with col6:
        st.header(recommendation[0][5])
        st.image(recommendation[1][5])

    with col7:
        st.header(recommendation[0][6])
        st.image(recommendation[1][6])

    with col8:
        st.header(recommendation[0][7])
        st.image(recommendation[1][7])
