import asyncio
from utils.make_connection import TelegramConnectionManager


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        TelegramConnectionManager("config.ini").get_client()
    )
