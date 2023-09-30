from db.engine import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List


class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True, index=True)
    short_name = Column(String)
    full_name = Column(String)
    code = Column(String)
    session_id = Column(Integer, ForeignKey('search_sessions.id'))


class SearchSession(Base):
    __tablename__ = 'search_sessions'
    id = Column(Integer, primary_key=True, index=True)
    start_station = relationship(back_populates='station')
    nodes: List['Station'] = relationship()
    end_station = relationship(back_populates='station')