import os 
   
path = os.getcwd() 
   
print("Directories in '", path, "' :")  
dir_list = os.listdir(path) 
for dir in dir_list:
    if os.path.isdir:
        print(dir)