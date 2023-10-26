import json
from sqlalchemy.orm import Session
from models import Track

def create_track_from_json(db: Session, json_file_path: str):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            # Suponha que o JSON contenha um campo 'name' para o nome da pista.
            if 'name' in data:
                track_name = data['name']

                # Crie um novo objeto Track com base no nome da pista e insira-o no banco de dados.
                db_track = Track(name=track_name)
                db.add(db_track)
                db.commit()
                db.refresh(db_track)
                return db_track
            else:
                raise ValueError("O arquivo JSON não contém o campo 'name'.")

    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo JSON em {json_file_path} não foi encontrado.")
    except Exception as e:
        raise e
