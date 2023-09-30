import asyncio
from bot_instances import async_bot_instance
from db.engine import Base, engine

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    asyncio.run(async_bot_instance.polling())