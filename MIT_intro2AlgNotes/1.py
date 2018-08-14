l=[1,2,10,6,5,4,1,0]

def findpeak(l):
    lenl=len(l)
    if lenl<3:
        raise Exception("error to find peak for 2 element")
    for i in range(lenl-2):
        pre=l[i]
        cur=l[i+1]
        nxt=l[i+2]
        if cur>pre and cur>nxt:
            return cur

def findpeak_opt(l,lo=0,hi=None):
    mid=(hi+lo)//2
    if l[mid]<l[mid-1]:
        leftPeak=findpeak_opt(l,lo,mid)
        return leftPeak
    elif l[mid]<l[mid+1]:
        rightPeak=findpeak_opt(l,mid,hi)
        return rightPeak
    else:
        return l[mid]
        
print(findpeak(l))
print(findpeak_opt(l,0,len(l)))



