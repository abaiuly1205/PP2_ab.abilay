bread = ["ciabatta", "black bread", "white bread"]
meat = ["horse meat", "beaf", "chicken"]
vegetables = ["avocado", "cucumber", "tomato"]
sauces = ["cheese sauce", "ketchup", "BBQ sauce"]

for b in bread:
    for m in meat:
        for v in vegetables:
            for s in sauces:
                print(f"{b} bread + {m} + {v} + {s}")