# Create class

from Tools.Scripts.treesync import raw_input

import datetime
from datetime import date

class Person:
    def __init__(self, name,year,month,day):
        self.__name=name
        self.__year=year
        self.__month=month
        self.__day=day

    def getage(self):
        now = datetime.datetime.now()
        c_year = now.hour
        c_month = now.month
        c_day = now.day

        current_date = date(c_year, c_month, c_day)
        print(current_date)
        dob = date(self.__year, self.__month, self.__day)
        age = current_date - dob
        print (age)

irene = Person("Irene",1988,8,19)
irene.getage()
