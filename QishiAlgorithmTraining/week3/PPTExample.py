"""
Example 1: valid parenthesis
 Given a string containing just the characters '(', ')', '{',
'}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of
brackets.
2.Open brackets must be closed in the correct order.
"""

s=[e for e in "{}[]()(()){()}"]

def isValid(s):
    stack=[]
    dict_parenthesis={'{':'}','[':']','(':')'}
    if len(s) %2 ==1:
        return False
    for e in s:
        if e in dict_parenthesis.keys():
            stack.append(e)
        else:
            if len(stack)==0:
                return False
            if not dict_parenthesis[stack.pop()] ==e:
                return False
    if len(stack)>0:
        return False

    return True 


print(isValid(s))

"""
You are given two arrays (without duplicates) nums1
and nums2 where nums1’s elements are subset of
nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.
 The Next Greater Number of a number x in nums1 is
the first greater number to its right in nums2. If it does
not exist, output -1 for this number.
"""
num1=[4,1,2]
num2=[1,3,4,2]
#num2=[9,3,4,1,0,0,2,5,10]


def nextGreaterElement(num1,num2):
    #find all next greater Element for num2's element first
    dict_ng=dict()
    stack=[]
    for n in num2:
        while stack and stack[-1]<n:
            dict_ng[stack.pop()]=n
        stack.append(n)

    result=[]
    for n in num1:
        if n in dict_ng.keys():
            result.append(dict_ng[n])
        else:
            result.append(-1)
    return result


print(nextGreaterElement(num1,num2))



"""
Infix->POSTfix
2+(2+3)+3*5+1
223++35*+1+

2+(2+3)*3+1
 223+3*+1+

3
+
3 
2 *
2 + 

1+2*3+(4+5)\2
123*+45+2\+

2
+
5
4
+
*
3  
2  \
1  +
s1 s2

1) num go s1   char go s2 
2) s2 none empty new char>=s2.top push new char to s2
3) s2 none empty new char<s2.top   pops2->s1  newchar->s1
4) ( push to s2
5) ) pops2 until meet ( ->s1
6) s2 not none pop s2->s1
7)s1top is char if newchar<=s1top s1.top append(newchar) else s2.append(newchar)
"""
s=[e for e in "2+(2+3)*3+1"]

dictlevel={'*':2,'\\':2,'+':1,'-':1,"(":0}

num=set([ e for e in "1234567890"])

s1=[]
s2=[]

while s:
    e=s.pop(0)  
    if e=="(":
        s2.append(e)
        continue
    if e==")":
        s2pop=s2.pop()
        while not s2pop=='(':
            s1.append(s2pop) 
            if s2:
                s2pop=s2.pop()
        continue

    if e in num:
        s1.append(e)
    else:
        if s1[-1] not in num:
            if  dictlevel[e]<=dictlevel[s1[-1]]:
                s1.append(e)
            else:
                s2.append(e)
            continue
            
        if s2==[]:
            s2.append(e)
        else:
           if dictlevel[e] >= dictlevel[s2[-1]]:
               s2.append(e)
           else:
               s1.append(s2.pop())
               s1.append(e)
     
while s2:
    s1.append(s2.pop())

print("".join(s1))
 
#------------------ ppt version-is wrong. Forget to check s1 top is op. The right one as follow------------- 
def infix2posfix(infixexpr):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    opStack=[]
    postfixList=[]
    tokenList= [e for e in infixexpr]
    
    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token=='(':
            opStack.append(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken !='(' and len(opStack)!=0:
                postfixList.append(topToken)
                topToken=opStack.pop()
        else:
            #check s1 top is op.  new op<= s1topop  s1.push(newop)  
            if not postfixList[-1] in "0123456789":
                if  prec[token]<=prec[postfixList[-1]]:
                    postfixList.append(token)
                else:
                    opStack.append(token)
            else:
                if opStack==[]:
                    opStack.append(token)
           
                elif not len(opStack)==0 and prec[opStack[-1]]>prec[token]:
                    postfixList.append(opStack.pop()) 
                    postfixList.append(token)
                else:
                    opStack.append(token)
   
    while opStack:
        postfixList.append(opStack.pop())
    print("".join(postfixList)) 

infix2posfix("2+(2+3)*3+1")

"""
infix2prefix

2+(2+3)*3+1

++2*+2331
""

