text=["hello","hai","hello","hai","good"]
wc={}
for w in text:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)


        
        


# character count
# a:3 
