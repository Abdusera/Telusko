class nums :
    def __init__(self):
        self.num = 1
    def __iter__(self):# hiv ndio vitu muhimu kweny method za iteration 1 ni method hii ya n iter
        return self
    def __next__(self): #pili ni hii ya next
      if self.num <= 10:
           val= self.num
           self.num +=  1

           return val
      else :
            raise StopIteration
values = nums()
for i in values:
    print(i)
    print(next(values))




