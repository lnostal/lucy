import random
from datetime import datetime, timedelta
from enum import Enum
import main

lucy_name = 'ᴫюся'
pet_lucy_name = 'ᴫюсю'

def generate_action(action, name=lucy_name):
    return '{} {}'.format(name, action)

class lucy_random_actions(str, Enum):
    jump = generate_action('прыгнула на колени кому-то из чата')
    sneeze = generate_action('чихнула')
    zoomies = generate_action('тыгыдыкает по чату')
    annoying_zoomies = generate_action('тыгыдыкает по чувачкам из чата')
    purr = generate_action('замурчала')
    meow = 'из-за угла послышалось громкое мяуканье'
    alone_play = generate_action('гоняет по чату фантик')
    angry = generate_action('рычит на всех из-под кровати')
    steal = generate_action('пытается украсть еду пока никто не видит')
    hungry = generate_action('настойчиво просит еды')
    poop = generate_action('обкакалась')
    milky_step = generate_action('месит лапками пледик с опоссумами и мурчит')
    fight = generate_action('пиздится с контрабасом')
    play = generate_action('носится по чату вместе с муняшей')
    dig = generate_action('копает лоток')
    scratch = generate_action('точит когти об обивку дивана')
    summer_door = generate_action('скребется в дверь')

class user_actions(str, Enum):
    pet = generate_action(pet_lucy_name, 'погладить')
    yell = generate_action(pet_lucy_name, 'крикнуть на')
    purr_pet = 'почесать за ушком'
    scold = generate_action(pet_lucy_name, 'ругать')
    clean = 'убрать какашки'
    play = 'поиграть дразнилкой с ᴫюсей'
    feed = generate_action(pet_lucy_name, 'покормить')
    open_door = 'открыть дверь'

class lucy_reply_actions(str, Enum):
    wanna_pet = lucy_random_actions.purr.value
    not_wanna_pet = generate_action('с презрением посмотрела и убежала')

    worry = generate_action('не может понять, куда унесли ее какашки')
    not_worry = generate_action('даже не заметила')

    wanna_play = generate_action('танцует жопкой и нападает на дразнилку')

    wanna_eat = generate_action('с радостью набрасывается на еду')
    not_wanna_eat = generate_action('понюхала еду и не стала есть')

    wanna_door = generate_action('забежала в другую комнату')
    not_wanna_door = generate_action('с чувством выполненного долга не стала заходить, развернулась и ушла')

    ignore = generate_action('равнодушно игнорирует')

def get_reply_action(*args):
    var = random.choice(args)
    if var == lucy_random_actions.poop:
        main.poop_count += 1
    return var.value

def get_action():
    return random.choice(list(lucy_random_actions)).value


def get_user_action():
    return random.choice(list(user_actions)).value

def get_zoomies_action():
    zomies = [lucy_random_actions.zoomies.value, lucy_random_actions.annoying_zoomies.value, lucy_random_actions.play.value]
    return random.choice(zomies)

def get_time():
    start_time = datetime.now()
    start_time = start_time.replace(hour=2, minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(hours=3)

    random_date = start_time + (end_time - start_time) * random.random()
    return random_date




print(get_action())
print(get_zoomies_action())
print(get_user_action())
print(get_reply_action(lucy_reply_actions.wanna_door, lucy_reply_actions.not_wanna_door, lucy_reply_actions.ignore))