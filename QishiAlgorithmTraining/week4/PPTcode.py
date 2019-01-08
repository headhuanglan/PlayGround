class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Queue(object):
    def __init__(self):
        self.size=0
        self.front=None
        self.end=None
    def isEmpty(self):
        return self.front is None
    def enQueue(self,x):
        node=ListNode(x)
        if self.isEmpty():
            self.front=node
        else:
            self.end.next=node
        self.end=node
        self.size+=1
    def deQueue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        temp=self.front.val
        self.front=self.front.next
        if self.front is None:
            self.end=None
        self.size-=1
        return temp

Q=Queue()
for i in range(10):
    Q.enQueue(i)

for _ in range(10):
    print(Q.deQueue())




