import pandas as pd

movies_data = {
    'Movie Title': ['The Dark Knight', 'Interstellar', 'The Matrix', 'Titanic', 
                    'Avengers: Endgame', 'Inception', 'The Notebook', 'Gladiator'],
    'Genre': ['Action, Drama', 'Sci-Fi, Drama', 'Action, Sci-Fi', 'Drama, Romance',
              'Action, Sci-Fi', 'Action, Sci-Fi', 'Romance, Drama', 'Action, Drama']
}

movies_df = pd.DataFrame(movies_data)

def recommend_movies(preferred_genres):
    user_genres_set = set(preferred_genres.split(', '))
    
    recommended_movies = []
    for _, row in movies_df.iterrows():
        movie_title = row['Movie Title']
        movie_genres = set(row['Genre'].split(', '))
        
        if not user_genres_set.isdisjoint(movie_genres):
            recommended_movies.append(movie_title)
    
    if recommended_movies:
        return recommended_movies
    else:
        return "No movies found matching your preferences."

def get_user_input():
    print("Please enter the genres you like (comma separated). Example: Action, Drama, Sci-Fi")
    preferred_genres = input("Enter your preferred genres: ").strip()
    
    recommendations = recommend_movies(preferred_genres)
    
    print("\nRecommended movies based on your preferences:")
    if isinstance(recommendations, list):
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print(recommendations)

get_user_input()