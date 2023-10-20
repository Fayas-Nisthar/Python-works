from json import load
with open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\countrys\\data.json",encoding="utf-8") as f:
    data=load(f)
# print(len(data))

#all region
all_region={c.get("region") for c in data}
# print(all_region)

#asian region
asian={c.get("name") for c in data if c.get("region")=="Asia"}
# print(asian)

#independent
independent=[c.get("name") for c in data if c.get("independent")==True]
# print(independent)

#name of country highest population
population=max(data,key=lambda p:p.get("population"))
# print(population.get("name"))

#country borders of india
borders=[c.get("borders") for c in data if c.get("name")=="India"]
print(borders)
