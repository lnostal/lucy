import random
from datetime import datetime, timedelta
import enums as en

class Actions():

    def __init__(self):
         self.poop_count = 0
         pass

    def get_reply_action(self, *args):
        var = random.choice(args)
        return var.value

    def get_action(self):
        var = random.choice(list(en.Lucy_random))
        return var.value

    def get_user_action(self):
        return random.choice(list(en.User)).value

    def get_zoomies_action(self):
        zomies = [en.Lucy_random.zoomies.value, en.Lucy_random.annoying_zoomies.value, en.Lucy_random.play.value]
        return random.choice(zomies)

    def get_time(self):
        start_time = datetime.now()
        start_time = start_time.replace(hour=2, minute=0, second=0, microsecond=0)
        end_time = start_time + timedelta(hours=3)

        random_date = start_time + (end_time - start_time) * random.random()
        return random_date