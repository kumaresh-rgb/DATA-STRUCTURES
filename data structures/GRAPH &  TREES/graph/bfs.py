from collections import deque
import snoop


class graph:
   
    def __init__(self,dict=None):
        if dict is None:
            dict={}
        self.dict=dict
      
    def addvertex(self,vertex,adjacent):
        self.dict[vertex].append(adjacent)
        
       
    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            devertex=queue.pop(0)
            print(devertex)
            for adjacentvertex in self.dict[devertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)
   
    
cdict={
    
    "a" :["b","c"],  
    "b" :["a","d","e"], 
    "c" :["a","e"],
    "d" :["b","e","f"],
    "e" :["d","f"],
    "f" :["d","e"]
}

op=graph(cdict)
op.bfs("a")




