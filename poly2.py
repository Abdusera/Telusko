class student:
    def __init__(self,m1,m2):
        self.m1= m1
        self.m2= m2
    def __add__(self, others):
        m1 = self.m1 + others.m1
        m2 = self.m2 + others.m2
        s3 = student(m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = self.m2 + self.m2

        if r1 > r2 :
            return True
        else:
            return False
    def __str__(self):
         return '{} {}'.format ( self.m1,self.m2)

s1= student(22,35)
s2= student(43,22)
s3= s1 + s2
print(s3.m1)
if s1 > s2 :
    print("S1 wins")
else:
    print("S2 WINS")
    print(s1)
    print(s2)



