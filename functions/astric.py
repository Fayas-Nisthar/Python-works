# def product(*args):
#     res=1
#     for n in args:
#         res=res*n
#     return res
# print(product(10,20,3))



# def add(*args):
#     ad=0
#     for n in args:
#         ad=ad+n
#     return ad
# print(add(10,20,3,5))

# def add(*args):
#     return sum(args)
# print(add(10,20,30))

def concat_strings(*args):
    #method 1
    # ---------
    # str=""
    # for w in args:
    #     str=str+w
    # return str
     
    #method 2
    #  ---------
    return " ".join(args)

# print(concat_strings("hello","good","morning","all"))


def reverse_concat(*args):
    ar=list(args)
    ar.reverse()
    return ar
print(reverse_concat("red","green","blue"))


