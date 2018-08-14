#comparision model   O(nlogn)

#
# integer sorting
#
#   counting sort:
#           3 5 7 5 5 3 6
#
#  0 1 2 3 4 5 6 7 8 9
#        2   3 1 1


l=[3,5,7,5,5,3,6]
def integersort(l):
    counter=[ [] for i in range(10)]
    for e in l:
        counter[e].append(e)
    res=[]
    val=0
    for i in counter:
        if not i==[]:
            res.extend(i)
        val+=1

    return res

print(integersort(l))

#radix sort  O(n)

# imagine each interge as base b
#
# #digits =d=log_b(K)
#
# sort ints by least significant interge
# sort...
# sort...


def key(number,bitpos):
    return  int([e for e in str(number)][bitpos])

def countingsort_with_key(A,bitpos=0):
    L=[[] for _ in range(10)]

    for j in range(len(A)):
        L[key(A[j],bitpos)].append(A[j])

    output=[]

    for i in range(10):
        output.extend(L[i])

    return output

l=[329,457,657,839,436,720,355]

def radixsort(l):
    for bitpos in range(2,-1,-1):
        l=countingsort_with_key(A=l,bitpos=bitpos)

    return l

print(radixsort(l))







