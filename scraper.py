import requests
from bs4 import BeautifulSoup
import collections

BASE_URL = "https://www.movie-map.com/"


# A data structure to hold a movie
class Movie:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.similar_movies = {} 

    def __str__(self):
        return "\nMovie Name: {}\nMovie Link: {}".format(self.name, self.link)

    def __repr__(self):
        return "\nMovie Name: {}\nMovie Link: {}".format(self.name, self.link)

    def find_similar_movies(self, name, link, similar_movies):
        """ Populates set <similar_movies> with related movies to given movie <name>. """
        movie_list = get_similar_movies(name)
        for movie in movie_list:

            self.similar_movies.append(movie_list)
            


    # make a crawler function thats essentially getting neighbors! 
    # make sure not to crawl through movies 2x
    # should be impltd recursively
    # set for neighbors because sets are constant time checking
    def get_neighbours(self, movie_link): #BFS 
        """ Return all the neighbours of given <movie_link>. """
        



def get_similar_movies(movie_link):
    """ Returns a list of dictionaries that contain a movie's name and link (href).
    Uses Movie Class. 
    """
    
    page = requests.get(BASE_URL + movie_link)
    soup = BeautifulSoup(page.text, 'html.parser') 

    # Find the div with id="gnodMap" which contains our movie links
    gnodMap = soup.find(id="gnodMap")

    movies = [] # create classes for dictionary and list
    movieElements = gnodMap.findChildren("a", recursive=False) # gets nodes, now for each we want the href attribute
    for movieElement in movieElements:
        movie = Movie(movieElement.text, movieElement["href"]) #movieElement.text = name
        movies.append(movie)
    return movies

if __name__ == '__main__':

    scraped_movies = []
    start_movie_name = "Interstellar"
    start_movie_link = "interstellar.html"
    start_movie = Movie(start_movie_name, start_movie_link)

    queue = collections.deque()
    queue.append(start_movie)
    explored_movies = set()

    count = 0
    
    while queue: 
        if count > 3:
            break
        movie = queue.popleft()
        print(movie)
        explored_movies.add(movie) 
        similar_movies = get_similar_movies(start_movie_link)
        print("{} similar movies".format(len(similar_movies)))
        for similar_movie in similar_movies:
            if similar_movie not in explored_movies:
                explored_movies.add(similar_movie)
                queue.append(similar_movie)
        count += 1

        

