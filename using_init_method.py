#Write a python program to init default values for user object using __init__ method.

class user:
    def __init__(self,val):
        self.variable=val
        print(self.variable)

obj1=user(10)
obj2=user('rahul')