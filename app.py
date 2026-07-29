import streamlit as st
import pickle
import requests

# -----------------------------
# TMDB API Key
# -----------------------------
API_KEY = "3eef31b027d15939f218d3535b53dda5"

# -----------------------------
# Load Model
# -----------------------------
movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))


# -----------------------------
# Fetch Poster
# -----------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path

    return "https://via.placeholder.com/500x750?text=No+Poster"


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].movie_id

        names.append(movies.iloc[i[0]].title)

        posters.append(fetch_poster(movie_id))

    return names, posters


# -----------------------------
# UI
# -----------------------------
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.write(names[i])