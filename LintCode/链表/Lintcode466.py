'''466. 链表节点计数 
计算链表中有多少个节点
样例
给出 1->3->5, 返回 3.
'''

class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        if not head:
            return 0
        i = 0
        while head.next:
            i += 1
            head = head.next
            
        i += 1
        return i

