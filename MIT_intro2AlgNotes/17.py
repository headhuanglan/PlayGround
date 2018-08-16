#Bellman-Ford   can handle negative weight  which causing inf loop
"""
Relax(u,v,w):
if d[v]>d[u]+w(u,v)
    d[v]=d[u]+w[u,v]
    pi[v]=u


BF(G,W,s)
   Initilize()
   for l=1 to |V|-1
        for each edge(u,v) in E
             Relax(u,v,w)

    for each eges(u,v) in E
        if d[v]>d[u]+w(u,v)
          then negative cycle path exists

O(VE)

"""

