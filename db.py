import peewee
from peewee import *


db = MySQLDatabase('u1828261_lucy', user='u1828261_admin', passwd='pN7iQ3rM3zyT5rJ8', host='31.31.198.36', port=3306, autoconnect=True)

class Main(peewee.Model):
    chat_id = peewee.CharField(primary_key=True)
    poops_current = peewee.IntegerField()
    poops_alltime = peewee.IntegerField()

    class Meta:
        database = db


class DB():

    row = Main()

    def __init__(self, chat_id):
        if db.close():
            db.connect()
        row = Main.get_or_create(chat_id=chat_id)
        self.row = row[0]

        if row[1]:
            self.row.poops_alltime = 0
            self.row.poops_current = 0

        pass

    def getRowByChatId(self, chat_id):
        return Main.get(Main.chat_id == chat_id)

    def getPoopsByAllTime(self):
        return self.row.poops_alltime
    
    def __addPoopsByAllTime(self,count):
        self.row.poops_alltime += count
        self.row.save()

    def getCurrentPoops(self):
        return self.row.poops_current
    
    def setCurrentPoops(self, count):
        self.row.poops_current = count
        self.row.save()

    def addCurrentPoops(self, count):
        self.row.poops_current += count
        self.__addPoopsByAllTime(count)
        self.row.save()
