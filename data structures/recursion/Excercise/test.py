from multiprocessing.connection import answer_challenge
import snoop

'''
list=[2,7,6,3]    
def test(l):
    for i in range (len(l)-1):
        for j in range (len(l)):
            print(l[i],l[j])
            
test(list)'''


'''    

list=[2,7,6,3]    
def test(l):
    for i in range (len(l)):
        for j in range (len(l)-1):
            print(l[i],l[j])
            
test(list)'''


'''@snoop
#todo 
def wipro(a,b):
    add=sub=mul=""
    t1=t2=t3=0
    for i in range (len(a)):
        t1=int(a[i])+int(b[i])
        t2=int(a[i])-int(b[i])
        t3=int(a[i])*int(b[i])
        
        add=add+str(t1)
        sub=sub+str(t2)
        mul=mul+str(t3)
        print(add,sub,mul)
        
a=input("enter the no:")
b=input("enter thr no:")
       
        
        
wipro(a,b)'''



#todo a archietecture firm
'''@snoop
def minmaxsum(num):
    a=list(map(int,input().split()))
 
    print(max(a)+min(a))
    
n=int(input("enter"))
minmaxsum(n)'''


#todo A space research agency
'''@snoop
def negative(num):
    a=list(map(int,input().split()))
    temp=0
    for i in a:
        if i<0:
            temp+=1
            print(temp)   
n=int(input("enter"))
negative(n)'''


'''@snoop
def loop(list):
    for i in range(len(a)):
        for j in range(len(a)):
            print (a[i])
n=int(input("enter"))
a=list(map(int,input().split()))
            
print(loop(n))'''
            
 
n=int(input("enter"))
b=list(map(int,input().split())) 
            

for i in range(len(b)):
    for j in range(len(b)):
        print(j,end="")

            