class pycharm:
    def execute(self):
     print("compiling")
     print("Running")
class Myeditor :
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("compiling")
        print("Running")

class laptop:
    def code(self,ide):
      ide.execute()
ide = Myeditor()
lap1 = laptop()
lap1.code(ide)
