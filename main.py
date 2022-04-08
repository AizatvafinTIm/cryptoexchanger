from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3
from string import ascii_letters
import random
from config import TOKEN
from utils import RegisterStates
from db import BotDB

bot = Bot(TOKEN)
bot_db = BotDB("exchanger_users.db")
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.chat.id,
                           "Привет! Спасибо, что выбрал именно наш p2p обменник. Чтобы выполнять сделки тебе нужно зарегистрироваться(/register)")


@dp.message_handler(commands=['register'])
async def start(msg: types.Message):

    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(RegisterStates.all()[0])


@dp.message_handler(state=RegisterStates.Register_STATE_0)
async def first_register_state(msg: types.Message):
    await msg.reply('Напиши своё имя и фамилию')
    state = dp.current_state(user=msg.from_user.id)
    await state.set_state(RegisterStates.all()[1])


@dp.message_handler(state=RegisterStates.Register_STATE_1)
async def second_register_state(msg: types.Message):

    state = dp.current_state(user=msg.from_user.id)
    
    await state.set_state(RegisterStates.all()[2])



def get_address_of_wallet():
    address = []
    for i in range(11):
        address.append(random.choice(ascii_letters))
    return ''.join(address)


executor.start_polling(dp)
