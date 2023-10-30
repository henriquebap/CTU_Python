from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Track(Base):
    __tablename__ = "TRACK"

    id = Column(Integer, primary_key=True, autoincrement=True)
    track_name = Column(String(100), nullable=False)

class Pilot(Base):
    __tablename__ = "PILOT"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    car = Column(String(30), nullable=False)
    skin = Column(String(30), nullable=False)
    # track_id = Column(Integer, ForeignKey('track.id'), nullable=False)

class Sessao(Base):
    __tablename__ = "Sessao"

    id = Column(Integer, primary_key=True)
    lapsCount = Column(Integer)
    duration = Column(Integer)


class Lap(Base):
    __tablename__ = "Lap"

    id = Column(Integer, primary_key=True)
    lap = Column(Integer)
    car = Column(Integer)
    time = Column(Integer)
    cuts = Column(Integer)
    tyre = Column(String(25))

    # sessao_id = Column(Integer, ForeignKey('Sessao.id'), nullable=False)
    # bestlaps = relationship("BestLap", back_populates="lap")

# class BestLap(Base):
#     __tablename__ = "BestLap"

#     lap_car = Column(Integer, ForeignKey('Lap.car'))
#     lap_time = Column(Integer, ForeignKey('Lap.time'))
#     lap_lap = Column(Integer, ForeignKey('Lap.lap'))
