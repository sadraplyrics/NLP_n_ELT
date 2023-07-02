from aiogram import types, filters
from aiogram import Router
from states_file import states
from database.bot_base import new_user


router_comm = Router()

@router_comm.message(filters.CommandStart())
async def starting_command(message: types.Message):
    await message.answer("Sup!\nMy name is NLP_ELT_bot")
    await new_user()
    


@router_comm.message(filters.Command(commands=["cancel", "stop"]))
async def stop(message: types.Message):
    if states["nums_active"] or states["prompted"]:
        states["nums_active"] = False
        states["prompted"] = False
        await message.answer("Ok")