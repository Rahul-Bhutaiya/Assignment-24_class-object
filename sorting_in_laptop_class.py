"""
WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.
"""

from laptop_class import laptop

obj1,obj2,obj3=laptop('Dell','i5',8,512),laptop('Asus','i5',16,256),laptop('Lenovo','i5',8,512)
tuple_var=obj1.ram,obj2.ram,obj3.ram

sorted_list=sorted(tuple_var)
print(sorted_list)