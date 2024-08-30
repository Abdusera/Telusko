class over:
    def __init__(self,A1,A2):
        self.A1 = A1
        self.A2 = A2

    def sum(self,a=None,b=None,c=None):
        B = 0
        if a!=None and b!=None and c!=None:
          B = a + b + c
        elif a!=None and b!=None:
          B = a+b
        else:
          B = a
          return B
B1 = over(11,22)
print(B1.A1)
print(B1.sum(23,32,2))



