import asyncio
from bot_instances import async_bot_instance

if __name__ == '__main__':
    asyncio.run(async_bot_instance.polling())