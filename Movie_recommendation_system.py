<<<<<<< HEAD
import streamlit as st
import numpy as np
import pandas as pd
import difflib

# Load the movie data and similarity scores
movies_data = pd.read_csv('movies.csv')
similarity = np.load('cosine similarity score.npy')

# Set title with bold and emoji
st.title('_Movie Recommendation System_ :movie_camera:')

# Input for movie name
movie_name = st.text_input('Enter the movie name:').lower()

# Button to trigger movie recommendation
if st.button('Recommend Movie'):
    # Check if a movie name is entered
    if movie_name:
        # Get the list of all movie titles
        list_of_all_titles = movies_data['title'].tolist()

        # Find close matches to the entered movie name
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

        # Check if a close match is found
        if find_close_match:
            close_match = find_close_match[0]

            # Get the index of the movie
            index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

            # Get the similarity scores
            similarity_score = list(enumerate(similarity[index_of_the_movie]))

            # Sort the movies based on similarity scores
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            # Display the recommended movies with enhanced styling
            st.subheader('**Top 10 Recommended Movies For You:**')
            for i in range(1, 11):
                movie_index = sorted_similar_movies[i][0]
                movie_name_of_the_index = movies_data[movies_data['index'] == movie_index]['title'].values[0]
                st.write(f"**{i}.** {movie_name_of_the_index}")
        else:
            st.write("No close match found for the entered movie name.")
    else:
        st.write("Please enter a movie name to get recommendations.")
=======
import streamlit as st
import numpy as np
import pandas as pd
import difflib

# Load the movie data and similarity scores
movies_data = pd.read_csv('movies.csv')
similarity = np.load('cosine similarity score.npy')

# Set title with bold and emoji
st.title('_Movie Recommendation System_ :movie_camera:')

# Input for movie name
movie_name = st.text_input('Enter the movie name:').lower()

# Button to trigger movie recommendation
if st.button('Recommend Movie'):
    # Check if a movie name is entered
    if movie_name:
        # Get the list of all movie titles
        list_of_all_titles = movies_data['title'].tolist()

        # Find close matches to the entered movie name
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

        # Check if a close match is found
        if find_close_match:
            close_match = find_close_match[0]

            # Get the index of the movie
            index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

            # Get the similarity scores
            similarity_score = list(enumerate(similarity[index_of_the_movie]))

            # Sort the movies based on similarity scores
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            # Display the recommended movies with enhanced styling
            st.subheader('**Top 10 Recommended Movies For You:**')
            for i in range(1, 11):
                movie_index = sorted_similar_movies[i][0]
                movie_name_of_the_index = movies_data[movies_data['index'] == movie_index]['title'].values[0]
                st.write(f"**{i}.** {movie_name_of_the_index}")
        else:
            st.write("No close match found for the entered movie name.")
    else:
        st.write("Please enter a movie name to get recommendations.")
>>>>>>> origin/main
