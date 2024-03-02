import os

path = os.getcwd()

f = open("dir7.txt", "w")
f.write('1234567890')


if os.path.exists("dir7.txt"):
  os.remove("dir7.txt")
else:
  print("The file does not exist")