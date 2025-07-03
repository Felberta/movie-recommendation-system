import pandas as pd


movies = pd.read_csv("data/movies.csv")


print("🎬 Sample Movie Data:")
print(movies.head())

def recommend_by_genre(genre):

    filtered = movies[movies['genres'].str.contains(genre, case=False, na=False)]
    
    
    if filtered.empty:
        print(f"❌ No movies found for genre: {genre}")
    else:
        print(f"\n📽️ Top movies in the genre '{genre}':")
        print(filtered[['title', 'genres']].head(10))


def recommend_similar_movies(movie_title):

    movie_title = movie_title.strip().lower()


    match = movies[movies['title'].str.lower().str.contains(movie_title)]

    if match.empty:
        print(f"❌ No matching movie found for: {movie_title}")
        return

    
    selected_movie = match.iloc[0]
    selected_genres = selected_movie['genres'].split('|')

    print(f"\n🔍 You selected: {selected_movie['title']}")
    print(f"📂 Genres: {', '.join(selected_genres)}")

    
    similar_movies = movies[movies['genres'].apply(
        lambda g: any(genre in g.split('|') for genre in selected_genres)
    )]

    
    similar_movies = similar_movies[similar_movies['title'] != selected_movie['title']]

    print(f"\n🎯 Recommended movies similar to '{selected_movie['title']}':")
    print(similar_movies[['title', 'genres']].head(10))


print("\n📌 Choose an option:")
print("1. Recommend by genre")
print("2. Recommend similar movies based on a movie")

choice = input("Enter 1 or 2: ")

if choice == '1':
    user_input = input("Enter a genre (e.g. Comedy, Action, Romance): ")
    recommend_by_genre(user_input)
elif choice == '2':
    movie_input = input("Enter part of a movie title (e.g. Toy, Jumanji): ")
    recommend_similar_movies(movie_input)
else:
    print("❌ Invalid choice")
