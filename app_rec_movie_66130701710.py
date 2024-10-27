import pickle
import streamlit as st
from myfunction_66130701710 import get_movie_recommendations
from surprise import SVD
# Load data back from the file
with open('66130701710_recommendation_usersim.pkl', 'rb') as file:
    user_similarity_df, user_movie_ratings = pickle.load(file)
    
st.title("Movie Recommendation System")

# Input: Collect user_id from the user
user_id = st.text_input("Enter User ID:", "")

if user_id:
    # Get recommendations (top 10)
    recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, 10)
    
    # Display recommendations
    st.write(f"Top 10 movie recommendations for User {user_id}:")
    for movie_title in recommendations:
        st.write("• " + movie_title)
