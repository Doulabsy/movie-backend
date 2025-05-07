
from database import SessionLocal
import query_helpers as query_helpers

# Créer une session
db = SessionLocal()

# movie = query_helpers.get_movie(db, movie_id = 1)
# print(movie.title, movie.genres)

# # Tester la récupération de films
# movies = query_helpers.get_movies(db, limit=5, genre="Comedy")

# for movie in movies:
#     print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# tester la fonction rating
# ratings = query_helpers.get_ratings(db, limit=5, min_rating=4.0)
# for rating in ratings:
#     print(f"User ID: {rating.userId}, Movie ID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")

# tester la focntion tag

tag = query_helpers.get_tag(db, user_id = 2, movie_id= 60756, tag_text="funny")
print(tag)
print(f"User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")

tags = query_helpers.get_tags(db, limit=5)
print(tags)
for tag in tags:
    print(f"User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")

# tester la fonction link
links = query_helpers.get_links(db, limit=5)
for link in links:
    print(f"Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")

# tester la fonction get_rating_count
rating_count = query_helpers.get_rating_count(db)
print(f"Nombre d'évaluations pour le film : {rating_count}")

# Fermer la session
db.close()