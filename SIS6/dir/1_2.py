import os 
   
path = os.getcwd() 

dir_list = os.listdir(path)
   
print("Files in '", path ,"':") 
for dir in dir_list: 
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)