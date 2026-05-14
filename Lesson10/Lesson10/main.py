import os

file2 = ("example.txt","x")

file2.close()


with open("example.txt","r")as file2:
    content = file.read()
    print(content)

with open("example.txt", "w") as file2:
    file2.write("hello")
list=["Hello world!\n","Welcome to python!\n"]
with open("example.txt", "w") as file2:
    file2.writelines(lista)

if os.path.exists("example.txt")""
    print("fajlli ekziston")

if os.path.exists("fds.txt")
    print("fajlli ekziston")
else:
    print("fajlli fds nuk ekziston")

with open("example.txt","a")as file:
    file2.write("hello sfd main")

name="Donjea"
age=21

with open("output.txt","a")as file:
    file2.write("Name:"+name + "\n")
    file2.write("Age:" + str(age) + "\n")




