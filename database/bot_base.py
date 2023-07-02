import sqlite3
from ..models.models import User
import asyncio

conn = sqlite3.connect("database/nlp_app.db")
c = conn.cursor()

async def new_user(user: User):
    c.execute(f"INSERT INTO users VALUES ({user.id, user.name})")






conn.commit()
conn.close()