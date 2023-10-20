sum=int(input("Enter sum"))
lst=[2,4,6,7,8]
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]

    if cur_sum==sum:
        print(f"pairs are {lst[low],lst[upp]}")
        low+=1
        upp-=1
    elif cur_sum<sum:
        low+=1

    elif cur_sum>sum:
        upp-=1








# lst=[2,4,5,6]
# i=0
# j=0
# n=int(input("enter 6,7 or 11"))
# for i in range(0,3):
#     for j in range(i+1,4):
#         if (lst[i]+lst[j]==n):
#             print(f"Numbers are {lst[i]} and {lst[j]}")
