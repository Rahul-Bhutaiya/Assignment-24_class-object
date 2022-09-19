"""
Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
"""

class laptop:
    def __init__(self,brand,cpu,ram,hdd):
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd

    def showConfig(self):
        print('Laptop Configurations...\nBrand :',self.brand,'\nCPU :',self.cpu,'\nRAM :',self.ram,'\nHDD :',self.hdd)

#obj1=laptop(input('Enter Brand of Laptop : '),input('Enter CPU of Laptop : '),input('Enter RAM of Laptop : '),input('Enter HDD of Laptop : '))

#obj1.showConfig()