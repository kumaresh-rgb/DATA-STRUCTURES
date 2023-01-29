import snoop

class graph:
    @snoop  
    def __init__(self,dict=None):
        if dict is None:
            dict={}
        self.dict=dict
    @snoop 
    def addvertex(self,vertex,adjacent):
        self.dict[vertex].append(adjacent)
        
    @snoop  
    def bfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            devertex=stack.pop()
            print(devertex)
            for adjacentvertex in self.dict[devertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)
   
    
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

