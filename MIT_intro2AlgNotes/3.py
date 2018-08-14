l=[2,4,7,3,5,1,9,8,100,22,3,145]
#for i =1,2,...n
#insert l[i] into sorted array l[0:i-1]
#by pair swap down to the correct position
#O(n^2)
# def insertsort(l):
#     for i in range(1,len(l)):
#         curvalue=l[i]
#         pos=i
#
#         while pos>0 and l[pos-1]>curvalue:
#             l[pos]=l[pos-1]
#             pos=pos-1
#
#         l[pos]=curvalue
#
#     return l


# def insertsort(l):
#     for i in range(1,len(l)):
#         curval=l[i]
#         pos=i
#         while curval<l[pos-1] and pos-1>=0:
#             l[pos]=l[pos-1]
#             pos-=1
#         l[pos]=curval
#     return l



def insertsort(l):
    for i in range(1,len(l)):
        pos=i
        val=l[pos]
        while val< l[pos-1] and pos-1>=0:
            l[pos]=l[pos-1]
            pos-=1
        l[pos]=val
    return l

# def merge(l,r):
#     if len(l)==0:
#         return r;
#     if len(r)==0:
#         return l;
#     result=[]
#     while len(l) and len(r):
#         lval=l[0]
#         rval=r[0]
#         if lval<rval:
#             result.append(lval)
#             l=l[1:]
#         else :
#             result.append(rval)
#             r=r[1:]
#     if len(l)==0 and len(r)>0:
#         result.extend(r)
#     if len(r)==0 and len(l)>0:
#         result.extend(l)
#     return result
#
#
# def mergesort(l,lo=0,hi=None):
#
#     mid=(lo+hi)//2
#
#     if mid==lo:
#         return [l[lo],]
#
#     left=mergesort(l,lo,mid)
#     right=mergesort(l,mid,hi)
#     result=merge(left,right)
#     return result


def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        v1=left[0]
        v2=right[0]
        #!!! note  <=  in case to merge same value and loop forever.
        if v1<=v2:
            result.append(v1)
            left=left[1:]
        if v2<=v1:
            result.append(v2)
            right=right[1:]
    if len(left)>0:
        result.extend(left)
    if len(right)>0:
        result.extend(right)
    return result



def mergesort(l,lo,hi):
    mid=(lo+hi)//2
    if lo==mid:
        return [l[lo],]
    left=mergesort(l,lo,mid)
    right=mergesort(l,mid,hi)
    result=merge(left,right)
    return  result



#print(merge([1,2,3,4,5,7],[3,8,9,22,100,145]))

print(mergesort(l,lo=0,hi=len(l)))




