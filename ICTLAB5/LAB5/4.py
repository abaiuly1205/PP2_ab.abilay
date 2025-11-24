s = input("Enter the sentence: ").lower()
uw = s.split()
print("Number of unique words:", len(set(uw)))