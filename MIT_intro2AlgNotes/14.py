#dfs

"""
parent={s:None}
DFS-visit(V,Adj,s):
    for v in Adj[s]:
       if v not in parent:
          parent[v]=s
          DFS-visit(V,adj,v)

A  B- C - F
 \ |   \  |
   D - E  G
"""

Adj={"A":["D",],"D":["A","B","E"],"B":["C","D"],"C":["B","E","F"],"E":["D","C"],"F":["C","G"],"G":["F",]}

V=["A","B","C","D","E","F","G"]
def DFS(V):
    parent=dict()
    def DFS_visit(s,Adj=Adj):
        for v in Adj[s]:
            if v not in parent.keys():
                parent[v]=s
                DFS_visit(v,Adj)

    for s in V:
        if s not in parent.keys():
            parent[s]=None
            DFS_visit(s,Adj=Adj)
    return  parent

print(DFS(V))

#O(E+V)


#topological sort
"""
RUN DFS
output the reverse time of finishing times 
"""



