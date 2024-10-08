import asyncio

from aiogram import Bot, Dispatcher, F

from app.handlers import router


async def main():
    bot = Bot(token="7554867601:AAG2vKwjk52YmUa52p3PW1vMrx0iB0DhfdM")
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot OFF")
