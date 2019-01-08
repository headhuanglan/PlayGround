#https://leetcode.com/problems/design-circular-queue/description/

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.QueueSize=k
        self.data=[None for _ in range(k+1)]
        self.pt1=0
        self.pt2=0
        self.ndata=0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.ndata==self.QueueSize:
            return False
        
         
        if self.ndata==0:
            #first insertion
            self.data[self.pt1]=value
            self.ndata+=1
            self.pt2=self.pt1
        else:
            self.pt2=(self.pt2+1) % self.QueueSize
            self.data[self.pt2]=value
            self.ndata+=1
        
        return True
        
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        """
        ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"] 
        [[6],[6],[],[],[],[5],[],[],[],[],[],[]]
        
        _ 1_ _ _ _ _
        """
        
        if self.ndata==0:
            return False
        
        element=self.data[self.pt1]
        
        self.pt1=(self.pt1+1) % self.QueueSize
        self.ndata-=1
        
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.ndata==0:
            return -1
        
        return self.data[self.pt1]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.ndata==0:
            return -1
        
        return self.data[self.pt2]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.ndata==0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.ndata==self.QueueSize:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
