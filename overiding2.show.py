class A:
    def show(self):
        print("Fathers phone")
class B(A):
    def show(self):
        print("My phone")


F = B()
F.show()