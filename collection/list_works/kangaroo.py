source_word="CHICKEN"
target_word="HEN"
source_word_list=[]
is_kangaroo=True
for ch in source_word:
    source_word_list.append(ch)
for ch in target_word:
    char_count=source_word_list.count(ch)

    if char_count>0:
        source_word_list.remove(ch)
        
    else:
        is_kangaroo=False
        break

print(is_kangaroo)




    
