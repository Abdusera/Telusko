class student:
    school = "MADARASATU SYRAT MUHAMMADIYYAH"
    def __init__(self,m1,m2,m3,m4):
        self.m1= m1
        self.m2= m2
        self.m3= m3
        self.m4= m4
    def avg(self):
        return ((self.m1+self.m2+self.m3+self.m4)/4)
    def get_m1(self):
        return self.m1

    @classmethod
    def info(cls):
         return cls.school
    @staticmethod
    def info():
        print("NYOTE MUNAKARIBISHWA NDUGU WANAFUNZI")


s1 = student(12,32,43,11)
s2 = student(65,43,24,20)
s3 =student(65,33,51,39)
s4 = student(22,43,55,10)
print(s1.avg())
print(s2.avg())
print(s3.avg())
print(s4.avg())
print(s1.get_m1())
print(student.info())
student.info()

