'''class node:            
 
    def __init__(self,data=None):
        self.data = data 
        self.nextref=None
        
class linkedlist:
    def __init__(self): 
        self.head=None           # Todo head node intialize
        

            
    def insert(self,newdata):    #Todo insertng at beginning of the node
        newnode=node(newdata)
        newnode.nextref =self.head
        self.head=newnode
        

            
    def deletef(self):
        if(self.head!=None):
            temp=self.head
            self.head=self.head.nextref
            temp=None
       
    def printlist(self):         # TODO PRINT THE NODE
        temp=self.head
        while (temp):
            print(temp.data,end='')
            temp=temp.nextref
         
      
           
        
l1=linkedlist()
                              #todo connecting the nodes second to third

 
                             #todo inserting the node calling before printlist()
l1.insert(10)
l1.insert(9)
l1.insert(8)
l1.insert(7) 


l1.deletef()
l1.printlist()  '''                #todo callling the printfunction


a=2
b=3
b=a
print(a)
print(b)