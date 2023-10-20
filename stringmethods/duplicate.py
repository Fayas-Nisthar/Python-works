word="goodmorning"
srt_word=sorted(word)
count=len(word)
for i in range(0,count-1):
    j=i+1
    if(srt_word[i]==srt_word[j]):
        print(srt_word[i])