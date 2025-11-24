students = [
    {"name": "Ayan", "score": 92},
    {"name": "Nursultan", "score": 85},
    {"name": "Alikhan", "score": 76},
    {"name": "Aisulu", "score": 88},
    {"name": "Aigerim", "score": 95},
    {"name": "Zhanar", "score": 73},
    {"name": "Dilshat", "score": 67},
    {"name": "Madina", "score": 81},
    {"name": "Yerbol", "score": 79},
    {"name": "Zhanibek", "score": 90},
    {"name": "Aknur", "score": 84},
    {"name": "Bauyrzhan", "score": 69},
    {"name": "Gulnar", "score": 77},
    {"name": "Altynay", "score": 93},
    {"name": "Marlen", "score": 58},
    {"name": "Saltanat", "score": 87},
    {"name": "Timur", "score": 72},
    {"name": "Saule", "score": 96},
    {"name": "Yerlan", "score": 80},
    {"name": "Assem", "score": 70},
]

students_sorted = sorted(students, key=lambda s: s['score'], reverse=True)
for i, s in enumerate(students_sorted, 1):
    print(i, "|", s['name'], "|", s['score'])