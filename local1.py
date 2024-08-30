a = 24
print(id(a))
def num():

        a = 19
        x = globals()['a']
        print(id(x))
        print(a)
        globals()['a']= 23
num()
print(a)