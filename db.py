import sqlite3 as sq
from aiogram.dispatcher import FSMContext


class BotDB:
    def __init__(self, db_name):
        self.base = sq.connect(db_name)
        self.cur = self.base.cursor()
        self.base.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, address TEXT)')
        self.base.commit()

    async def push_data(self, state):
        async with state.proxy() as data:
            self.cur.execute('INSERT INTO users VALUES (?,?)', tuple(data.values()))
