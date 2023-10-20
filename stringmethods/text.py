# vowel count
# consonant count


text="Pneumonoultramicroscopicsilicovolcanoconiosis"
count=0
consonant=0
text.casefold()
vowels="aeiou"
for w in text:
    if w in vowels:
        count+=1
    elif w.isalpha:
        consonant+=1

print(f"vowels={count}")
print(f"consonant count={consonant}")


