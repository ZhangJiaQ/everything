"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        '''
        112. 删除排序链表中的重复元素
        给定一个排序链表，删除所有重复的元素每个元素只留下一个。
        
        样例
        给出 1->1->2->null，返回 1->2->null
        
        给出 1->1->2->3->3->null，返回 1->2->3->null
        '''
        if not head:
            return None
        # write your code here
        _first = head
        _next = head.next
        while _next:
            if _next.val == _first.val:
                _first.next = _next.next
            else:
                _first = _first.next
            _next = _next.next
        return head