class BABA :
   def __init__(self):
     self.name1 = "ABDUSSALAAM"
     self.jina = 24
   def compare(self,others):
       if self.name1 == others.name1:
           return True
       else:
           return False


N1 = BABA()
N1.name1 = "BAHASAN"
A1 = BABA()

if N1.compare (A1) :
    print("They are same")
else:
    print("They are different")
print(N1.name1)
print(A1.jina)
