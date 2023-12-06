import asyncio
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

import commands

API_TOKEN = '6507692415:AAFOBIaBXYvhyblm2Xt7vY2lkRsshBdxM_E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help']) 
async def send(message: types.Message):
      await message.answer(c.describe_commands())

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
   await message.answer(c.welcome())
   await message.answer_sticker(sticker='CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE') 

@dp.message_handler(commands=['lucy_active'])
async def send(message: types.Message):
     await message.answer(c.lucy_act())
     while (c.lucy_active):
          await message.answer(c.act.get_action())
          await asyncio.sleep(c.zoomies_interval())

@dp.message_handler(commands=['pet']) 
async def send(message: types.Message):
      await message.answer(c.pet())

@dp.message_handler(commands=['yell']) 
async def send(message: types.Message):
      await message.answer(c.yell())

@dp.message_handler(commands=['purr_pet']) 
async def send(message: types.Message):
      await message.answer(c.purr_pet())

@dp.message_handler(commands=['scold']) 
async def send(message: types.Message):
      await message.answer(c.scold())

@dp.message_handler(commands=['clean']) 
async def send(message: types.Message):
      await message.answer(c.clean())

@dp.message_handler(commands=['play']) 
async def send(message: types.Message):
      await message.answer(c.play())

@dp.message_handler(commands=['feed']) 
@dp.async_task
async def send(message: types.Message):
      await message.answer(c.feed())
      if (c.not_hungry):
            await asyncio.sleep(c.poop_interval())
            await message.answer(c.pooped())

@dp.message_handler(commands=['open_door']) 
async def send(message: types.Message):
      await message.answer(c.open_door())

@dp.message_handler(commands=['poops']) 
async def send(message: types.Message):
      await message.answer(c.poops())

@dp.message_handler() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   if c.trigger(message.text):
      await message.answer_sticker(sticker=c.random_sticker())   

if __name__ == '__main__':
   c = commands.Commands()
   executor.start_polling(dp, skip_updates=True)