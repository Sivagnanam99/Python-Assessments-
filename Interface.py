import abc
class Myinterface( abc.ABC ):
@abc.abstractclassmethod
    def disp( ):
        pass
#print(" Hello from Myclass ")
class Myclass(Myinterface):
    def disp( ):
    pass
o1=Myclass()
