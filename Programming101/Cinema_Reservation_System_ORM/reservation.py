from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from connection import Base


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    row = Column(Integer)
    col = Column(Integer)

    projection_id = Column(Integer, ForeignKey("projections.id"))
    projection = relationship("Projection", backref="reservations")
