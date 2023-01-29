
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
        
    def middle(self,pos,newdata):
        newnode=node(newdata)
        if pos< 1:
            print("exist") 
        elif (pos==1):
            newnode.nextref =self.head
            self.head=newnode
        else:
            temp=self.head
            for i in range(1,pos-1):
                if(temp!=None):
                    temp=temp.nextref
            if(temp!=None):
                newnode.nextref=temp.nextref
                temp.nextref=newnode
            else:
                print("null")
        
    def append(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while(temp.nextref):
            temp=temp.nextref
            temp.nextref=newnode
            
            
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

l1.insert(1) 
l1.insert(7)                   #todo inserting the node calling before printlist()
l1.insert(8)
l1.insert(9)

l1.deletef()
l1.middle(6,10)
l1.middle(7,38)



l1.append(6)
l1.printlist()                  #todo callling the printfunction
