#coding:utf-8
class TheThing(object):#定义TheThing的class内容
    def __init__(self):#初始化第一数值为0
        self.number=0

    def some_function(self):
        print"I got called."
    def add_me_up(self,more):#定义add_me_up的self和more
        self.number+=more
        return self.number
#两个不同的东西
a=TheThing()
b=TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

################
import random as r
class Fish:
    def __init__ (self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x-=1
        print("我的位置：",self.x,self.y)

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
        
    def eat(self):
        if self.hungry:
            print("吃货的梦想是天天有得吃"）
            self.hungry=False
        else:
            print("太饱了"）

                    
