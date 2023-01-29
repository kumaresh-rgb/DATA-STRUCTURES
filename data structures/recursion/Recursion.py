def hund(n):
    if n<1:
        print ("you tyoe above hundered")
    else:
        print(n)
        hund(n-1)
        
          
hund(100)


def Rev( n ):
    if n > 0 :
        print( n )
        Rev( n-1 )
        
        
Rev(1)


