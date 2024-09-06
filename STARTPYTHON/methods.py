class DoMath:
    def addition(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x - y
    
    def mutiplication(self, x , y):
        return x * y
    

first_object = DoMath()
print(first_object.addition(5, 6))
print(first_object.subtraction(7, 8))
print(first_object.mutiplication(10, 11))


second_object = DoMath()
print(second_object.addition(20,21))
print(second_object.subtraction(25,20))
print(second_object.mutiplication(20,30))
