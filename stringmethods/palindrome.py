word="hello"
p_str=""
count=len(word)
# for i in range(0,count):
#     print(word[i])
for j in range(count-1,-1,-1):
    p_str+=word[j]
print(p_str)
print("palindrome" if word==p_str else "not palindrome")