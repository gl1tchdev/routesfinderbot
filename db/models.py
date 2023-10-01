from db.engine import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from enum import Enum
from typing import List


class StationType(Enum):
    START = 'start'
    NODE = 'node'
    END = 'end'


class Station(Base):
    __tablename__ = 'stations'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    short_name: Mapped[str] = mapped_column()
    full_name: Mapped[str] = mapped_column()
    code: Mapped[str] = mapped_column()


class SearchSession(Base):
    __tablename__ = 'search_sessions'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    stations: Mapped[List['StationChoice']] = relationship()


class StationChoice(Base):
    __tablename__ = 'chosen_stations'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    station_type: Mapped['StationType'] = mapped_column()
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    station: Mapped['Station'] = relationship(Station)
    session_id: Mapped[int] = mapped_column(ForeignKey('search_sessions.id'))
    search_session: Mapped['SearchSession'] = relationship(SearchSession, back_populates='stations')
