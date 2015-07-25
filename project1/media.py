import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initializes Movie class.
        Args:
            title (str): Title of movie.
            poster_image_url (str): URL of movie poster image.
            trailer_youtube_url (str): YouTube URL of movie trailer.
        """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        """
        Opens youtube url for specific movie.
        """
        webbrowser.open(self.trailer_youtube_url)
