def fact( n ):
   
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2 :
        return 1
    else :
        return n * fact(n - 1)
    
        
print(fact(34))



import math

def fact(n):
    if n==0:
        return 1
    else:
        print(math.factorial(n))
fact(3)
    
    
    
    
num=int(input('enter the number'))
    
def fact( n ):
       
    if n < 1 :
        return 1
    else :
        return n * fact(n - 1)
    
        
print(fact(num))