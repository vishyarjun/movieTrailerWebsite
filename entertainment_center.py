import media
import fresh_tomatoes
import datetime

# create an object/instance for movie butterfly effect
butterfly_effect = media.Movie("1954","https://www.youtube.com/watch?v=B8_dgqfPXFg")

# create an object/instance for movie butterfly frida
frida = media.Movie("75780","https://www.youtube.com/watch?v=aRwrdbcAh2s")
# create an object/instance for movie life is beautiful
life_is_beautiful = media.Movie("289","https://www.youtube.com/watch?v=S9ID5DHsX8g")
# create an object/instance for movie god father
god_father = media.Movie("295134","https://www.youtube.com/watch?v=vbk_mDNLWyE")
# create an object/instance for movie premam
premam = media.Movie("409255","https://www.youtube.com/watch?v=pbgvTikmIMk")
# create an object/instance for movie the terminal
the_terminal = media.Movie("594","https://www.youtube.com/watch?v=dgXyQUMRpj4")

movies = [frida,life_is_beautiful,god_father,premam,the_terminal,butterfly_effect]
#calls the fresh_tomatoes methods to display movies in web browser
fresh_tomatoes.open_movies_page(movies)

