def beuty(name,**data):
    print(name)
    print(data)
    for key,values in data.items():
       print(f"{key} :{values}")
beuty("SALMA",FULL_NAME='salma hamad ali',Borned= 2002,Place='WETE',Address= 'Kipangani',Contact= 656097952)