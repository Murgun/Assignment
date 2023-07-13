class A:
    def __init__(self, a,b,c):
        self.__a = a #private
        self._b = b #protected
        self.c = c #public

    def display(self):
        print(f"A={self.__a}B={self.__b}C={self.c}")    

class B(A):
    def display(self):
        try:
          print(f"A={self.__a}")
        except Exception:
          print("private var is not accessable")
        finally:     
          print("remaining values are:")
          print(f"B={self._b}\nC={self.c}") 

               
obj=B(34,54,23)
obj.display()


