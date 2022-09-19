#Write a python program to delete the age property of the user.

class user:
    name='rahul'
    age=20
    email='rahul@gmail.com'
    
print('Value in age property of user class :',user.age)

del user.age

print('after deleting age property :',user.age)