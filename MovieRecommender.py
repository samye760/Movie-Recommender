import requests

def get_movies_from_tastedive(name):
    endpoint = "https://tastedive.com/api/similar"
    param = {"q": name, "type": "movies", "limit": "5"}
    return requests.get(endpoint, params = param).json()

def extract_movie_titles(related):
    movies = []
    for movie in related["Similar"]["Results"]:
        movies.append(movie["Name"])
        
    return movies

def get_related_titles(titles):
    movies = []
    for title in titles:
        rel_movies = extract_movie_titles(get_movies_from_tastedive(title))
        for movie in rel_movies:
            if movie not in movies:
                movies.append(movie)
        
    return movies

def get_movie_data(title):
    endpoint = "http://www.omdbapi.com/"
    param = {"t": title, "r": "json"}
    return requests.get(endpoint, params = param).json()

def get_movie_rating(movie):
    try:
        ratings = movie["Ratings"][1]
        if ratings["Source"] == "Rotten Tomatoes":
            return int(ratings["Value"].replace("%", ""))
        else:
            return 0
    except:
        return 0
    
def get_sorted_recommendations(titles):
    ranking = {}
    related = get_related_titles(titles)
    for movie in related:
        score = get_movie_rating(get_movie_data(movie))
        ranking[movie] = score
        
    return sorted(ranking, key = lambda k: (ranking[k], k), reverse = True)