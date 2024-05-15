from typing import Self
from datetime import date

class calculator:
    def __init__(self,version:int):
        self.version=version
    def discription(self):
        print(f"Currently running Calculator version {self.version}")
    @staticmethod
    def addnumber(*number)->float:
        return sum(number)
if __name__=="__main__":
    calc1=calculator(10)
    calc2=calculator(200)
    calc1.discription()
    calc2.discription()
     