import webbrowser

class Video():
    def __init__(self,movie_title,movie_duration):
        self.title = movie_title
        self.duration = movie_duration
        
class Movie(Video):
#The class Movie gives the info. of different movies.
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
#Another class inheriting the Video class
    def __init__(self,movie_title, movie_duration, seasons,episodes,tv_station):
        Video.__init__(self,movie_title,movie_duration)
        self.seasons = seasons
        self.episodes = episodes
        self.tv_station = tv_station

    def get_local_listing(self):
        print self.movie_title

friends = TvShow("Friends", "22mins", 10, 365, "It's Hot")
#An instance of a TvShow class

#friends.get_local_listing()
#print friends.movie_duration
