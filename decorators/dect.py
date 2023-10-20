def swap_nums(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_nums
def sub(n1,n2):
    return n1-n2

@swap_nums
def div(n1,n2):
    return n1/n2

print(sub(2,10))
print(div(5,10))