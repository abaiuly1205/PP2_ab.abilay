import os 
   
path = os.getcwd() 
   
dir_list = os.listdir(path) 
   
print("Files and directories in '", path, "' :")  
for x in dir_list: 
        print(x)
print("Directories:") 
for dir in dir_list: 
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)
print("Files:")   
for file in dir_list:
    if os.path.isfile(os.path.join(path, file)):
        print(file)