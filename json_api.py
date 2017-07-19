
import requests
# this python file can be imported and used whenever API call needs to be made
#to retrieve movie from TMDB based on movie id
def get_movie_details(movie_id):
    apikey="?api_key=ddb1cae2b2c35f2ad7e50626679381e5"
    main_api="https://api.themoviedb.org/3/movie/"
    url=main_api+movie_id+apikey
    json_data=requests.get(url).json()
    return json_data

