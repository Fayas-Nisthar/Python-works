from json import load
with open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\movies\\db.json")as f:
    data=load(f)
# print(len(data))
movie_names=[mv.get("Title") for mv in data]
# print(movie_names)

#print all directors
directors={d.get("Director") for d in data}
directors.discard("N/A")
# print(directors)

#highest rating
filterded_rating=[m for m in data if m.get("imdbRating")!="N/A"]
top_rating=max(filterded_rating,key=lambda m:float(m.get("imdbRating")))
# print(top_rating.get("Title"))

#print all genre  #myself
# genres=[g.get("Genre") for g in data]
# word=str(genres).replace("[","").replace("'","").replace("]","").replace(",","").split(" ")
# wc=set(word)
# print(wc)


all_geners=set()
all_geners=set()
for m in data:
    for gn in m.get("Genre").split( ):
        all_geners.add(gn.rstrip(","))
# print(all_geners)

# print all movie with genre action
# for mv in data:
    # if mv.get("Genre").count("Action")>0:
        # print(mv.get("Title"))

# movie released before 2014
for mv in data:
    r_date=mv.get("Released")
    year=r_date.split( )[-1]
    
    if year.isdigit():
        if int(year)>2014:
            print(mv.get("Title"))

