lst=[1,2,4,2,6,7,8,3]
count=0
for i in range(1,len(lst)-1):
    x=lst[i-1]
    y=lst[i]
    z=lst[i+1]
    if x<y>z:
        count+=1
        print(f"peak={x,y,z}")
 
    elif x>y<z:
        count+=1
        print(f"valley={x,y,z}")



