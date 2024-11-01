# Aiogram imports
from aiogram import Dispatcher, Bot
from bot.handlers import main_router

# Other imports
import asyncio, os
import logging, sys
from dotenv import load_dotenv 


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

async def main():
    '''START BOT'''
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
