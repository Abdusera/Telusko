from time import sleep
from threading import *
class hello(Thread):
    def run(self):
         for i in range(5):
             print("Hellow")

             sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = hello()
t2 = Hi()
t1.start()#This allow executing different thread
sleep(0.2)
t2.start()

t1.join()
t2.join()


print("BYE")

