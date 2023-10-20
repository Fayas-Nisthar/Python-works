lst=[i for i in range(1,8)]
day=["holiday" if d==1 or d==7 else "weekday" for d in lst]
print(day)