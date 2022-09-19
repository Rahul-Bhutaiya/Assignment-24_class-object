#Write a python program to create a School class and 3 instance variables and 1 class variable.

class School:
    class_var='Aspire Public School'

    def __init__(self,std):
        self.instance_var1=std
    def stud_name(self,name):
        self.instance_var2=name

obj1=School(12)
obj1.ininstance_var3=34