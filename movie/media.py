import webbrowser
class Movie():
    """This is a bullshit class"""
    
    VALID_RATINGS=["G","PG","PG-13","R"]
    
    def __init__(self,movie_title, movie_storyline, poster_image, youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url
        
    def show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
