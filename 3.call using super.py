class Siva:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Surya(Siva):
    def __init__(self, txt):
        super().__init__(txt)
    def printf(self):
        print("Siva Is Also M.Sc Student...!")
        
    

x = Surya("Siva Is B.Sc Student..!")

x.printmessage()

x.printf()
