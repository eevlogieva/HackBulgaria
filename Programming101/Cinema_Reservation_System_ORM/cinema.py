from movie import Movie
from projection import Projection
from reservation import Reservation


class Cinema():
    def __init__(self, session):
        self.__session = session

    def add_movie(self, movie_name, movie_rating):
        movie = Movie(name=movie_name, rating=movie_rating)
        self.__session.add(movie)
        self.__session.commit()

    def add_movies(self, data_for_movies):
        movies = []
        for movie in data_for_movies:
            movies.append(Movie(name=movie[0],
                                rating=movie[1]))
        self.__session.add_all(movies)
        self.__session.commit()

    def add_projection(self, projection_type, projection_datetime, movie_id):
        projection = Projection(type=projection_type,
                                dateTime=projection_datetime,
                                movie_id=movie_id)
        self.__session.add(projection)
        self.__session.commit()

    def add_projections(self, data_for_projections):
        projections = []
        for projection in data_for_projections:
            projections.append(Projection(type=projection[0],
                                          dateTime=projection[1],
                                          movie_id=projection[2]))

    def add_reservation(self, current_username, current_projection_id, current_row, current_col):
        reservation = Reservation(username=current_username,
                                  projection_id=current_projection_id,
                                  row=current_row,
                                  col=current_col)
        self.__session.add(reservation)
        self.__session.commit()

    def show_movies(self):
        all_movies = session.query(Movie).order_by(Movie.rating).all()
        return all_movies

