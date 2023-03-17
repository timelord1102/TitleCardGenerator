import requests

APIKey = "c4410bc9f0f92da919f494775d41df89";

def getSearchResults(searchString):
    url = "https://api.themoviedb.org/3/search/tv?api_key="+ APIKey +"&query=" + searchString.replace(" ", "%20")
    response = requests.get(url)
    return response.json()

def getShowDetails(showID):
    url = "https://api.themoviedb.org/3/tv/" + str(showID) + "?api_key=" + APIKey
    response = requests.get(url)
    return response.json()

def getSeasonDetails(showID, seasonNumber):
    url = "https://api.themoviedb.org/3/tv/" + str(showID) + "/season/" + str(seasonNumber) + "?api_key=" + APIKey
    response = requests.get(url)
    return response.json()

def getEpisodeDetails(showID, seasonNumber, episodeNumber):
    url = "https://api.themoviedb.org/3/tv/" + str(showID) + "/season/" + str(seasonNumber) + "/episode/" + str(episodeNumber) + "?api_key=" + APIKey
    response = requests.get(url)
    return response.json()

def getSeasonCount(showID):
    url = "https://api.themoviedb.org/3/tv/" + str(showID) + "?api_key=" + APIKey
    response = requests.get(url)
    return response.json()["number_of_seasons"]

def getEpisodeImage(showID, seasonNumber, episodeNumber):
    url = "https://api.themoviedb.org/3/tv/" + str(showID) + "/season/" + str(seasonNumber) + "/episode/" + str(episodeNumber) + "/images?api_key=" + APIKey
    response = requests.get(url)
    return response.json()

def getStill(showID, seasonNumber, episodeNumber, stillURL):
    url = "https://image.tmdb.org/t/p/original" + stillURL
    response = requests.get(url)
    return response
    