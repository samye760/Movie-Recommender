# Movie-Recommender
This Python script uses 2 different APIs (TasteDive and OMDB) to recommend related, highly rated movies to the user based on input of a title. The title can be any form of media - songs, artists, movies, etc. - the app with return a list of movies with the highest rated coming first.

The TasteDive API first takes the media name and returns a list of the 5 closest related movies each based on the titles given. The OMDB API then takes those related movies, looks at their Rotten Tomatoes rating, then returns a sorted list of related movies ranked by the highest rated first.

Both of these APIs do need keys which can be signed up for for free on their respective websites (https://tastedive.com/read/api and https://www.omdbapi.com/). These API keys will have to be generated and added to the <param> varables in the code in order to work.
