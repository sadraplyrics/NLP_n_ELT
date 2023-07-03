from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import asyncio
from handlers import nums_handlers, base_commands_handlers, words_handlers


async def main() -> None:
    config: Config = load_config(".env")

    
    elt_bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()


    dp.include_router(base_commands_handlers.router_comm)
    dp.include_router(words_handlers.router_words)
    dp.include_router(nums_handlers.router_nums)
    


    await elt_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(elt_bot)

if __name__ == "__main__":
    asyncio.run(main())