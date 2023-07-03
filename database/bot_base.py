import sqlite3
import asyncio
import random

conn = sqlite3.connect("database/nlp_app.db")
c = conn.cursor()


async def add_new_user(id, name) -> None:
    with conn:
        c.execute(f"INSERT INTO users VALUES ({id}, '{name}')")
        conn.commit()


async def user_exists(id) -> bool:
    with conn:
        c.execute(f"SELECT 1 FROM users WHERE id={id}")
        conn.commit()
        return (bool(c.fetchone()))
    
    
async def get_user_name(id) -> str:
    with conn:
        c.execute(f"SELECT name FROM users WHERE id={id}")
        conn.commit()
        return c.fetchone()[0]


async def get_random_word() -> tuple:
    with conn:
        c.execute(f"SELECT * FROM words WHERE id={random.randint(0, 13160)}")
        return c.fetchone()
    

async def add_word_to_vocab(user_id, word_id, level):
    with conn:
        c.execute(f"INSERT INTO user_words VALUES (last_insert_rowid(), {user_id}, {word_id}, {level})")

async def words_i_know(id):
    out = ""
    with conn:
        c.execute(f"""SElECT w.word, w.meaning FROM
words AS w JOIN user_words AS uw ON w.id = uw.word_id
WHERE uw.user_id = {id}""")
        for pair in c.fetchmany(5):
            out += f"word: {pair[0]}\nmeaning: {pair[1]}\n\n"
        return out


"""async def main():
    print(await words_i_know(503248804))


asyncio.run(main())"""