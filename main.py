import aiogram
import dotenv

dotenv.load_dotenv()



main_bot = aiogram.Bot("token")
disp = aiogram.Dispatcher(main_bot)


@disp.message_handler()
async def do_stuff(message: aiogram.types.Message):
    chat_id = message.chat.id
    text = "Check out this cool hamster!"
    link = "https://i.pinimg.com/564x/86/19/5b/86195b199cb576d170594ec66ebb2c64.jpg"

    await main_bot.send_message(chat_id=chat_id, text=text)
    await main_bot.send_photo(chat_id=chat_id, photo=link)
    


if __name__ == "__main__":
    aiogram.utils.executor.start_polling(disp)