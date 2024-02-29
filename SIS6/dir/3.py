import os

path = '/Users/abylay/PP2_ab.abilay/SIS6'
if os.access(path, os.F_OK):
     print("\n" + os.path.basename(path))
     print("\n" + os.path.dirname(path) + "\n")
else:
     print(f"{path} do not exists")