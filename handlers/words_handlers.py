from aiogram import types, filters
from aiogram import Router
from .states_file import states
from database.bot_base import get_user_name, get_random_word, add_word_to_vocab, words_i_know
#from database.models import models
from lexicon.lexicon import LEXICON


router_words: Router = Router()


word = 0

@router_words.message(filters.Command(commands=["learn_words", "words", "vocabulary"]))
async def learn_words_1(message: types.Message):
    await message.answer("Would you like to learn some new words?")
    states["prompted_words"] = True


@router_words.message(filters.Text(text=["yes", "yeah", "ok"], ignore_case=True), lambda x: states["prompted_words"])
async def learn_words_2(message: types.Message):
    global word
    if states["prompted_words"]:
        word = await get_random_word()
        await message.answer(f"{await get_user_name(message.from_user.id)}, do you know the word {word[1]}")
        states["prompted_words"] = False
        states["words_active"] = True


@router_words.message(filters.Text(text=["yes", "yeah", "ok"], ignore_case=True), lambda x: states["words_active"])
async def learn_words_3(message: types.Message):
    global word
    if states["words_active"]:
        await message.answer("Wonderful! Included in your vocab!")
        await add_word_to_vocab(message.from_user.id, word[0], 2)
        await message.answer("Wish to continue?")
        states["words_active"] = False
        states["prompted_words"] = True

        
@router_words.message(filters.Text(text=["no", "nah"], ignore_case=True), lambda x: states["words_active"])
async def learn_words_3_1(message: types.Message):
    global word
    if states["words_active"]:
        await message.answer(f"Here is the definition: {word[2]}")
        await message.answer(f"Here is the example: {word[3]}")
        await message.answer("I added this word to your vocab and will check it later!")
        await add_word_to_vocab(message.from_user.id, word[0], 2)
        await message.answer("Wish to continue? Type next")
        states["words_active"] = False
        states["prompted_words"] = True
    
# ------------------------- WHEN PROMPTED -------------------------

@router_words.message(filters.Text(text=["next"], ignore_case=True), lambda x: states["prompted_words"])
async def learn_words_4(message: types.Message):
    if states["prompted_words"]:
        states["prompted_words"] = False
        states["words_active"] = True
        await message.answer("Great!, just tell me to stop when you're done using /stop command!")       


@router_words.message(filters.Text(text=["no"], ignore_case=True), lambda x: states["prompted_words"])
async def learn_words_5(message: types.Message):
    if states["prompted_words"]:
        states["prompted_words"] = False
        states["words_active"] = False
        await message.answer("Sad! Maybe next time!")       
        


@router_words.message(filters.Command(commands=["known"]))
async def learn_words_6(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"User {await get_user_name(user_id)} knows the following words:\n{await words_i_know(user_id)}")

        
