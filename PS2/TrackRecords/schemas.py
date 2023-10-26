# from pydantic import BaseModel

# class TrackBase(BaseModel):
#     name: str

# class TrackCreate(TrackBase):
#     pass

# class Track(TrackBase):
#     id : int

#     class Config:
#         from_attributes = True

# class PilotBase(BaseModel):
#     name: str
#     car: str
#     skin: str

# class PilotCreate(PilotBase):
#     pass

# class Pilot(PilotBase):
#     id : int

#     class Config:
#         from_attributes = True

# class SessionBase(BaseModel):
#     lapsCount: int
#     duration: int

# class SessionCreate(SessionBase):
#     pass

# class Session(SessionBase):
#     id : int

#     class Config:
#         from_attributes = True

# class LapBase(BaseModel):
#     lap : int
#     car : int
#     time : int
#     cuts : int
#     tyre : str

# class LapCreate(LapBase):
#     pass

# class Lap(LapBase):
#     id : int

#     class Config:
#         from_attributes = True

# class BestLapBase(BaseModel):
#     lap_car = int
#     lap_time = int
#     lap_lap = int

# class BestLapCreate(BestLapBase):
#     pass

# class BestLap(BestLapBase):
#     pass

