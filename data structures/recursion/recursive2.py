import snoop

 
i =100;
while i>0:
    print(i)
    i=i-1
 

 #TODO:  FACT0RIAL PROGRAMM
 

def god (n):
    if n<=1:
        return 1
    else:
        return n * god(n-1)
print(god(5))
    

#TODO:  1 TO 100 IN  REVERSE
@snoop    
def god(n):
        if n<=0:
            return 0
        else:
            print(n)
            god(n-1)
god(99)