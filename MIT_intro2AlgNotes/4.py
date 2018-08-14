#priority Queue
#a set of element each element with a key

#insert(S,x) insert element x into set S
#max(S) return element with the largest key
#extract_max(s)  and remove from queue
#increase_key(S,x,k) increase the element  x's key to k

#heap
#A array visulizaed as nearly completed binary tree.

#                        1
#                 2            3
#            4        5   6        7
#
#
# root of tree is first element (i=1)
# parent(i)=i//2
# left(i)=2i  right(i)=2i+1
#
# Max-heap property: the key of a node is >= the keys of its childern
#
#
# max_heapify: correct a single violation in the heap property in a subtree s root
#              assume trees rooted at left(i) and right(i) are maxheaps
#
#
# convert A[1..n] into max_heapify
# Build_max_heap(A):          #  need  O(nlogn) to build
#     for i =n//2 downto 1    # A[n/2+1 ....n] are all leaves
#            do max_heapilify(A,i)_

# heapsort  O(nlogn)
# 1Buld_max_heap from unsorted array
# 2find max element A[1]
# 3swap elements A[n] with A[1] now max element at end of the array
# 4discard last n from heap  decease heap size
# 5 new root may violate maxheap but childern are maxheaps run maxheaplify



#first element is the size of arrary
#tree view as follow
    #          2
    #    6           3
    # 1    5      8

l=[6,2,6,3,1,5,8]

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def max_heapify(l,i):
    heapsize=l[0]
    l_=left(i)
    r_=right(i)
    if(l_<=heapsize and l[l_]>l[i]):
        largest=l_
    else:
        largest=i

    if(r_<=heapsize and l[r_]>l[largest]):
        largest=r_

    if not largest==i:
        #exchange A[i] and A[largest]
        l[i],l[largest]=l[largest],l[i]
        max_heapify(l,largest)




def build_max_heap(l):
    length=l[0]
    for i in range(length//2,0,-1):
        max_heapify(l,i)
    return l

def heapsort(l):
    result=[]
    heapsize_original=l[0]
    l = build_max_heap(l)
    for _ in range(heapsize_original):
        maxelement=l[1]
        heapsize=l[0]
        l[1],l[heapsize]=l[heapsize],l[1]
        l=l[:-1];l[0]-=1;result.append(maxelement)
        max_heapify(l,1)
    return result


print(heapsort(l))