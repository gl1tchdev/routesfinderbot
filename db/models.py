from db.engine import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from enum import Enum
from typing import List


class StationType(Enum):
    START: str = 'start_station'
    END: str = 'end_station'
    NODE: str = 'node_station'

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = -1
        return members[index]

    def translate(self) -> str:
        translations = {
            'start_station': 'Стартовая станция',
            'end_station': 'Конечная станция',
            'node_station': 'Промежуточная станция'
        }
        return translations[self.value]


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
    user_id: Mapped[int] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)
    prompt_finished: Mapped[bool] = mapped_column(default=False)


class StationChoice(Base):
    __tablename__ = 'chosen_stations'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    station_type: Mapped['StationType'] = mapped_column()
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id'))
    station: Mapped['Station'] = relationship(Station)
    session_id: Mapped[int] = mapped_column(ForeignKey('search_sessions.id'))
    search_session: Mapped['SearchSession'] = relationship(SearchSession, back_populates='stations')
    destination_time: Mapped[int] = mapped_column(default=0)
