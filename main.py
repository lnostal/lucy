from aiogram import Bot, Dispatcher, executor, types

import actions as a

API_TOKEN = '6507692415:AAFOBIaBXYvhyblm2Xt7vY2lkRsshBdxM_E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

triggers = ["ебать ту люсю", "люся", "люсе", "люсю", "люси"]
rainbow_triggers = ["радуга", "цветовое решение"]

def trigger(message):  
   text = message.lower()
   answer = False

   for t in triggers:
      if t in text:
         answer = True
         break

   return answer


@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   await message.answer("триггерюсь на люсю...")
   await message.answer_sticker(sticker='CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE') 


@dp.message_handler() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   if trigger(message.text):
      await message.answer_sticker(sticker='CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE') 


@dp.message_handler(commands=['help'])
async def commands(message: types.Message):
    for command in list(a.user_actions):
        await bot.send_message(message.from_user.id, f'{command}\n{discription}')
    

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)