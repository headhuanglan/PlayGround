#https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=[]
        self.size=0
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        self.size+=1
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.size !=0:
            top=self.data[0]
            self.data=self.data[1:]
            self.size-=1
            return top
        else:
            return False
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.size==0:
            return None
        else:
            return self.data[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.size==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
