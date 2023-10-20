all_users=["mammotty","mohanlal","dq","fahad","asif","nivin","prithvi"]
nivin_friends=["asif","dq","fahad"]
dq_friend=["mammotty","asif","fahad"]
users=set(all_users)
friends=set(nivin_friends)
# diff=users.difference(friends)
# diff.discard("nivin")
# print (diff)
mutual=friends.intersection(dq_friend)
print(mutual)