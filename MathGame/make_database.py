from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MathProblem(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Integer)


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    points = Column(Integer)
