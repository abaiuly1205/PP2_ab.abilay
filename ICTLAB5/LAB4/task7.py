phrase = input("enter a phrase or word: ")
cleaned_phrase = ''.join(char for char in phrase if char.isalnum())
lowercased_phrase = cleaned_phrase.lower()
print("cleaned phrase:", cleaned_phrase)
if lowercased_phrase == lowercased_phrase[::-1]:
    print("the phrase is a palindrome")
else:
    print("the phrase is not a palindrome")