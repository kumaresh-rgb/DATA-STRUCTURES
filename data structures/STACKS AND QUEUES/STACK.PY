class  node:
    
    def __init__(self,value=None):
        self.value=value
        self.next=next
        
class linkedlist:
    def __init__(self):
        self.head=None
        
    def __iter__(self):
        iterate=self.head
        while iterate:
            yield iterate
            iterate=iterate.next
        
class stack:
    def __init__(self):
        self.linkedlist=linkedlist()
        
    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    def push(self,value):
        newnode = node(value)
        newnode.next = self.linkedlist.head
        self.linkedlist.head = newnode
    
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode =  self.linkedlist.head.value
            self.linkedlist.head =  self.linkedlist.head.next
            return poppednode
        
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.linkedlist.head.value
        
    '''def delete(self):
        self.linkedlist.head = None'''
        
        
        
cstack=stack()
print(cstack.isempty())
print(cstack.push(10))
print(cstack.push(20))
print(cstack.push(30))
print(cstack.push(40))
print(cstack.push(50))
print(cstack.isempty())
print(cstack.peek())
print(cstack.pop())
print(cstack.peek())


