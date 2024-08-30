def Kitutuma(name,**data) :
    print(name)
    print(data)
    for key, value in data.items() :
       print(f"{key}:{value}")
Kitutuma('ABDUSSALAAM',age= 24,city='TANGA',Address='CHUKWANI',Contact= 693834464)