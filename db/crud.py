from sqlalchemy.orm import Session
from db.engine import engine
from db.models import Station
from enum import Enum

db: Session = Session(bind=engine)


class StationsType(Enum):
    START = 'start_station'
    END = 'end_station'


def create_station(short_name: str, full_name: str, code: str):
    if db.query(Station).filter(Station.code == code).first():
        return
    station_db: Station = Station(short_name=short_name, full_name=full_name, code=code)
    db.add(station_db)
    db.commit()
    return station_db