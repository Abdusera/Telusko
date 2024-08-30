class Father:
     def son1(self):
         print("We love our Mom")


     def son2(self):
        print("We love our Dad")


class Mother:
    def son3(self):
        print("We love our Grand Maa")

    def son4(self):
        print("We love our Grand Paa")
s1 = Father()
s1.son1()
s1.son2()
b1 = Mother()
b1.son4()
class Aunt(Mother,Father):
    def cousin(self):
        print("I love my brother and my all children")
    def nephew(self):
        print("I love my brother and my all children and my father too")
A1 = Aunt()
A1.nephew()