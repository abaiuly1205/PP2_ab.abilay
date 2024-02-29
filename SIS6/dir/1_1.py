import os 
   
path = os.getcwd() 
   
print("Files in '", path, "' :")  
dir_list = os.listdir(path) 
for file in dir_list:
    if os.path.isfile:
        print(file)