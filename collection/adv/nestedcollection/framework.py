frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

# for fw in frameworks:
#     print(fw.get("name"))
#     print(fw.get("rating"))

# fw_names=[fw.get("name") for fw in frameworks]
# print(fw_names)

# all_rating=[fw.get("rating")for fw in frameworks]
# print(all_rating)

# framework=[fw.get("name") for fw in frameworks if fw.get("language")==("python")]
# print(framework)

# ratings=[fw.get("name") for fw in frameworks if fw.get("rating")==5]
# print(ratings)

# id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4)]
# print(id_filter)

less_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(less_rating)

top_rating=max(frameworks,key=lambda fw:fw.get("rating"))
print(top_rating)

srt=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))
print(srt)