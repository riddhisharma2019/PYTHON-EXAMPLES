a=10                                   # this is the global variable
def something():
    a=15                                            # this is the local variable
    print("in function",a)                    # so inside this is local, for making some global vaiable we use keyword

something() 

print("outside", a)