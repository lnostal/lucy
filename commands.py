import actions as a 
import main

# ----- help -----

def describe_commands():
   description = """
/start\tинфо о чате
/help\tподсказка

--вы находитесь здесь--
"""
   for action in list(a.user_actions):
      description += '\n/{} -- {}'.format(action.name, action.value)

   description += "\n/poops -- узнать количество какашек в чате\n\n💩 какашек сейчас: {} 💩".format(main.poop_count)

   return description



# ----- start -----

def welcome():
    welcome_message = """
✨ заведи кошечку в своем чатике ✨
люся не даст заскучать

гайд по чату:

{}
""".format(describe_commands())
    return welcome_message

def to_reply(action):
    if action == a.lucy_random_actions.poop:
       main.poop_count += 1
    return 'вы попытались ' + action.value + '\n'

# ----- pet -----

def pet():
   message = to_reply(a.user_actions.pet)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_pet, a.lucy_reply_actions.not_wanna_pet)
   return message

# ----- roar -----
def roar():
   message = to_reply(a.user_actions.roar)
   message += a.get_reply_action(a.lucy_random_actions.angry, a.lucy_reply_actions.ignore, a.lucy_random_actions.poop)
   return message

# ----- purr_pet -----
def pet():
   message = to_reply(a.user_actions.purr_pet)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_pet, a.lucy_reply_actions.not_wanna_pet)
   return message

# ----- punish -----
def punish():
   message = to_reply(a.user_actions.punish)
   message += a.get_reply_action(a.lucy_reply_actions.not_worry, a.lucy_reply_actions.ignore, a.lucy_random_actions.angry)
   return message

# ----- purr_pet -----
def purr_pet():
   message = to_reply(a.user_actions.purr_pet)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_pet, a.lucy_reply_actions.not_wanna_pet)
   return message

# ----- clean -----
def clean():
    message = to_reply(a.user_actions.clean)
    if main.poop_count == 0:
      return message + "а убирать-то нечего!"
   
    main.poop_count -= 1
    message += "какашки успешно убраны\n"
    message += a.get_reply_action(a.lucy_reply_actions.worry, a.lucy_reply_actions.not_worry, a.lucy_reply_actions.ignore)
    return message


# ----- play -----
def play():
   message = to_reply(a.user_actions.play)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_play, a.lucy_reply_actions.ignore, a.lucy_reply_actions.not_worry)
   return message

# ----- feed -----
def feed():
   message = to_reply(a.user_actions.feed)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_eat, a.lucy_reply_actions.not_wanna_eat)
   return message

# ----- open_door -----
def open_door():
   message = to_reply(a.user_actions.open_door)
   message += a.get_reply_action(a.lucy_reply_actions.wanna_door, a.lucy_reply_actions.not_wanna_door)
   return message

# ----- poops -----
def poops():
    message = "{}\nвсего: {}\n".format('💩'*main.poop_count, main.poop_count)

    if main.poop_count == 0:
       return message + "все убрано, в чате чистота и порядок"

    if main.poop_count < 6:
       return message + "надо бы убраться"
    
    if main.poop_count < 11:
       return message + "в чате стоит странный аромат. на полу рассыпаны какие-то коричневые штуки"
    
    if main.poop_count < 21:
       return message + "вашим мамам за вас стыдно"
    
    if main.poop_count > 20:
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

