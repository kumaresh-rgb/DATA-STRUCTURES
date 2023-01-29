class node:            
    '''
     IN BETWEEN NODES IN LINKEDLIST
    '''         
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
        
    def middle(self,prenode,newdata):
        if prenode is None:
            print("exist") 
            return
        newnode=node(newdata)
        newnode.nextref=prenode.nextref
        prenode.nextref=newnode
        
        
    def append(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while(temp.nextref):
            temp=temp.nextref
            temp.nextref=newnode
       
    def printlist(self):         # TODO PRINT THE NODE
        temp=self.head
        while (temp):
            print(temp.data,end='')
            temp=temp.nextref
         
      
           
        
l1=linkedlist()
                              #todo connecting the nodes second to third
l1.append(6)
l1.insert(1) 

l1.insert(7)                   #todo inserting the node calling before printlist()


l1.middle(l1.head.nextref,8)

l1.printlist()                  #todo callling the printfunction
