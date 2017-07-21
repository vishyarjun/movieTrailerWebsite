import webbrowser
import video
import json_api


# Class and Parent Class initializing
class Movie(video.Video):
    """ This class is used to define a movie and its attributes """

    # Attribute of the Movie Class
    MOVIE_STAR_RATING = [1, 2, 3, 4, 5]

    def __init__(self, movie_id, trailer_youtube):
        """
        Instances of the Class object

        :param movie_id:
        :param trailer_youtube:
        """

        # Calls parent class to set attributes
        self.json_result = json_api.get_movie_details(movie_id)

        video.Video.__init__(self,
                             self.json_result['original_title'],
                             self.json_result['overview'],
                             self.json_result['poster_path'],
                             trailer_youtube)

        self.rating = self.json_result['vote_average']
        self.stars = self.get_stars(self.rating)
        self.genres = self.json_result['genres']

    def get_stars(self, rating):
        """
        Method to display star rating for the movie
        based on rating out of 10

        :param rating: string
        :return: Star rating.
        """
        self.rating = rating
        str2 = "*"
        out = ""
        i = 1
        while i < rating:
            out = out + str2
            i = i + 1

        return out
