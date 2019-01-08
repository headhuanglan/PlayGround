#https://leetcode.com/problems/queue-reconstruction-by-height/description/

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        """    copy from answer
            Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, 
            therefore each guy's index     will be just as same as his k value.
            For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
        E.g.
        input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        subarray after step 1: [[7,0], [7,1]]
        subarray after step 2: [[7,0], [6,1], [7,1]]
        ...
        """
 
 
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []
        
        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res


        
