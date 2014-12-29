from cinema import Cinema
import datetime
from connection import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from command_parser import CommandParser


def main():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cinema_city = Cinema(session)
    new_movies_and_projections_in_cinema(cinema_city)
    command_parser = CommandParser()
    command_parser.add_command("show_movies", cinema_city.show_movies)
    cinema_city.show_movies(session)
    command = input(">>>")
    command_parser.run_command(command)
    # command_parser(session, command)


def new_movies_and_projections_in_cinema(cinema):
    cinema.add_movies([["Hunger Games", 3.7],
                       ["Wreck-it Ralph", 5.7],
                       ["Interstellar", 9.8]])
    cinema.add_projections([["3D", datetime.datetime(2014, 4, 3, 20, 20), 1],
                            ["3D", datetime.datetime(2014, 3, 4, 21, 21), 2]])


if __name__ == '__main__':
    main()
