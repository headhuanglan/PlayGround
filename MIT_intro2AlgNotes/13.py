#quick short
l=[3,2,1]


def quickshort(l,lo=0,high=None):
    if lo < high:
        pivot=high
        cur=lo
        while cur<pivot:
            if l[cur]>=l[pivot]:
                l[cur],l[pivot-1],l[pivot]=l[pivot-1],l[pivot],l[cur]
                pivot-=1
            else:
                cur+=1

        quickshort(l,lo,pivot-1)
        quickshort(l,pivot+1,high)
        return l





print(quickshort(l,0,len(l)-1))

#note !!!    l[cur]=l[pivot-1] exchange first, to avoid overwrite l[cur] eg: l[3,1,2]  pos 1 is pivot, cur=0 .
#note !!!    quickshort(l,lo,pivot-1)   must pivot-1 to avoid inf loop.


#-----------------------BFS-------------------------
"""

BFS(s,Adj)
   level={s:0}
   parent={s:None}
   i=1
   frontier=[s]
   while frontier:
       next=[]
       for u in frontier:
          for v in Adj[u]
              if v not in level
                  level[v]=i
                  parent[v]=u
                  next.append(v)
       frontier=next
       i+=1
 
A  B- C - F
 \ |   \  |
   D - E  G
"""

Adj={"A":["D",],"D":["A","B","E"],"B":["C","D"],"C":["B","E","F"],"E":["D","C"],"F":["C","G"],"G":["F",]}

def bfs(s,Adj=Adj):
    level={s:0}
    parent={s:None}
    i=1
    frontier=[s,]
    while frontier:
        next=[]
        for u in frontier:
            for v in Adj[u]:
                if v not in level.keys():
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier=next
        i+=1
    return level

print(bfs("D",Adj))