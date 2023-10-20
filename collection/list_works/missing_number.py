lst=[1,2,4]
lst.sort()
i=0
limit=len(lst)-1
while(i<limit):
    j=i+1

    diff=lst[j]-lst[i]
    if diff==1:
        i+=1
    else:
        print(lst[i]+1,"is missing")
        break 




# max_num=max(lst)
# total_sum=max_num*(max_num+1)/2
# cur_sum=sum(lst)
# diff=total_sum-cur_sum
# if (diff==0):
#     print(max_num+1,"is missing")

# else:
#     print(diff,"missing number")