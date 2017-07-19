class Video():
    """ This Class is used to define any type of video. Any Class that uses video can inherit this class """
    # initializing the variables
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url="https://image.tmdb.org/t/p/w500/"+poster_image
        self.trailer_youtube_url=trailer_youtube
    # method to show video/trailer of the video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
