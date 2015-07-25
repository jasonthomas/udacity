import media
import fresh_tomatoes

# constants
YOUTUBE = 'https://www.youtube.com/watch?v='
WIKIMEDIA = 'https://upload.wikimedia.org/wikipedia/en'


# define Movie objects
memento = media.Movie('Memento',
                      '%s/c/c7/Memento_poster.jpg' % WIKIMEDIA,
                      '%s0vS0E9bBSL0' % YOUTUBE)

pulp = media.Movie('Pulp Fiction',
                   '%s/8/82/Pulp_Fiction_cover.jpg' % WIKIMEDIA,
                   '%swZBfmBvvotE' % YOUTUBE)

darkknight = media.Movie('The Dark Knight',
                         '%s/8/8a/Dark_Knight.jpg' % WIKIMEDIA,
                         '%s5y2szViJlaY' % YOUTUBE)

godfather = media.Movie('The Godfather',
                        '%s/1/1c/Godfather_ver1.jpg' % WIKIMEDIA,
                        '%ssY1S34973zA' % YOUTUBE)

seven = media.Movie('Seven Samurai',
                    '%s/8/84/Seven_Samurai_movie_poster.jpg' % WIKIMEDIA,
                    '%sMwvpUtc1hBU' % YOUTUBE)

interstellar = media.Movie('Interstellar',
                           '%s/b/bc/'
                           'Interstellar_film_poster.jpg' % WIKIMEDIA,
                           '%s0vxOhd4qlnA' % YOUTUBE)

taxidriver = media.Movie('Taxi Driver',
                         '%s/c/c9/Taxi_Driver_poster.JPG' % WIKIMEDIA,
                         '%ssLpMx8_TYOo' % YOUTUBE)

# create list of movies
movies = [memento, pulp, darkknight,
          godfather, seven, interstellar, taxidriver]

# generate web page with movies
fresh_tomatoes.open_movies_page(movies)
