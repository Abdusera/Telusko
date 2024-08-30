class A:
    def __init__(self):
        print("In A init")

    def Aa(self):
      print("Feature One -A")
    def Bb(self):
      print("Feature Two")

class B:
    def __init__(self):
        print("In B unit")

    def Aa(self):
        print("Feature one - B")


    def Dd(self):
        print("Feature four")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Init C")
    def feat(self):
        super().Bb()
C1 = C()
C1.Aa()
C1.feat()
