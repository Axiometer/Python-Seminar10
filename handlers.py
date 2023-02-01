import texts
from aiogram import Bot, Dispatcher, executor, types
from calc_bot import *

# global TOKEN, logger

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Приветствие
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    name = message.from_user.full_name
    logger.info('Поприветствовали пользователя')
    await message.answer(f'{name}, {texts.greetings}')

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    logger.info('Вывели справку')
    await message.answer(f'{texts.HELP_MESSAGE}')

@dp.message_handler()
async def messagehandler(message: types.Message):
    logger.info(f'Пользователь ввел выражение {message.text}')
    answer = 0
    formatted_message = message.text.lower().replace(' ', '')
    try:
        logger.info(f'Вычисляем выражение {formatted_message}')
        answer = str(eval(formatted_message))
        answer = formatted_message + ' = ' + answer
            
    except SyntaxError: answer = False
    except NameError: answer = False
    except TypeError: answer = False
    except ZeroDivisionError: answer = False

    if (not answer):    
        await message.answer("ошибка...")
    else:
        await message.answer(answer)