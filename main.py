#!/usr/bin/env python3

import logging
import asyncio
import toml
import datetime
import random
from telethon import TelegramClient
from telethon.errors import RPCError, PeerFloodError, ChatAdminRequiredError, UserNotParticipantError

config = toml.load('config.toml')


async def run_bot():
    await client.start(config['telegram']['phone_number'])
    while True:
        await asyncio.sleep(60)


if __name__ == '__main__':
    client = TelegramClient(
        config['app']['client_name'], 
        config['telegram']['api_id'], 
        config['telegram']['api_hash']
    )
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())
