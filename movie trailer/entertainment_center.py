import media
import fresh_tomatoes
#Import the other python files to use the following instances

#various instances of the class Movie in file media.py
#Instance 1
movie1 = media.Movie("Dear zindagi",
                     "Story about how one can find happiness in his own life",
                     "http://data1.ibtimes.co.in/en/full/627612/dear \
                     -zindagi.jpg",
                     "https://www.youtube.com/watch?v=5DkO7ksXY8E")
print movie1.title
#print movie1.storyline

#Instance 2
movie2 = media.Movie("Dangal",
                     "Story about how girls are no less than boys",
                     "http://st1.bollywoodlife.com/wp-content/uploads/2016/07/748607.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

#print movie2.title
#print movie2.storyline
#movie2.show_trailer()

#Instance 3
movie3 = media.Movie("3 idiots",
                     "Story about why one should follow his own dreams",
                     "http://kingofwallpapers.com/3-idiots/3-idiots-009.jpg",
                     "https://www.youtube.com/watch?v=K0eDlFX9GMc")

#Instance 4
movie4 = media.Movie("pk",
                     "Story about how an alien made human beings understand \
                     that religion in one's life does nothing \
                     but separate people..",
                     "http://static.koimoi.com/wp-content/new-galleries/2014/10/pk-movie-poster-2.jpg",
                     "https://www.youtube.com/watch?v=SOXWc32k4zA")

#Instance 5
movie5 = media.Movie("My name is Khan",
                     "Story of a muslim whose life was badly \
                     affected after 9/11",
                     "http://www.gstatic.com/tv/thumb/movieposters/7915881/p7915881_p_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=nqxgYT3TYzY")

#Instance 6
movie6 = media.Movie("Sultan",
                     "Story of an Indian who helped a lost pakistani little \
                     girl get back to her home.",
                     "https://i.ytimg.com/vi/zjW5Iw4Zy0Y/movieposter.jpg",
                     "https://www.youtube.com/watch?v=wPxqcq6Byq0")

movies = [movie1,
          movie2,
          movie3,
          movie4,
          movie5,
          movie6]

fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__
#print media.Movie.__module__
#print media.Movie.__name__
