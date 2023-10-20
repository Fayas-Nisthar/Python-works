lst1=[10,13,15,20,25]
lst2=[12,13,20,25,30]
lst1.sort()
lst2.sort()
i,j=0,0
limit1=len(lst1)
limit2=len(lst2)
while(i<limit1 and j<limit2):
    if lst1[i]==lst2[j]:
        print(lst1[i],lst2[j])
        j+=1
        i+=1
    elif lst1[i]<lst2[j]:
        i+=1
    else:
        j+=1

