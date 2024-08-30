class kitutuma:
    def __init__(self,cpu,ram):
     self.cpu = cpu
     self.ram = ram

    def config(self):
        print("CONFIG IS : ", self.cpu,self.ram)
com1 = kitutuma('CORE !8',8)
com2 = kitutuma('CORE !5',16)

com1.config()
com2.config()