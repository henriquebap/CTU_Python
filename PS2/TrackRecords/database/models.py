from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Track(Base):
    __tablename__ = "TRACK_T1"

    id = Column(Integer, primary_key=True, autoincrement=True,nullable=False)
    track_name = Column(String(100), nullable=False)
    number_of_sessions = Column(Integer)

    pilots = relationship("Pilot", back_populates="track")

class Pilot(Base):
    __tablename__ = "PILOT_T1"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    car = Column(String(80), nullable=False)
    skin = Column(String(80), nullable=False)
    track_id = Column(Integer, ForeignKey('TRACK.id'), nullable=False)

    # Define the relationship to the 'Track' model
    track = relationship("Track", back_populates="pilots")

class Sessao(Base):
    __tablename__ = "SESSAO"

    id = Column(Integer, primary_key=True)
    lapsCount = Column(Integer)
    duration = Column(Integer)
    laps = relationship("Lap", back_populates="sessao")

class Lap(Base):
    __tablename__ = "LAP"

    id = Column(Integer, primary_key=True)
    lap = Column(Integer, nullable=False)
    car = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    cuts = Column(Integer, nullable=False)
    tyre = Column(String(25), nullable=False)
    sessao_id = Column(Integer, ForeignKey('SESSAO.id'), nullable=False)

    # Define the relationship to the 'Sessao' model
    sessao = relationship("Sessao", back_populates="laps")

class BestLap(Base):
    __tablename__ = "BESTLAP"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lap_car = Column(Integer)
    lap_time = Column(Integer)
    lap_lap = Column(Integer)
