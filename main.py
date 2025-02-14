import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



from config import TOKEN
import sqlite3
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

button_registr = KeyboardButton(text='Регистрация в телеграм-боте')
button_exchange_rates = KeyboardButton(text='Курс валют')
button_tips = KeyboardButton(text='Советы по экономии')
button_finances = KeyboardButton(text='Личные финансы')

keyboards = ReplyKeyboardMarkup(keyboard=[
    [button_registr, button_exchange_rates],
    [button_tips, button_finances]
    ], resize_keyboard=True)


conn = sqlite3.connect('user.db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    category1 TEXT,
    category2 TEXT,
    category3 TEXT,
    expenses1 REAL,
    expenses2 REAL,
    expenses3 REAL
    )
    ''')

conn.commit()

class FinancesForm(StatesGroup):
    category1 = State()
    expenses1 = State()
    category2 = State()
    expenses2 = State()
    category3 = State()
    expenses3 = State()


@dp.message(CommandStart())
async def send_start(message: Message):
    await message.answer('Привет! Я ваш финансовый помощник. Выберите одну из опций в меню:', replay_markup=keyboard)








async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())