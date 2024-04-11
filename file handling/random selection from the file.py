import random
with open('Readme.txt', 'r')as file:
   name = (file.read())
name_list = name.split("\n")
print((name_list))
print("Choice: "+ random.choice(name_list))