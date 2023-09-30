from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from config import DB_PATH

engine = create_engine(f'sqlite:///{DB_PATH}')


class Base(DeclarativeBase):
    pass
