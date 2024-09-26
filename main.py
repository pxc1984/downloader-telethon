"""Main module for this project"""

import asyncio
import toml
from telethon import TelegramClient

config = toml.load('config.toml')


async def run_bot():
    """Function, responsible for main loop"""
    client = TelegramClient( 
        config['app']['client_name'], 
        config['telegram']['api_id'], 
        config['telegram']['api_hash']
    )

    await client.start(config['telegram']['phone_number'])
    while True:
        await asyncio.sleep(60)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())
