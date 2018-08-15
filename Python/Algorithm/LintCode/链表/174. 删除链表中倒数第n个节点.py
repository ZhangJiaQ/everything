"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
		"""
		174. 删除链表中倒数第n个节点
		给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。



		样例
		给出链表1->2->3->4->5->null和 n = 2.

		删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.

		挑战
		O(n)时间复杂度

		注意事项
		链表中的节点个数大于等于n
		"""
        if not head:
            return None
        # write your code here
        link_length = 0
        temp = head
        while temp:
            link_length += 1
            temp = temp.next
        print(link_length)
        temp = head
        if n == link_length:
            return head.next
        for i in range(link_length-n-1):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        else:
            return None
        return head