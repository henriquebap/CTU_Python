import json
from database import SessionLocal, models
def create_track(json_file_path: str):
    db = SessionLocal()
    
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if 'track' in data:
                track_name = data["track"]

                db_track = models.Track(track_name=track_name)
                db.add(db_track)
                db.commit()
                db.refresh(db_track)
            else:
                raise ValueError("JSON data does not contain the 'track' field.")
    finally:
        db.close()

    return db_track

def create_pilot(track_id: int,json_file_path: str):
    db = SessionLocal()

    try:

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if all(key in data for key in ["name", "car", "skin"]):
                pilot_name = data["name"]
                pilot_car = data["car"]
                pilot_skin = data["skin"]

                db_pilot = models.Pilot()
                db_pilot = models.Pilot(name=pilot_name, car=pilot_car, skin=pilot_skin)
                db_pilot.track_id = track_id
                db.add(db_pilot)
                db.commit()
            else:
                raise ValueError("O Arquivo Json nao tem o campo chamado 'name', 'car' ou 'skin'. ")
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo Json em {json_file_path} nao foi encontrado")
    finally:
        db.close() 
    
    return db_pilot

def create_session(json_file_path: str):
    db = SessionLocal()

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if all(key in data for key in ["lapsCount", "duration"]):
                session_lapsCount = data["lapsCount"]
                session_duration = data["duration"]

                db_session = models.Sessao()
                db_session = models.Sessao(lapsCount=session_lapsCount, duration = session_duration)
                db.add(db_session)
                db.commit()
                db.refresh(db_session)
            else:
                raise ValueError("O Arquivo Json nao tem o campo chamado 'lapsCount' ou 'duration'. ")
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo Json em {json_file_path} nao foi encontrado")        

    finally:
        db.close()

    return db_session

def create_lap(json_file_path: str, sessao_id: int):
    db = SessionLocal()

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if all(key in data for key in ["car", "time", "cuts", "tyre"]):
                lap_car = data["car"]
                lap_time = data["time"]
                lap_cuts = data["cuts"]
                lap_tyre = data["tyre"]



                db_lap = models.Lap()
                db_lap = models.Lap(time = lap_time, car = lap_car, cuts = lap_cuts, tyre = lap_tyre)
                db_lap.sessao_id = sessao_id

                db.add(db_lap)
                db.commit()
                db.refresh(db_lap)
            else:
                raise ValueError("O Arquivo Json nao tem o campo chamado 'lapsCount' ou 'duration'. ")
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo Json em {json_file_path} nao foi encontrado")        

    finally:
        db.close()

    return db_lap

# def create_bestlap(lap_car, lap_time, lap_lap):
#     db = SessionLocal()

#     try:
#         db_bestlap = models.BestLap(lap_car=lap_car,
#             lap_time=lap_time,
#             lap_lap=lap_lap)
#         db.add(db_bestlap)
#         db.commit()
#         db.refresh(db_bestlap)

#     finally:
#         db.close()
    
#     return db_bestlap


def get_track(track_id):
    db = SessionLocal()
    try:
        track = db.query(models.Track).filter(models.Track.id == track_id).first()
        return track
    finally:
        db.close()

def delete_track(track_id):
    db = SessionLocal()
    try:
        db.query(models.Track).filter(models.Track.id == track_id).delete()
        db.commit()
    finally:
        db.close()
    