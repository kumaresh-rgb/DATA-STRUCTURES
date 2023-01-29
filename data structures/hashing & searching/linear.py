import snoop

@snoop
def linear(array,value):
    for i in range (len(array)):
        if array[i] == value:
            return print(i) 
    return print(-1)
    
linear([24,34,567,1,2,80],1)



def linear(array,value):
    for i in range (len(array)):
        if array[i] == value:
            return print(i)  ,array[i]
    return print(-1)
    
linear([24,34,567,1,2,80],1)



