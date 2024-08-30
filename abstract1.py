from abc import ABC , abstractmethod

class computer :
    @abstractmethod
    def process (self):
        print("ABSTRACT method is the method which have no declaration or definition")


class Laptop (computer ):
    def process(self):
        print("Running")

class programmer :
    def work(self,com):
        print("solving problems")
        com.process()

class Desktop(computer):
    def process(self):
        print("I'ts also running here")





com = computer()
com1 = Laptop()
com3= Desktop()
prog1= programmer()

prog1.work(com3)