from aiogram import types, filters
from aiogram import Router
from .states_file import states
from database.bot_base import add_new_user, user_exists, get_user_name
#from database.models import models
from lexicon.lexicon import LEXICON


router_comm = Router()

@router_comm.message(filters.CommandStart())
async def starting_command(message: types.Message):
    await message.answer(LEXICON["/start"])
    if not await user_exists(message.from_user.id):
        await message.answer("You are new! What is your name?")
        states["prompted_name"] = True
    else:
        await message.answer(f"You're an old head! Welcome back, {await get_user_name(id=message.from_user.id)}")
    

    
@router_comm.message(lambda x: x.text and states["prompted_name"])
async def get_name(message: types.Message):
    if states["prompted_name"]:
        name = message.text
        await message.answer(f"Hello, {name}")
        await add_new_user(message.from_user.id, name)
        states["prompted_name"] = False


@router_comm.message(filters.Command(commands=["cancel", "stop"]))
async def stop(message: types.Message):
    global states
    states = dict.fromkeys(states, False)
    await message.answer("Ok")


