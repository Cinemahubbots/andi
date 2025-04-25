from telethon import TelegramClient
import asyncio
from commands import *
from message_forwarding import *

# Telegram API credentials
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'

# Initialize Telegram client
client = TelegramClient('userbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def main():
    # Start forwarding logic
    await main_forwarding_logic(client)
    print("Bot is now monitoring live messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())