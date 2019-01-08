#https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
#DP        
#        gp[i]=  set( gp[i-1]  insert at   -|- |- |- |- |- |-         n=3 
         
        gp=[None for _ in range(n+1)]
        gp[1]=set(["()"])
        for i in range(2,n+1):
            gpi_set=set()
            for pt in gp[i-1]:
                #insert at pos j
                for j in range(2*(i-1)+1):
                    new_pt= pt[0:j]+ "()"+pt[j:len(pt)+1]
                    if new_pt not in gpi_set:
                        gpi_set.add(new_pt)
            gp[i]=gpi_set
        
        result=[]
        for pt in gp[n]:
            result.append(pt)             
                   
        return result
        
    
    
        
# binary brute force too slow---------------------------------        
#         mydict={'1':'(','0':')'}
#         result=[]
#         bit=n*2
#         for i in range(1<<(bit-1),2**bit):
#             "((()))"
#             "111000"
#             "()))(("
#             "100011"
#             mysum=0
#             ii=i #make a copy >> will change the value
#             Flag=True
#             for shift in range(bit):
#                 cur=ii>>shift & 1
#                 if shift==0 and cur !=0:
#                     Flag=False
#                 if shift==bit-1 and cur !=1:
#                     Flag=False
#                 if cur==0:
#                     mysum-=1
#                 if cur==1:
#                     mysum+=1
#                 if mysum>0:
#                     Flag=False
#             if mysum!=0:
#                 continue
#             if Flag:
#                 result.append(bin(i))

#         #parse result
#         r=[]
#         for val in result:
#             val=val[2:]  #drop 0b
#             parenthese=''.join([ mydict[e] for e in val])
#             r.append(parenthese)
#         return r

