import asyncio
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

import commands

API_TOKEN = '6507692415:AAFOBIaBXYvhyblm2Xt7vY2lkRsshBdxM_E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help']) 
async def send(message: types.Message):
      await message.answer(c.describe_commands(message.chat.id))

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
   await message.answer(c.welcome(message.chat.id))
   await message.answer_sticker(sticker='CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE') 

@dp.message_handler(commands=['lucy_active'])
async def send(message: types.Message):
     await message.answer(c.lucy_act())
     while (c.lucy_active):
          await message.answer(c.lucy_actions(message.chat.id))
          await asyncio.sleep(c.zoomies_interval())

@dp.message_handler(commands=['pet']) 
async def send(message: types.Message):
      await message.answer(c.pet())

@dp.message_handler(commands=['yell']) 
async def send(message: types.Message):
      await message.answer(c.yell(message.chat.id))

@dp.message_handler(commands=['purr_pet']) 
async def send(message: types.Message):
      await message.answer(c.purr_pet())

@dp.message_handler(commands=['scold']) 
async def send(message: types.Message):
      await message.answer(c.scold(message.chat.id))

@dp.message_handler(commands=['clean']) 
async def send(message: types.Message):
      await message.answer(c.clean(message.chat.id))

@dp.message_handler(commands=['play']) 
async def send(message: types.Message):
      await message.answer(c.play())

@dp.message_handler(commands=['feed']) 
@dp.async_task
async def send(message: types.Message):
      await message.answer(c.feed())
      if (c.not_hungry):
            await asyncio.sleep(c.poop_interval())
            await message.answer(c.pooped(message.chat.id))

@dp.message_handler(commands=['open_door']) 
async def send(message: types.Message):
      await message.answer(c.open_door())

@dp.message_handler(commands=['poops']) 
async def send(message: types.Message):
      await message.answer(c.poops(message.chat.id))

@dp.message_handler()
async def echo(message: types.Message): 
      if c.trigger(message.text):
            await message.answer_sticker(sticker=c.random_sticker())   

if __name__ == '__main__':
   c = commands.Commands()
   executor.start_polling(dp, skip_updates=True)