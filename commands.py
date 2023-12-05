import actions as a 
import main
import random
import enums as en

class Commands():

   def __init__(self):
      self.act = a.Actions()
      pass


   # ----- help -----

   def describe_commands(self):
      description = """
/start\tинфо о чате
/help\tподсказка

--вы находитесь здесь--
"""
      for action in list(en.User):
         description += '\n/{} -- {}'.format(action.name, action.value)

      description += "\n/poops -- узнать количество какашек в чате\n\n💩 какашек сейчас: {} 💩".format(self.act.poop_count)

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
      
      self.act.poop_remove()
      message += "какашки успешно убраны\n"
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
      message += self.act.get_reply_action(en.Lucy_reply.wanna_eat, en.Lucy_reply.not_wanna_eat)
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

   # ----- triggers -----

   def trigger(message):  
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

   def random_sticker():
      stickers = [
         'CAACAgIAAxkBAAEmnFRlH8-sZCVjHbQBC5RyB0pf5IA99AACDDYAAihN4UhiZoZ0MM9NDDAE',
         'CAACAgIAAxkBAAEoDbBlbYY6EIZNi7skrkquYQWApeL3fwACOTsAApP3SUsYbgzulIOKWzME',
         'CAACAgIAAxkBAAEoDbJlbYY9nBDYiZY_RTmaWVi5CPg-NgACeCkAAo_pAUr5r4KMRPYXcTME',
         'CAACAgIAAxkBAAEoDbRlbYZRdbpAdYRTtsQ8PVT_zL3EEAACWysAAqYVAAFKL1bKNHUIlYAzBA',
         'CAACAgIAAxkBAAEoDbdlbYZZcjUaO2qcgEk0kUC0W_qTuAACeSAAAgSGCEocMJB0qFrXgDME',
         'CAACAgIAAxkBAAEoDbplbYZbgdUHTL_46KsR3GH1o5g61wACzyEAAoPDCUrEcMCwm6-mczME']
      
      return random.choice(stickers)