#Dijkstra
"""

Relax(u,v,w):
if d[v]>d[u]+w(u,v)
    d[v]=d[u]+w[u,v]
    pi[v]=u

Dijkstr(G,W,s)
   init(G,s) S={}  Q=V[G] d[s]=0     #Q in priority Q by d()
   while Q != {}
         u =extractmin(Q)
         S=S U  {u}
         for each v in Adj[u]
               relax(u,v,w)



"""
