class student:
     def __init__(self,name,rollno):
         self.name = name
         self.rollno = rollno
         self.lap = self.laptop()
     def show(self):
         print(self.name,self.rollno)
         self.lap.show()
     class laptop:
           def __init__(self):
               self.brand = 'DELL'
               self.generation = 8
               self.speed = 'i7'
               self.memory = '500 GB'

           def show(self):
               print(self.brand,self.generation,self.speed,self.memory)




s1 = student ("ABDUSSALAAM",22)
S2 = student ("SALMA",20)


print(s1.name,s1.rollno)
s1.show()

