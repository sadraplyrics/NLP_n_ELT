from aiogram import types, filters
from aiogram import Router
from lexicon.lexocon import LEXICON
from ELT_services import fun_nums
from .states_file import states


router: Router = Router()


@router.message(filters.Command(commands=["nums_facts"]))
async def starting_command(message: types.Message):
    await message.answer("Would you like to know some nums facts?")
    states["prompted"] = True


@router.message(lambda x: x.text and x.text.isdigit())
async def funny_nums(message: types.Message):
    if states["nums_active"]:
        await message.answer(fun_nums.nums_api(message.text))
        #states["known_nums"].append(message.text)
        #states["facts"] += 1
        #await message.answer(f"You now know {states['facts']} facts about numbers")
        await message.answer("Want to know some more?")
        states["prompted"] = True



# ------------------------- WHEN PROMPTED -------------------------
@router.message(filters.Text(text=["yes", "ok"], ignore_case=True))
async def funny_nums_yes(message: types.Message):
    if states["prompted"]:
        states["nums_active"] = True
        states["prompted"] = False
        await message.answer("Cool! Write down the number you'd like to know more about")


@router.message(filters.Text(text=["no", "nah"], ignore_case=True))
async def funny_nums_no(message: types.Message):
    if states["prompted"]:
        states["prompted"] = False
        states["nums_active"] = True
