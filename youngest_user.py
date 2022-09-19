#Write a python program to create 3 user objects and find the youngest of all.

class user:
    def __init__(self,age):
        self.age=age
    
    def youngest(self1,self2,self3):
        return (self1.age if self1.age<self3.age else self3.age) if self1.age<self2.age else (self2.age if self2.age<self3.age else self3.age)

obj1,obj2,obj3=user(int(input('Enter Age Of First User : '))),user(int(input('Enter Age Of Second User : '))),user(int(input('Enter Age Of Third User : ')))

age=user.youngest(obj1,obj2,obj3)
print('youngest user is user1  age:%d'%obj1.age if obj1.age==age else 'youngest user is user2  age:%d'%obj2.age if obj2.age==age else 'youngest user is user3  age:%d'%obj3.age if obj3.age==age else 'pass')