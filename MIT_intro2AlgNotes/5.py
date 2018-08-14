#air plain schedual
# |      |    |            |     |               |
# within 3 min can land

#binary search tree.

#               30
#       17              40
# 14        20
#
# node X  key(x)
# pointers  parent(x)
#           left(x)
#           right(x)
#
# For all nodes, if y in left subtree of x , key(y)<=key(x)
#                   y                              >=

# ArrayInsert  shifting  O(n)
# Linklist    random access is slow  O(n)
# min_heaps/max_heap  not check the other brunch.  element is <=K or >=K from t take O(n)
#
#
# binary search tree  insertion take O(log(n))  easy to check inserting value <=or >= exists value within K

# find_min go to left hit leaf O(lgn)
# next_larger(x)  O(lgn)



#----Augmented BST structure-----------------------------------
# rank(t)== number of planes land<=t
#
# node contains info of how many planes below
#
#
#
#                   49  6
#
#       46   2                    79  3
#
# 43  1                  64   1            85  1

l=[49,46,79,43,64,85]

class node(object):
    def __init__(self,parent,value):
        self.parent=parent
        self.value=value
        self.left=None
        self.right=None
    def setleft(self,left):
        self.left=left
    def setright(self,right):
        self.right=right

def insert(bst,value,k=3):

    if value >=bst.value:
        if bst.right:
            insert(bst.right,value)
        else:
            if abs(bst.value - value) >= k:
                bst.right=node(bst,value)

    else:
        if bst.left:
            insert(bst.left,value)
        else:
            if abs(bst.value - value) >= k:
                bst.left=node(bst,value)

def findmin(bst):
    while bst.left:
        bst=bst.left
    return bst.value


def findnextlarge(bst):
    if bst.right:
        return findmin(bst.right)
    else:
        #bst right=None
        #         Root
        #       /     \...
        #     *
        #   /   \
        #  0    y
        # 0   0  bst
        y=bst.parent
        while y and bst==y.right:
            bst=y; y=y.parent

        return y.value


def printbst(bst):
    if bst.left:
        printbst(bst.left)
    print(bst.value)
    if bst.right:
        printbst(bst.right)









bst=node(None,l[0])

for value in l[1:]:
    insert(bst,value)


printbst(bst)
print("#"*10)
print(findmin(bst))


print(findnextlarge(bst.right.left))