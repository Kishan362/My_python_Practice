#nonlocal in python 

def outer():
    x = "a function ni ander no che"
    def inner():
        nonlocal x
        x = "aa nonlocalche"
        print("printing nonlocal:", x)
    inner()
    print("aa function ni ander no che:", x)


outer()


#1-starts with local
#2-parant local
#3-Global local
#4-built in python