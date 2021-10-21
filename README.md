# Movie-Recommender
This Python script uses 2 different APIs (TasteDive and OMDB) to recommend related, highly rated movies to the user based on input of a title. The title can be any form of media - songs, artists, movies, etc. - the app with return a list of movies with the highest rated coming first.

The TasteDive API first takes the media name and returns a list of the 5 closest related movies each based on the titles given. The OMDB API then takes those related movies, looks at their Rotten Tomatoes rating, then returns a sorted list of related movies ranked by the highest rated first.
