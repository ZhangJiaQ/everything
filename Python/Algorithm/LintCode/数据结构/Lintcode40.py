'''
40. Implement Queue by Two Stacks 

As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

And I don't know why i can't push it on github
'''

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.L1 = []
        self.L2 = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        
        self.L1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        while self.L1:
            temp = self.L1.pop()
            self.L2.append(temp)
        a = self.L2.pop()
        while self.L2:
            self.L1.append(self.L2.pop())
        return a

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.L1) > 1:
            temp = self.L1.pop()
            self.L2.append(temp)
        a = self.L1.pop()
        self.L1.append(a)
        print a
        while self.L2:
            self.L1.append(self.L2.pop())

        return a



