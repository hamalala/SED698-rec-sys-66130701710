import pickle
import streamlit as st
import pandas as pd

# Load the data
with open('66130701710_recommendation_movie_svd.pkl', 'rb') as file:
    svd_model, movie_ratings, movies = pickle.load(file)

# Streamlit app title
st.title("Movie Recommendation System")

# User input for User ID
user_id = st.number_input("Enter User ID:", min_value=1, value=1)

# Process recommendations for the specified User ID
rated_user_movies = movie_ratings[movie_ratings['userId'] == user_id]['movieId'].values
unrated_movies = movies[~movies['movieId'].isin(rated_user_movies)]['movieId']
pred_rating = [svd_model.predict(user_id, movie_id) for movie_id in unrated_movies]
sorted_predictions = sorted(pred_rating, key=lambda x: x.est, reverse=True)

# Display top 10 recommendations
top_recommendations = sorted_predictions[:10]

st.subheader(f"Top 10 Movie Recommendations for User {user_id}")
for recommendation in top_recommendations:
    movie_title = movies[movies['movieId'] == recommendation.iid]['title'].values[0]
    st.write(f"{movie_title} (Estimated Rating: {recommendation.est:.2f})")
