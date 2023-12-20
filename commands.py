import actions as a 
import random
from db import DB
import enums as en

class Commands():

   def __init__(self):
      self.act = a.Actions()
      self.not_hungry = False
      self.lucy_active = False
      pass

   # ----- money -----
#https://www.tinkoff.ru/cf/QjoW9LVrQ7
   def money(self):
      return "покормить кошку (на оплату сервера):\nhttps://www.tinkoff.ru/cf/QjoW9LVrQ7"


   # ----- help -----

   def describe_commands(self, chat_id):
      description = """
/start\tинфо о чате
/help\tподсказка

--вы находитесь здесь--
"""

      for action in list(en.User):
         description += '\n/{} -- {}'.format(action.name, action.value)

      description += "\n/lucy_active -- включить/выключить случайные кошачьи действия"

      row = DB(chat_id)
      description += "\n/poops -- узнать количество какашек в чате\n\n💩 какашек за все время: {} 💩".format(row.getPoopsByAllTime())
         
      return description



   # ----- start -----

   def welcome(self, chat_id):
      welcome_message = """
✨ заведи кошечку в своем чатике ✨
люся не даст заскучать

гайд по чату:

{}
""".format(self.describe_commands(chat_id))
      return welcome_message

   def to_reply(self, action):
      return 'вы попытались ' + action.value + '\n'

   # ----- pet -----

   def pet(self):
      message = self.to_reply(en.User.pet)
      message += en.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- yell -----
   def yell(self, chat_id):
      message = self.to_reply(en.User.yell)
      action = self.act.get_reply_action(en.Lucy_random.angry, en.Lucy_reply.ignore, en.Lucy_random.poop)
      message += action

      row = DB(chat_id)
      if action == en.Lucy_random.poop.value:
         row.addCurrentPoops(1)

      return message

   # ----- purr_pet -----
   def pet(self):
      message = self.to_reply(en.User.purr_pet)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- scold -----
   def scold(self, chat_id):
      message = self.to_reply(en.User.scold)
      action = self.act.get_reply_action(en.Lucy_reply.not_worry, en.Lucy_reply.ignore, en.Lucy_random.angry, en.Lucy_random.poop)
      message += action

      row = DB(chat_id)
      if action == en.Lucy_random.poop.value:
         row.addCurrentPoops(1)

      return message

   # ----- purr_pet -----
   def purr_pet(self):
      message = self.to_reply(en.User.purr_pet)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- clean -----
   def clean(self,chat_id):
      row = DB(chat_id)
      poop_count = row.getCurrentPoops()
      message = self.to_reply(en.User.clean)
      if poop_count == 0:
         return message + "а убирать-то нечего!"
      
      if poop_count == 1:
         row.setCurrentPoops(0)
         message += "какашки успешно убраны\n"
      elif poop_count >= 2:
         chances =  [True, True, False]
         chance = random.choice(chances)
         if not chance:
            poop_count = poop_count - int(poop_count/2)
            row.setCurrentPoops(poop_count)
            message += "половина какашек просыпалась мимо пакетика\n"
         else:
            message += "какашки успешно убраны\n"
            row.setCurrentPoops(0)
      
      message += self.act.get_reply_action(en.Lucy_reply.worry, en.Lucy_reply.not_worry, en.Lucy_reply.ignore)
      return message


   # ----- play -----
   def play(self):
      message = self.to_reply(en.User.play)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_play, en.Lucy_reply.ignore, en.Lucy_reply.not_worry)
      return message

   # ----- feed -----
   def feed(self):
      message = self.to_reply(en.User.feed)
      action = self.act.get_reply_action(en.Lucy_reply.wanna_eat, en.Lucy_reply.not_wanna_eat)
      message += action
      self.not_hungry = action == en.Lucy_reply.wanna_eat.value
      return message

   # ----- open_door -----
   def open_door(self):
      message = self.to_reply(en.User.open_door)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_door, en.Lucy_reply.not_wanna_door)
      return message

   # ----- poops -----
   def poops(self, chat_id):
      row = DB(chat_id)
      poop_count = row.getCurrentPoops()

      message = "{}\nсейчас в чате {} какашек\n".format('💩'*poop_count, poop_count)

      if poop_count == 0:
         message += "все убрано, в чате чистота и порядок"

      elif poop_count < 6:
         message += "надо бы убраться"
      
      elif poop_count < 11:
         message = "в чате стоит странный аромат. на полу рассыпаны какие-то коричневые штуки"
      
      elif poop_count < 21:
         message += "вашим мамам за вас стыдно"
      
      elif poop_count > 20:
         message += "в чате появился новый коричневый массажный ковер. откуда он здесь и почему так странно пахнет?"

      message += "\n\nкакашек за все время: {}".format(row.getPoopsByAllTime())
      return message
   
   # ----- poop -----

   def poop_interval(self):
      #return random.randint(1, 5) #для тестов
      return random.randint(3600, 10800) # в промежутке от часа до трех
   
   def zoomies_interval(self):
      #return random.randint(1, 5) #для тестов
      return random.randint(1800,3600)

   def lucy_act(self):
      self.lucy_active = not self.lucy_active

      if self.lucy_active:
         return "периодически кошечка будет напоминать о себе"
      
      return "кошечка ушла спать в свой домик и больше не будет шуршать по чату"

   def pooped(self, chat_id):
      row = DB(chat_id)
      self.not_hungry = False

      poops = random.randint(1,4)

      msg = "не так давно вы кормили кошечку\n"
      msg += en.Lucy_random.poop.value
      msg += "\n\nв чате стало на {} какашки больше\n".format(poops)

      row.addCurrentPoops(poops)

      return msg
   

   # ----- triggers -----

   def trigger(self,message):  
      triggers = ["ебать ту люсю", "люся", "люсе", "люсю", "люси"]

      text = message.lower()
      answer = False

      for t in triggers:
         if t in text:
            answer = True
            break

      return answer

   # ----- begin -----
   def zoomies(self):
      return self.act.get_zoomies_action()
   # ----- random_sticker -----

   def random_sticker(self):
      stickers = [
         'CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE',
         'CAACAgIAAxkBAAEoDbBlbYY6EIZNi7skrkquYQWApeL3fwACOTsAApP3SUsYbgzulIOKWzME',
         'CAACAgIAAxkBAAEoDbJlbYY9nBDYiZY_RTmaWVi5CPg-NgACeCkAAo_pAUr5r4KMRPYXcTME',
         'CAACAgIAAxkBAAEoDbRlbYZRdbpAdYRTtsQ8PVT_zL3EEAACWysAAqYVAAFKL1bKNHUIlYAzBA',
         'CAACAgIAAxkBAAEoDbdlbYZZcjUaO2qcgEk0kUC0W_qTuAACeSAAAgSGCEocMJB0qFrXgDME',
         'CAACAgIAAxkBAAEoDbplbYZbgdUHTL_46KsR3GH1o5g61wACzyEAAoPDCUrEcMCwm6-mczME']
      
      return random.choice(stickers)