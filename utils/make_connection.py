import configparser
from telethon import TelegramClient


class TelegramConnectionManager:
    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.api_id = config['Telegram']['api_id']
        self.api_hash = config['Telegram']['api_hash']
        self.phone = config['Telegram']['phone']
        self.username = config['Telegram']['username']

    async def get_client(self):
        client = TelegramClient(self.username, api_id=self.api_id,
                                api_hash=self.api_hash)
        await client.start()
        return client
