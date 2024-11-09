import asyncio
import os

from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.database.models import create_debil


async def main():
    await create_debil()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot OFF")



