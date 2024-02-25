import re
import csv

f = open('row.txt', 'r', encoding='utf8')
text = f.read()

pattern = r"\n(?P<reti>[0-9]+)\.\n(?P<aty>.+)\n(?P<sany>.+)x(?P<bagasy>.+)\n"

res = re.finditer(pattern, text)

with open('data.csv', 'w', newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['reti', 'aty', 'sany', 'bagasy', 'quny'])
    for x in res:
        writer.writerow([
            x.group('reti'), 
            x.group('aty'),
            float(x.group('sany').strip().replace(',','.')),
            float(x.group('bagasy').strip().replace(',','.').replace(' ',''))
        ])