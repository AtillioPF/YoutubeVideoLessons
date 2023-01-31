# importing a class to use functions, static functions

class Math:
    #creating static methods
    @staticmethod
    def add(num1,num2):
        return num1 + num2
    
    @staticmethod
    def multiply(num1,num2):
        return num1 * num2
    
    @staticmethod
    def add5(num,):
        return num + 5
    
    @staticmethod
    def pr():
        print("Study")
    
    
    
    
print(Math.add(5,4))
print(Math.multiply(5,4))
print(Math.add5(5))
Math.pr()