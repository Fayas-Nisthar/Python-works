from json import load
with open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\products\\item.json",encoding="utf-8")as f:
    data=load(f)
# print total num of product
# print(len(data))

# print all categories
all_categories={p.get("category") for p in data}
# print (all_categories)

# print electronic product name
electronic=[e.get("title")for e in data if e.get("category")=="electronics"]
# print(electronic)

# top rating
rating=[r.get("rating") for r in data]
mrating=max(rating,key=lambda rt:rt.get("rate"))
# print(mrating)

#top rated product
top_rating=max(data,key=lambda r:(r.get("rating").get("rate")))
# print(top_rating.get("title"))

# product having category womens clothing price range (100-300)
product=[p.get("title") for p in data if p.get("category")=="women's clothing" if p.get("price")>10 and p.get("price")<30]
# print(product)

# which product got most number of ratings
max_count=max(data,key=lambda c:(c.get("rating")).get("count"))
# print(max_count.get("title"))

# jwellery product with rating>3
# jwellery=[j.get("title") for j in data if j.get("category")=="jewelery" if j.get("rating").get("rate")>3]
# print(jwellery)

#sort product wrt price order by desc
srt_items=sorted(data,reverse=True,key=lambda p:p.get("price"))
item=[i.get("title") for i in srt_items]
# print(item)

#categorywise product count

wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
# print(wc) 
val_key=[(v,k) for k,v in wc.items()]
# print(max(val_key))   #character and value checking
print(max(val_key, key=lambda m:m[0]))