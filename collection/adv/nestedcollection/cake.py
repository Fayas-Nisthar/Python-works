cake=[
    {"id":1,"name":"bluberry","shape":"round","varients":[
        {"weight":.5,"price":250},
        {"weight":1,"price":500},]
    },
    
    {"id":2,"name":"blackberry","shape":"square","varients":[
        {"weight":.5,"price":350},
        {"weight":1,"price":550},]
    },

    {"id":3,"name":"red velvet","shape":"heart","varients":[
        {"weight":.5,"price":300},
        {"weight":1,"price":600},]
    },

    {"id":4,"name":"black forest","shape":"square","varients":[
        {"weight":.5,"price":275},
        {"weight":1,"price":550},]
    },

    {"id":5,"name":"kitkat","shape":"round","varients":[
        {"weight":.5,"price":550},
        {"weight":1,"price":900},]
    },
]

#print all cake name
# print([c.get("name") for c in cake])

#print <300
# print([c.get("name") for c in cake for v in c.get("varients") if v.get("price")<300])

#available shapes
# print (set([c.get("shape") for c in cake]))

#highest price
price=[v.get("price") for c in cake for v in c.get("varients")]
# print(max(price))

#highest price cake
# print ([c.get("name") for c in cake for v in c.get("varients") if v.get("price")==max(price)])

#weight 1  price <550
# print([c.get("name") for c in cake for v in c.get("varients") if v.get("weight")==1 and v.get("price")<=550])

#heart shape cake
# print([c.get("name") for c in cake if c.get("shape")=="heart"])

#lowest price
lp_cake=[c.get("name") for c in cake for v in c.get("varients") if v.get("price")==min(price)]