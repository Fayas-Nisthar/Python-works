color_st={"blue","red","green"}
# # color_st.add("yellow")
# # print(color_st)

# st2={"blue","black","green"}
# # set_union=color_st.union(st2)
# # print (set_union)

# # set_intr=color_st.intersection(st2)
# # print(set_intr)

#for removing obj
# color_st.pop()
# color_st.remove("blue")
# color_st.discard("white") #if there is no white, not show errors 
# print(color_st)


lst1=["10","17","12"]
lst2=["13","12","18","10","17"]
st_lst1=set(lst1)
st_lst2=set(lst2)
# # commom_elements=st_lst1.intersection(st_lst2)
# # print(commom_elements)
# diff_elements=st_lst1.difference(st_lst2)
# print(diff_elements)
print (st_lst1.issuperset(st_lst1))
print (st_lst1.issubset(st_lst2))