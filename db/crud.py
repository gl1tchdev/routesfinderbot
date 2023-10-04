from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.engine import engine
from db.models import Station, StationChoice, StationType, SearchSession
from typing import Optional

session_db: Session = Session(bind=engine)


def create_station(short_name: str, full_name: str, code: str) -> Station:
    query = select(Station).where(Station.code == code)
    station_db: Station = Station(short_name=short_name, full_name=full_name, code=code)
    if not session_db.execute(query).one_or_none():
        session_db.add(station_db)
        session_db.commit()
    return station_db


def get_station_by_code(code: str) -> Optional[Station]:
    query = select(Station).where(Station.code == code)
    return session_db.scalar(query)


def create_search_session(user_id: int) -> SearchSession:
    search_session_db = SearchSession(user_id=user_id)
    session_db.add(search_session_db)
    session_db.commit()
    return search_session_db


def get_session_by_user(user_id: int) -> Optional[SearchSession]:
    query = select(SearchSession).where(SearchSession.user_id == user_id and not SearchSession.prompt_finished).order_by(SearchSession.id.desc())
    return session_db.scalar(query)


def get_last_choice(user_id: int) -> Optional[StationChoice]:
    user_session = get_session_by_user(user_id)
    return user_session.stations[-1] if user_session else None


def register_station_choice(station: Station, session: SearchSession, station_type: StationType) -> StationChoice:
    db_station = StationChoice(
        search_session=session,
        station_type=station_type,
        station=station
    )
    session_db.add(db_station)
    session_db.commit()
    return db_station


def set_session_timestamp(user_id: int, timestamp: datetime):
    user_session = get_session_by_user(user_id)
    user_session.timestamp = timestamp
    session_db.commit()
