import os 
   
path = os.getcwd() 
   
dir_list = os.listdir(path) 
   
print("Files and directories in '", path, "' :")  
print(dir_list)