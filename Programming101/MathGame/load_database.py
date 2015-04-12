from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from make_database import Base


engine = create_engine("sqlite:///math-game.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
