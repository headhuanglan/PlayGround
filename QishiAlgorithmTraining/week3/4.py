#https://leetcode.com/problems/next-greater-element-iii/description/

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        
        11285973
        
        s=[3]
        1128597
        
        s=[3,7]
        112859
        
        1128 7 
        
        l>p and s yes!
           find p a new val must be small in 3 7 9 and max then 5 
           min=999
           for e in  (s and l)
              if e>p and e<min:
                   e=min
           min=7
           pre=min
             str+sort(s+l)  ok 
        
       
        
        
        """
        if n<10 or n>=2**32-1:
            return -1
        
        num=str(n)
        last=None
        pre=None
        s=[]
        while len(num)>=2:
            last=num[-1]
            pre=num[-2]
            
            if int(last)>int(pre):
                if s==[]:
                    return int(num[:-2]+last+pre) if int(num[:-2]+last+pre)<=2**32-1 else -1
                else:
                     
                    min_=float("inf")
                    for e in s+[last]:
                        if int(e)>int(pre) and int(e)<min_:
                            min_=int(e)
                    new_pre=str(min_)
                     
                    newpre_2end=s+[last]+[pre]
                    newpre2end=[]
                    firstflag=True
                    for e in newpre_2end:
                        if e==new_pre and firstflag:
                            firstflag=False
                            continue
                        newpre2end.append(e)
                    newpre2end=sorted(newpre2end)
                    r=num[:-2]+new_pre+"".join(newpre2end)
                    return int(r) if int(r)<=2**32-1 else -1
                        
                    
                    
                    
            else:
                s.append(num[-1])
                num=num[:-1]
        
        return -1
    
        
        """
        did not pass test  don't know why!!!  The output is clearly a right answer.
        Input:  2147483647
        Output: 2147483674
        Expected: -1
        """
        
        
        
        
        
        
        
        
        
