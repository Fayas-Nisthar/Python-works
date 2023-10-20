def capitalize(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper
@capitalize
def morning():
    return "good morning"
@capitalize
def afternoon():
    return "good after noon"

# print (morning())
# print(afternoon())