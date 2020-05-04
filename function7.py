a=10
print(id(a))

def something():
    a=9

    x=globals() ['a']               # globals give aal the global variable with a name a
    print(id(x))
    print("in fun",a)

something()
print("outside",a)