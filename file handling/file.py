#file handling
#opening file
with open("scratch.txt", mode='r')as file:
    data = file.readline()

print(data)
#creating new file
with open('Readme.txt', 'w')as file:
   file.write("This is the new file")
    file.writelines(["This is line 1","\nThis is line 2"])

  #read file
with open('Readme.txt', 'r')as file:
   data = file.readline()
   print(data)
