from enum import Enum

lucy_name = 'ᴫюся'
pet_lucy_name = 'ᴫюсю'
    
def generate_action(action, name=lucy_name):
    return '{} {}'.format(name, action)

class Lucy_random(str, Enum):
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


class User(str, Enum):
        pet = generate_action(pet_lucy_name, 'погладить')
        yell = generate_action(pet_lucy_name, 'крикнуть на')
        purr_pet = 'почесать за ушком'
        scold = generate_action(pet_lucy_name, 'ругать')
        clean = 'убрать какашки'
        play = 'поиграть дразнилкой с ᴫюсей'
        feed = generate_action(pet_lucy_name, 'покормить')
        open_door = 'открыть дверь'

class Lucy_reply(str, Enum):
        wanna_pet = Lucy_random.purr.value
        not_wanna_pet = generate_action('с презрением посмотрела и убежала')

        worry = generate_action('не может понять, куда унесли ее какашки')
        not_worry = generate_action('даже не заметила')

        wanna_play = generate_action('танцует жопкой и нападает на дразнилку')

        wanna_eat = generate_action('с радостью набрасывается на еду')
        not_wanna_eat = generate_action('понюхала еду и не стала есть')

        wanna_door = generate_action('забежала в другую комнату')
        not_wanna_door = generate_action('с чувством выполненного долга не стала заходить, развернулась и ушла')

        ignore = generate_action('равнодушно игнорирует')

