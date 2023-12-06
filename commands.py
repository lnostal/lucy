import actions as a 
import random
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

   def describe_commands(self):
      description = """
/start\tинфо о чате
/help\tподсказка

--вы находитесь здесь--
"""

      for action in list(en.User):
         description += '\n/{} -- {}'.format(action.name, action.value)

      description += "\n/lucy_active -- включить/выключить случайные кошачьи действия"
      description += "\n/poops -- узнать количество какашек в чате\n\n💩 какашек сейчас: {} 💩".format(self.act.poop_count)
      
      description += "\n" + self.money()
         
      return description



   # ----- start -----

   def welcome(self):
      welcome_message = """
✨ заведи кошечку в своем чатике ✨
люся не даст заскучать

гайд по чату:

{}
""".format(self.describe_commands())
      return welcome_message

   def to_reply(self, action):
      if action == en.Lucy_random.poop:
         self.act.poop_increment()
      return 'вы попытались ' + action.value + '\n'

   # ----- pet -----

   def pet(self):
      message = self.to_reply(en.User.pet)
      message += en.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- yell -----
   def yell(self):
      message = self.to_reply(en.User.yell)
      message += self.act.get_reply_action(en.Lucy_random.angry, en.Lucy_reply.ignore, en.Lucy_random.poop)
      return message

   # ----- purr_pet -----
   def pet(self):
      message = self.to_reply(en.User.purr_pet)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- scold -----
   def scold(self):
      message = self.to_reply(en.User.scold)
      message += self.act.get_reply_action(en.Lucy_reply.not_worry, en.Lucy_reply.ignore, en.Lucy_random.angry, en.Lucy_random.poop)
      return message

   # ----- purr_pet -----
   def purr_pet(self):
      message = self.to_reply(en.User.purr_pet)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_pet, en.Lucy_reply.not_wanna_pet)
      return message

   # ----- clean -----
   def clean(self):
      message = self.to_reply(en.User.clean)
      if self.act.poop_count == 0:
         return message + "а убирать-то нечего!"
      
      if self.act.poop_count == 1:
         self.act.poop_remove()
         message += "какашки успешно убраны\n"

      if self.act.poop_count >= 2:
         chances =  [True, True, False]
         chance = random.choice(chances)
         if not chance:
            self.act.poop_count = self.act.poop_count - int(self.act.poop_count/2)
            message += "половина какашек просыпалась мимо пакетика\n"
         else:
            message += "какашки успешно убраны\n"
            self.act.poop_remove()
      
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
      self.not_hungry = action == en.Lucy_reply.wanna_eat
      return message

   # ----- open_door -----
   def open_door(self):
      message = self.to_reply(en.User.open_door)
      message += self.act.get_reply_action(en.Lucy_reply.wanna_door, en.Lucy_reply.not_wanna_door)
      return message

   # ----- poops -----
   def poops(self):
      message = "{}\nвсего: {}\n".format('💩'*self.act.poop_count, self.act.poop_count)

      if self.act.poop_count == 0:
         return message + "все убрано, в чате чистота и порядок"

      if self.act.poop_count < 6:
         return message + "надо бы убраться"
      
      if self.act.poop_count < 11:
         return message + "в чате стоит странный аромат. на полу рассыпаны какие-то коричневые штуки"
      
      if self.act.poop_count < 21:
         return message + "вашим мамам за вас стыдно"
      
      if self.act.poop_count > 20:
         return message + "в чате появился новый коричневый массажный ковер. откуда он здесь и почему так странно пахнет?"


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

   def pooped(self):
      self.not_hungry = False

      poops = random.randint(1,4)

      for _ in range(poops):
         self.act.poop_increment()

      msg = "не так давно вы кормили кошечку\n"
      msg += en.Lucy_random.poop.value
      msg += "\n\nстало на {} какашек больше\n".format(poops)
      msg += self.poops()

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