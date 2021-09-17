class Demo:
    def __init__(self):
        self.public = 10
        self._protected = 20
        self.__private = 30
        
    def publicfun(self):
        print("public fun")
        
    def _protectedfun(self):
        print("protected fun")
    
    def __privatefun(self):
        print("private fun")
        
obj = Demo()
print(obj.public)
print(obj._protected)
obj.publicfun()
obj._protectedfun()

#obj.__privatefun()

#print(obj.__private)
