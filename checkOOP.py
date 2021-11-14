class A(object):
    def __init__(self,x):
        self.x = x
        
    
class B(A):
    def __init__(self, y):
        A.__init__(self,x = 90)
        self.y = y
        
    def call(self):
        return A.x, self.y
    
a = B(100)

print(a.call())