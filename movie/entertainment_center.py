import media
import fresh_tomatoes
toy_story=media.Movie("Toy Story", "The movie of a toy boy and girl","https://www.imdb.com/title/tt1979376/","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("avatar", "The movie of a toy boy and girl","https://www.imdb.com/title/tt1979376/","https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)
print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story,avatar]
#fresh_tomatoes.open_movies_page(movies)
#print(toy_story.VALID_RATINGS)
print(media.Movie.__doc__)
