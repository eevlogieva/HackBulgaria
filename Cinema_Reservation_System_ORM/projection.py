from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from connection import Base


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    dateTime = Column(DateTime)

    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projections")
