import re

def re(s):
    pattern = r'[ ,.]'
    res = re.sub(pattern, ':', s)
    return res

s = input()
result = re(s)
print(result)